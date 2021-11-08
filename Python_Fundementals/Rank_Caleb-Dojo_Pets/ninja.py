class Ninja:
    def __init__(self, first_name, last_name, pet=None, pet_food=None, treats=None):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = pet
        self.pet_food = pet_food
        self.treats = treats

    def displayInfo(self):
        print(f"Name: {self.first_name} {self.last_name}")
        if self.pet == None:
            print(f"Pet: {self.pet}")
        else:
            print(f"Pet: --------")
            self.pet.displayInfo()
            print(f"-------------")
        print(f"Pet Food: {self.pet_food}")
        print(f"Treats: {self.treats}")
        return self

    def walk(self):
        if self.pet != None:
            self.pet.play()
        else:
            print("This Ninja has no pet. :'(")
        return self

    def feed(self):
        if self.pet != None:
            self.pet.eat()
        else:
            print("This Ninja has no pet. :'(")
        return self

    def bathe(self):
        if self.pet != None:
            self.pet.noise()
        else:
            print("This Ninja has no pet. :'(")
        return self
