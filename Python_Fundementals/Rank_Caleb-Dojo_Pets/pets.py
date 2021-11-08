class Pet:
    def __init__(self, name, Type, tricks=None):
        self.name = name
        self.type = Type
        self.tricks = tricks
        self.health = 75
        self.energy = 50

    def displayInfo(self):
        print(f"Name: {self.name}")
        print(f"Type: {self.type}")
        print(f"Tricks: {self.tricks}")
        print(f"Health %: {self.health}")
        print(f"Energy %: {self.energy}")

    def sleep(self):
        if self.energy <= 75:
            self.energy += 25
        else:
            self.energy = 100
        return self

    def eat(self):
        if self.energy <= 95:
            self.energy += 5
        else:
            self.energy = 100
        
        if self.health <= 90:
            self.health += 10
        else:
            self.health = 100
        return self

    def play(self):
        if self.health <= 95:
            self.health += 5
        else:
            self.health = 100
        return self

    def noise(self):
        print("sfx: 'Pet's Noise'")
        return self

class Dog(Pet):
    def __init__(self, name, Type, tricks=None):
        super().__init__(name, Type, tricks=tricks)
    
    def noise(self):
        print("Bark!!!")
        return self

class Cat(Pet):
    def __init__(self, name, Type, tricks=None):
        super().__init__(name, Type, tricks=tricks)
    
    def noise(self):
        print("Meow!")
        return self

class Bird(Pet):
    def __init__(self, name, Type, tricks=None):
        super().__init__(name, Type, tricks=tricks)
    
    def noise(self):
        print("Chirp!!!")
        return self