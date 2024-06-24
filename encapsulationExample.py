class EncapsulationExample:
    def __init__(self, value):
        # Protected attribute
        self._protected_value = value
        
        # Private attribute
        self.__private_value = value

    # Public method to get the protected value
    def get_protected_value(self):
        return self._protected_value

    # Public method to set the protected value
    def set_protected_value(self, value):
        self._protected_value = value

    # Public method to get the private value
    def get_private_value(self):
        return self.__private_value

    # Public method to set the private value
    def set_private_value(self, value):
        self.__private_value = value

    # Protected method
    def _protected_method(self):
        print("This is a protected method.")

    # Private method
    def __private_method(self):
        print("This is a private method.")
    
    # Public method to demonstrate accessing private method
    def access_private_method(self):
        self.__private_method()


# Creating an object of EncapsulationExample class
obj = EncapsulationExample(34)

# Accessing and modifying the protected attribute
print("Protected value (initial):", obj.get_protected_value())
obj.set_protected_value(56)
print("Protected value (modified):", obj.get_protected_value())

# Accessing and modifying the private attribute
print("Private value (initial):", obj.get_private_value())
obj.set_private_value(78)
print("Private value (modified):", obj.get_private_value())

# Accessing the protected method
obj._protected_method()

# Accessing the private method through a public method
obj.access_private_method()
