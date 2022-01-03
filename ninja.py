import pet
class Ninja:
    def __init__(self, first_name, last_name, treats, pet_food,ninjas_pet):
        self.first_name=first_name
        self.last_name=last_name
        self.treats=treats
        self.pet_food=pet_food
        if ninjas_pet[1] == "Dog":
            self.animal= pet.Dog(ninjas_pet[0],ninjas_pet[1],ninjas_pet[2])
        else:
            self.animal = pet.Pet(ninjas_pet[0],ninjas_pet[1],ninjas_pet[2])
    def walk(self):
        self.animal.play()
        return self
    def feed(self):
        self.animal.eat()
        return self
    def bathe(self):
        self.animal.noise()
        return self
jordan = Ninja("Jordan", "French", "milk bones", "raw chicken", ["Jax", "Dragon","flying"])
jordan.feed().walk().bathe()
# print(jordan.animal.health)
zed = Ninja("Zed", "Legend", "bones", "poro king puppy chow", ["Talon", "Dog", "rollover"])
zed.feed().walk().bathe()
