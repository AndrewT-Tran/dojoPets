from dojoPets import pet
class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food, pet):
        self.first_name = first_name
        self.last_name = last_name
        self.treats = treats
        self.pet_food = pet_food
        self.pet = pet

    def walk(self):
        self.pet.play()
        return self
    # walk() - walks the ninja's pet invoking the pet play() method

    def feed(self):
        print("Feeding " + self.pet.name + " " + self.pet_food)
        self.pet.eat()
        return self
    # feed() - feeds the ninja's pet invoking the pet eat() method

    def bathe(self):
        self.pet.noise()
        return self
    #  bathe() - cleans the ninja's pet invoking the pet noise() method
Ninja1 = Ninja("Andrew", "Tran", "Candy", "Apples", "Pikachu")
Ninja1.pet = pet("Pikachu", "Electric", "Apples")
Ninja1.pet.sound = "~ Pika ~ Pika ~"
Ninja1.walk().feed().bathe()
