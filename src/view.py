__author__ = 'Zhydenko'

def render_item(team1, team2, score, date):
    print(team1 + " vs " + team2 + "  " + score + "  " + date)
    return

def render_menu():
    print ("""
            1.Space to view all matches
            2.E to exit
            3.S to search
    """)
    return