class pet:
    def __init__(self, name, breed, tricks):
        self.name = name
        self.breed = breed
        self.tricks = tricks
        self.health = 100
        self.energy = 100

    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5
        return self

    def noise(self):
        print(self.sound)
        return self

class pet2(pet):
    pass
