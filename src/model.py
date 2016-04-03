__author__ = 'Kryvonis'


class Model(object):
    """
    Object means gameResult
    """

    class __Model:
        def __init__(self):
            """
            Initialize standart data
            :return: null
            """
            self.England = []
            self.add_result('Lester', 'Everton', '2:0', '03.18.16')
            self.add_result('MU', 'Everton', '3:0', '03.16.16')
            self.add_result('Chelsea', 'Arsenal', '2:1', '03.18.16')
            self.add_result('MU', 'Chelsea', '0:0', '03.20.16')
            self.add_result('Arsenal', 'Lester', '1:1', '03.22.16')
            self.add_result('Arsenal', 'Chelsea', '3:0', '03.25.16')

        def add_result(self, first_T, second_T, result, date):
            """
            Add one gameResult in England league
            :param first_T: first team name
            :param second_T: second team name
            :param result: game result
            :param date: date of game
            :return: null
            """
            self.England.append((first_T, second_T, result, date))

        def get_by_team(self, team):
            """
            Find all game width one team
            :param team: name of team
            :return: result array of all games
            """
            results = []
            for game in self.England:
                if team in game:
                    results.append(game)
            return results

        def get_all_games(self):
            """
            Get all England league games
            :return: array of all games
            """
            return self.England

        def get_team_items(self, match):
            return match[0], match[1], match[2], match[3]

    instance = None

    def __new__(cls):
        if not Model.instance:
            Model.instance = Model.__Model()
        return Model.instance
