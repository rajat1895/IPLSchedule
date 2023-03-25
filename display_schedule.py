class DisplaySchedule:

    # def __init__(self, mlist):
    #     self.matchlist = mlist

    def display_match_schedule(self, mlist):

        match_num = 0
        for match in mlist:

            match_num = match_num+1
            print("Match " + str(match_num) + " " + match.Home_Team + " Vs " + match.Away_Team + " at " + match.Venue)


