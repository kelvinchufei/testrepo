# define the Vehicle class
"""This module demonstrates how the Python class works"""


class Vehicle:
    """This class defines the Vehicle class"""
    name = ""
    kind = "car"
    color = ""
    value = 100.00

    def description(self):
        """This is the print self description function"""
        desc_str = "%s is a %s %s worth $%.2f." % (self.name, self.color, self.kind, self.value)
        return desc_str

    def crash(self):
        """The crash event changes the Vehicle name and value"""
        self.color = "crashed " + self.color
        self.value = 0.0


# your code goes here

CAR_1 = Vehicle()
CAR_1.name = "Ford Mustang GT"
CAR_1.kind = "convertible"
CAR_1.color = "red"
CAR_1.value = 60000.00

CAR_2 = Vehicle()
CAR_2.name = "Jeep"
CAR_2.kind = "SUV"
CAR_2.color = "black"
CAR_2.value = 30000.00

# test code
print(CAR_1.description())
print(CAR_2.description())
print("A car crash happened.")
CAR_2.crash()
print(CAR_2.description())
