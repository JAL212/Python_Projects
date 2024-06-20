# Define the parent class Animal
class Animal:
    name = ""
    species = ""
    age = 0

    def information(self):
        msg = "\nName: {}\nSpecies: {}\nAge: {}".format(self.name, self.species, self.age)
        return msg

    #Method that allows for polymorphism
    def get_info(self):
        return self.information()

# Define a class Dog that inherits from Animal
class Dog(Animal):
    # Additional attributes specific to Dog
    name = "Magpie"
    species = "Dog"
    age = 10
    breed = "Shih Tzu"
    is_trained  = True

    def dog_info(self):
        msg = "Breed: {}\nIs Trained: {}".format(self.breed, self.is_trained)
        return msg
    
    #Polymorphism using same method name to get different info
    def get_info(self):
        return self.information() + "\n" + self.dog_info()

# Define a class Bird that inherits from Animal
class Bird(Animal):
    # Additional attributes specific to Bird
    name = "Tweedy"
    species = "Bird"
    age = 8
    wing_span = 14
    can_fly = True

    def bird_info(self):
        msg = "Wing Span(inches): {}\nCan Fly: {}".format(self.wing_span, self.can_fly)
        return msg

    #Polymorphism using same method name to get different info
    def get_info(self):
        return self.information() + "\n" + self.bird_info()

if __name__ == "__main__":
    dog = Dog()
    print(dog.get_info())

    bird = Bird()
    print(bird.get_info())


    
