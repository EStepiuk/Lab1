__author__ = 'Zhydenko'


def render_item(team1, team2, score, date):
    """
    Write one MatchResult on screen
    :param team1:
    :param team2:
    :param score:
    :param date:
    :return:
    """
    print(date)
    print(team1 + " vs " + team2 + "  " + score + "  " + date)
    return


def render_action():
    print("Now write name of team")


def render_menu():
    """
    Write on screen menu
    :return null
    """
    print ("""            - Space to view all matches
            - E to exit
            - S to search""")
    return
