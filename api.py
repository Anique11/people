#! /usr/bin/env python3

import pickle

class Api():
    def __init__(self):
        self.team = None
    
    def initialise(self, force=False):
        if self.team is not None:
            msg = "There is already a team present. "
            if not force:
                print(msg + "Made no changes.")
                return self.team
            else:
                print(msg + "Using the Force - replacing team.")
        from team import Team
        self.team = Team()
        return self.team
    
    def load(self):
        with open('team.pickle', 'rb') as stored:
            self.team = pickle.load(stored)
        return self.team
    
    def save(self, team=None):
        if team is None:
            team = self.team
        with open('team.pickle', 'wb') as storage:
            # Pickle the 'team' dictionary using the highest protocol available.
            pickle.dump(team, storage, pickle.HIGHEST_PROTOCOL)
    
    def __del__(self):
        self.save()
