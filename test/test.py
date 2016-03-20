"""

>>> from controller import *

>>> from model import *

>>> from view import *

>>> import coverage

>>> england(first)
Lester vs Everton - 2:0 on 26/2/2016 in England
MU vs Everton - 3:0 on 27/2/2016 in England
Chelsea vs Everton - 0:0 on 28/2/2016 in England
Arsenal vs Everton - 1:0 on 29/2/2016 in England

>>> spain(first)
Barcelona vs Everton - 2:0 on 26/2/2016 in Spain
Real vs Everton - 2:0 on 27/2/2016 in Spain
Sevilla vs Everton - 2:0 on 28/2/2016 in Spain
Eibar vs Everton - 2:1 on 29/2/2016 in Spain

>>> ukraine(first)
Dynamo vs Everton - 2:4 on 26/2/2016 in Ukraine
Vorskla vs Everton - 2:2 on 27/2/2016 in Ukraine
Stal vs Everton - 2:6 on 28/2/2016 in Ukraine
Dnipro vs Everton - 2:7 on 29/2/2016 in Ukraine

>>> sort_goals(first)
Dnipro vs Everton - 2:7 on 29/2/2016 in Ukraine
Stal vs Everton - 2:6 on 28/2/2016 in Ukraine
Dynamo vs Everton - 2:4 on 26/2/2016 in Ukraine
Vorskla vs Everton - 2:2 on 27/2/2016 in Ukraine
MU vs Everton - 3:0 on 27/2/2016 in England
Eibar vs Everton - 2:1 on 29/2/2016 in Spain
Lester vs Everton - 2:0 on 26/2/2016 in England
Barcelona vs Everton - 2:0 on 26/2/2016 in Spain
Real vs Everton - 2:0 on 27/2/2016 in Spain
Sevilla vs Everton - 2:0 on 28/2/2016 in Spain
Arsenal vs Everton - 1:0 on 29/2/2016 in England
Chelsea vs Everton - 0:0 on 28/2/2016 in England

>>> sort_date(first)
Lester vs Everton - 2:0 on 26/2/2016 in England
Barcelona vs Everton - 2:0 on 26/2/2016 in Spain
Dynamo vs Everton - 2:4 on 26/2/2016 in Ukraine
Lester vs Everton - 2:0 on 26/2/2016 in England
Barcelona vs Everton - 2:0 on 26/2/2016 in Spain
Dynamo vs Everton - 2:4 on 26/2/2016 in Ukraine
Lester vs Everton - 2:0 on 26/2/2016 in England
Barcelona vs Everton - 2:0 on 26/2/2016 in Spain
Dynamo vs Everton - 2:4 on 26/2/2016 in Ukraine
MU vs Everton - 3:0 on 27/2/2016 in England
Real vs Everton - 2:0 on 27/2/2016 in Spain
Vorskla vs Everton - 2:2 on 27/2/2016 in Ukraine
MU vs Everton - 3:0 on 27/2/2016 in England
Real vs Everton - 2:0 on 27/2/2016 in Spain
Vorskla vs Everton - 2:2 on 27/2/2016 in Ukraine
MU vs Everton - 3:0 on 27/2/2016 in England
Real vs Everton - 2:0 on 27/2/2016 in Spain
Vorskla vs Everton - 2:2 on 27/2/2016 in Ukraine
Chelsea vs Everton - 0:0 on 28/2/2016 in England
Sevilla vs Everton - 2:0 on 28/2/2016 in Spain
Stal vs Everton - 2:6 on 28/2/2016 in Ukraine
Chelsea vs Everton - 0:0 on 28/2/2016 in England
Sevilla vs Everton - 2:0 on 28/2/2016 in Spain
Stal vs Everton - 2:6 on 28/2/2016 in Ukraine
Chelsea vs Everton - 0:0 on 28/2/2016 in England
Sevilla vs Everton - 2:0 on 28/2/2016 in Spain
Stal vs Everton - 2:6 on 28/2/2016 in Ukraine
Arsenal vs Everton - 1:0 on 29/2/2016 in England
Eibar vs Everton - 2:1 on 29/2/2016 in Spain
Dnipro vs Everton - 2:7 on 29/2/2016 in Ukraine
Arsenal vs Everton - 1:0 on 29/2/2016 in England
Eibar vs Everton - 2:1 on 29/2/2016 in Spain
Dnipro vs Everton - 2:7 on 29/2/2016 in Ukraine
Arsenal vs Everton - 1:0 on 29/2/2016 in England
Eibar vs Everton - 2:1 on 29/2/2016 in Spain
Dnipro vs Everton - 2:7 on 29/2/2016 in Ukraine


"""

if __name__ == "__main__":
    import doctest
    doctest.testmod()
