#! /usr/bin/env python3

import pickle

class Api():
    def __init__(self):
        self.team = None
    
    def _initialise(self, name, force=False):
        if self.team is not None:
            msg = "There is already a team present. "
            if not force:
                print(msg + "Made no changes.")
                return self.team
            else:
                print(msg + "Using the Force - replacing team.")
        from team import Team
        self.team = Team(name)
        return self.team
    
    def load(self, name ='team', save=True):
        filename = '{}.pickle'.format(name)
        if save and self.team is not None:
            self.save()
        try:
            with open(filename, 'rb') as stored:
                self.team = pickle.load(stored)
        except IOError:
            print('No save file found. Creating new team "{}"'.format(name))
            self._initialise(name, force=True)
        return self.team
    
    def save(self, team=None):
        if team is None:
            team = self.team
        filename = '{}.pickle'.format(team.name)
        with open(filename, 'wb') as storage:
            # Pickle the 'team' dictionary using the highest protocol available.
            pickle.dump(team, storage, pickle.HIGHEST_PROTOCOL)
    
    def __del__(self):
        self.save()
