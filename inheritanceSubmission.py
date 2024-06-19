# Define the parent class Animal
class Animal:
    name = ""
    species = ""
    age = 0

# Define a class Dog that inherits from Animal
class Dog(Animal):
    # Additional attributes specific to Dog
    breed = ""
    is_trained  = False


# Define a class Bird that inherits from Animal
class Bird(Animal):
    # Additional attributes specific to Bird
    wing_span = 0
    can_fly = True

    
