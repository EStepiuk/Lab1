__author__ = 'Zhydenko'

def render_item(team1, team2, score, date):
    print("\n"+date)
    print(team1 + " vs " + team2 + "  " + score + "  " + date)
    return

def render_menu():
    print ("""
            - Space to view all matches
            - E to exit
            - S to search
    """)
    return