class Person(object):
    def __init__(self, hp=100, name='Tommy'):
        self.hp = hp
        self.name = name
        self.alive = True

    def add_health(self, hp):
        self.hp += hp

    def add_damage(self, hp):
        self.hp -= hp
        if self.hp <= 0:
            self.hp = 0
            self.alive = False

    def get_health(self):
        return self.hp

    def is_alive(self):
        return self.alive


class Worm(Person):
    pass