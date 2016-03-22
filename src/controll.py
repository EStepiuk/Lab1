__author__ = 'dnt'
from os import system
import model
import view
import getch


def main_loop():
    for t in model.England:
        view.render_item(t.get_first(), t.get_second(), t.get_result(), t.get_date())
    while True:
        user_interaction_handler()


def user_interaction_handler():
    c = getch.getch()
    system("clear")
    if c == ' ':
        for t in model.England:
            view.render_item(t.get_first(), t.get_second(), t.get_result(), t.get_date())
    elif c == 'e':
        exit(0)
    elif c == 's':
        items = model.get_by_team(raw_input())
        for i in items:
            view.render_item(i.get_first(), i.get_second(), i.get_result(), i.get_date())
    view.render_menu()


main_loop()