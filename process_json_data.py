from match_model import Match
from display_schedule import DisplaySchedule


class ProcessJsonData:

    def __init__(self, j_data):
        self.json_data = j_data
        self.process_data()

    def process_data(self):

        match_database = []

        list_matches = self.json_data['data']
        for matches in list_matches:

            match_home_team = matches['teams'][0]
            match_away_team = matches['teams'][1]
            match_venue = matches["venue"]
            new_match = Match(match_home_team, match_away_team, match_venue)
            match_database.append(new_match)

        DisplaySchedule.display_match_schedule(0, match_database)



