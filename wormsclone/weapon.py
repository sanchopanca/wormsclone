class Weapon(object):
    def __init__(self, name):
        self.name = name


class Artillery(Weapon):
    def __init__(self, name):
        Weapon.__init__(self, name)