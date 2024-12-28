# Create a class representing anything you like (a Smartphone, Book, or even a Superhero!).
# Add attributes and methods to bring the class to life!
# Use constructors to initialize each object with unique values.
# Add an inheritance layer to explore polymorphism or encapsulation.


class Smartphone:
    def __init__(self, brand, model, storage, battery_capacity):
        self.brand = brand
        self.model = model
        self.storage = storage
        self.__battery_capacity = battery_capacity  # Encapsulation: Private attribute

    def get_battery_capacity(self):
        """Access the private battery capacity attribute."""
        return f"{self.__battery_capacity} mAh"

    def make_call(self, contact):
        """Simulate making a call."""
        print(f"Calling {contact} from {self.model}...")

    def send_message(self, contact, message):
        """Simulate sending a message."""
        print(f"Sending message to {contact}: {message}")

    def display_info(self):
        """Display smartphone details."""
        return f"Brand: {self.brand}, Model: {self.model}, Storage: {self.storage}GB, Battery: {self.get_battery_capacity()}"

# Base Smartphone Example
basic_phone = Smartphone("Samsung", "Galaxy S22", 128, 3700)
print(basic_phone.display_info())
basic_phone.make_call("Alice")
basic_phone.send_message("Bob", "Hey, what's up?")
print()

        