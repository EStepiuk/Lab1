__author__ = 'Kryvonis'


class MatchResult:
    """
    Object means matchrResult
    """

    def __init__(self, first_T, second_T, result, date):
        """
        main constructor
        :param first_T:
        :param second_T:
        :param result:
        :param date:
        :return:
        """
        self.date = date
        self.result = result
        self.first_T = first_T
        self.second_T = second_T

    def get_date(self):
        """
        :return self.date:
        """
        return self.date

    def get_result(self, ):
        """
        :return self.resutl:
        """
        return self.result

    def get_first(self):
        """
        :return self.first_team:
        """
        return self.first_T

    def get_second(self):
        """

        :return self.second_team:
        """
        return self.second_T


England = [MatchResult('Lester', 'Everton', '2:0', '03.18.16'),
           MatchResult('MU', 'Everton', '3:0', '03.16.16'),
           MatchResult('Chelsea', 'Arsenal', '2:1', '03.18.16'),
           MatchResult('MU', 'Chelsea', '0:0', '03.20.16'),
           MatchResult('Arsenal', 'Lester', '1:1', '03.22.16'),
           MatchResult('Arsenal', 'Chelsea', '3:0', '03.25.16')]


def get_by_team(team):
    """
    Return list of team what we want to find
    :param team:
    :return result:
    """
    results = []
    for t in England:
        if t.get_first() == team or t.get_second() == team:
            results.append(t)
    return results
