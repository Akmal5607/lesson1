class SuperHero:
    people='people'
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name=name
        self.nickname=nickname
        self.superpower=superpower
        self.health_points=health_points
        self.catchphrase=catchphrase
    def get_name(self):
        return self.name
    def get_health_points(self):
        return self.health_points *2
    def __len__(self):
        return len(self.catchphrase)

    def __str__(self):
        return f'{self.nickname}, {self.superpower}, {self.health_points}'


superhero = SuperHero()
print(superhero)
print(superhero.get_name())
print(superhero.get_health_points())
print(superhero.__len__())


class Other(SuperHero):
    superh = superhero
    superh = 'Bedmen'
def  __init__(self)
    def __init__(self, name, nickname, superpower, health_points, catchphrase):
        self.name = name
        self.nickname = nickname
        self.superpower = superpower
        self.health_points = health_points
        self.catchphrase = catchphrase

    def get_name(self):
        return self.name

    def get_health_points(self):
        return self.health_points * 2

    def __len__(self):
        return len(self.catchphrase)

    def __str__(self):
        return f'{self.nickname}, {self.superpower}, {self.health_points}'
class oti():
    ssgg = 'freek'
    def __init__(self):
        return f'{self.people}, {self.ssgg}, '


















