# This is a sample Python script.
from data import match_data
from match_model import Match
from display_schedule import DisplaySchedule
from APICall import get_data
from process_json_data import ProcessJsonData

api_url = "https://api.cricapi.com/v1/currentMatches?apikey=5514f25d-4079-4648-89f3-5f5a4d601bf5&offset=0"

json_data = get_data(api_url)

ProcessJsonData(json_data)

# match_database = []

# for match in match_data:
#     print(match["Home_Team"])
#     match_home_team = match["Home_Team"]
#     match_away_team = match["Away_Team"]
#     match_venue = match["Venue"]
#     new_match = Match(match_home_team, match_away_team, match_venue)
#     match_database.append(new_match)
# DisplaySchedule.display_match_schedule(0, match_database)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

