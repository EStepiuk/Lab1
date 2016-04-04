__author__ = 'Stepiuk'
from os import system
from model import Model
import sear_json
import sear_pickle
import sear_yaml
import ConfigParser
import view
import getch
import functools


user_input = None
model = Model()
config = ConfigParser.ConfigParser()
backup_functions = []


def render(items=model.get_all_games()):
    """
    Render given items
    and user menu
    :param items: items to render
    :return:
    """
    system("clear")
    for i in items:
        view.render_item(i[0], i[1], i[2], i[3])
    view.render_menu()


def notify(observer):
    """
    Decorator to notify
    given observer about event
    :param observer: observer to notify
    :return:
    """

    def decorator(f):
        def wrapper(*args):
            res = f(*args)
            observer()
            return res

        return wrapper

    return decorator


def backup_data():
    for f in backup_functions:
        f()


def register(observer):
    backup_functions.append(observer)


def unregister(observer):
    backup_functions.remove(observer)


model.add_result = notify(backup_data)(model.add_result)
sear_yaml.write = functools.partial(sear_yaml.write, obj=model.England)
sear_json.write = functools.partial(sear_json.write, obj=model.England)
sear_pickle.write = functools.partial(sear_pickle.write, obj=model.England)


def configure():
    config.read("../config.ini")
    restore_from = config.get("Restore", "from")
    if restore_from == "yaml":
        model.copy(sear_yaml.read())
    if restore_from == "json":
        model.copy(sear_json.read())
    if restore_from == "pickle":
        model.copy(sear_pickle.read())

    if config.getboolean("BackUp", "yaml"):
        register(sear_yaml.write)
    if config.getboolean("BackUp", "json"):
        register(sear_json.write)
    if config.getboolean("BackUp", "pickle"):
        register(sear_pickle.write)


def user_action_handler():
    """
    Handle user actions:
    e -> exit
    s -> search by team
    a -> add result
    space -> full table
    :return:
    """
    if user_input == ' ':
        render()
    elif user_input == 'e':
        exit(0)
    elif user_input == 's':
        render(model.get_by_team(raw_input("Input team name: ")))
    elif user_input == 'a':
        model.add_result(raw_input("First team name: "), raw_input("Second team name: "),
                         raw_input("Score in format g:g: "), raw_input("Date in format mm.dd.yy: "))
        render()


@notify(user_action_handler)
def read_input(input_):
    """
    Reads user input and
    notify user_action_handler()
    when user act
    :param input_: user input
    :return:
    """
    global user_input
    user_input = input_


def main_loop():
    """
    Main lifecycle
    :return:
    """
    configure()
    render()
    while True:
        read_input(getch.getch())
    backup_data()


main_loop()
