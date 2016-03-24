"""
>>> from model import *

>>> from view import *

>>> import coverage

>>> render_action()
Now write name of team
>>> render_menu()
            - Space to view all matches
            - E to exit
            - S to search
>>> render_item("a","b","2:0","03.02.2016")
03.02.2016
a vs b  2:0  03.02.2016


>>> a = MatchResult('Lester', 'Everton', '2:0', '03.18.16')
>>> a.get_date()
'03.18.16'
>>> a.get_first()
'Lester'
>>> a.get_second()
'Everton'
>>> a.get_result()
'2:0'
>>> items = get_by_team('Lester')

>>> i = items[0]

>>> render_item(i.get_first(), i.get_second(), i.get_result(), i.get_date())
03.18.16
Lester vs Everton  2:0  03.18.16


"""

if __name__ == "__main__":
    import doctest

    doctest.testmod()
