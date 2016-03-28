__author__ = 'Stepiuk'
from os import system
from model import Model
import view
import getch

user_input = None
model = Model()


def render(items=model):
    """
    Render given items
    and user menu
    :param items: items to render
    :return:
    """
    system("clear")
    for i in items:
        view.render_item(i.get_first(), i.get_second(), i.get_result(), i.get_date())
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


def user_action_handler():
    """
    Handle user actions:
    e -> exit
    s -> search by team
    space -> full table
    :return:
    """
    if user_input == ' ':
        render()
    elif user_input == 'e':
        exit(0)
    elif user_input == 's':
        render(model.get_by_team(input()))


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
    render()
    while True:
        read_input(getch.getch())


main_loop()
