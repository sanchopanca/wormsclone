from wormsclone.utils import LoopList


class Team(object):
    def __init__(self, person_iterable):
        self.persons = LoopList(person_iterable)

    def get_team_health_sum(self):
        s = 0
        for person in self.persons:
            s += person.get_health()
        return s

    def get_next_person(self):
        if self.get_team_health_sum() == 0:
            return None
        person = self.persons.get_next()
        while not person.is_alive():
            person = self.persons.get_next()
        return person