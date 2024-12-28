# Create a program that includes animals or vehicles with the same action (like move()). 
# However, make each class define move() differently (for example, Car.move() prints 
# "Driving" 🚗, while Plane.move() prints "Flying" ✈️).


class Vehicle:
    def move(self):
        """Base method to be overridden by subclasses."""
        raise NotImplementedError("Subclasses must implement this method!")

class Car(Vehicle):
    def move(self):
        print("Driving 🚗")

class Plane(Vehicle):
    def move(self):
        print("Flying ✈️")

class Boat(Vehicle):
    def move(self):
        print("Sailing 🛥️")

class Bicycle(Vehicle):
    def move(self):
        print("Pedaling 🚴")

class Train(Vehicle):
    def move(self):
        print("Chugging along 🚂")

# Demonstrating Polymorphism
def demonstrate_movement(vehicles):
    for vehicle in vehicles:
        vehicle.move()

# Create instances of each class
car = Car()
plane = Plane()
boat = Boat()
bicycle = Bicycle()
train = Train()

# Add them to a list
vehicles = [car, plane, boat, bicycle, train]

# Call the move method on each
demonstrate_movement(vehicles)
 