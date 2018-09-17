#! /usr/bin/env python3

class Team:
    def __init__(self, name='team'):
        self.name = name
        self.people = dict()
        self.meetings = dict()
    
    def add_person(self, short):
        new = Person(short)
        self.people[short] = new
        return new
    
    def get_emails(self):
        emails = list()
        for person in self.people.values():
            emails.append(person.get_email())
        return emails
    
    def list_incomplete_persons(self):
        for person in self.people.values():
            if not person.is_complete():
                print(person.summary())
    
    def list_members(self):
        for perspn in self.people.values():
            print('{}: {}, {}'.format(person.short,
                                      person.get_nickname(),
                                      person.active)
                  )
    
    def add_meeting(self, name, agg=False):
        if agg:
            new = CompoundMeeting(name)
        else:
            new = Meeting(name)
        self.meetings[name] = new
        return new

class Person:
    mail_domain = 'elsevier.com'
    
    def __init__(self, short):
        self.short = short
        self.first = None
        self.last = None
        self.nick = None
        self.email = None
        self._location = None
        self._note = ''
        self.attendance = 1
        self.active = True
        self.meetings = set()
    
    def is_complete(self):
        if None in (self.first, self.last,
                    self.email, self._location):
            return False
        return True
    
    def summary(self, note_activity=False):
        data = {'short name': self.short,
                'first name': self.first,
                'last name': self.last,
                'nickname': self.get_nickname(),
                'e-mail': self.get_email(),
                'location': self._location,
                'seat required': self.seat,
                'note': self._note,
                'attendance': self.attendance,
                'meetings': self.meetings,
                }
        if note_activity:
            data['active'] = self.active
        return data
    
    def add_note(self, note):
        if self._note:
            self._note = '{} | {}'.format(self._note, note)
        else:
            self._note = note
    
    def replace_note(self, note):
        self._note = note
    
    def _add_meeting(self, meeting):
        self.meetings.add(meeting)
    
    def get_full_name(self):
        return '{} {}'.format(self.firstname, self.lastname)
    
    def get_nickname(self):
        if self.nick is not None:
            return self.nick
        return self.first
    
    def get_email(self):
        return '{}@{}'.format(self.email, self.mail_domain)

class BaseMeeting:
    frequencies = {1: 'daily',
                   7: 'weekly',
                   14: 'bi-weekly',
                   0: 'as needed'}
    def __init__(self, name):
        self.name = name
        self.length = 1
        self.frequency = None
        self.location = 'Amsterdam'

class Meeting(BaseMeeting):
    def __init__(self, name):
        super()
        self.attendants = set()
    
    def add_person(self, person):
        self.attendants.add(person)
        person._add_meeting(self)

class CompoundMeeting(BaseMeeting):
    def __init__(self, name):
        super()
        self.meetings = set()
    
    def add_meeting(self, meeting):
        self.meetings.add(meeting)
