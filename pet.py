class Pet:
    def __init__(self, name, type, tricks):
        self.name=name
        self.type=type
        self.tricks=tricks
        self.energy = 50
        self.health = 50
    def sleep(self):
        self.energy+=25
    def eat(self):
        self.energy+=5
        self.health+=10
    def play(self):
        self.health+=5
        self.energy-=10
    def noise(self):
        print("heavy breathing...")
class Dog(Pet):
    def noise(self):
        print("barking...")
