class Car:
    """A simple attempt to represent a car."""

    def __init__(self, manufacturer, model, year):
        self.manufacturer = manufacturer
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.manufacturer} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")


class Battery:
    """A simple attempt to model a battery for an electric car."""

    def __init__(self, battery_size=75):
        self.battery_size = battery_size

    def describe_battery(self):
        print(f"This car has a {self.battery_size}-kWh battery.")

    def get_range(self):
        """Print a statement about the range this battery provides."""
        if self.battery_size == 75:
            car_range = 260
        elif self.battery_size == 100:
            car_range = 315
        else:
            car_range = 300

        print(f"This car can go about {car_range} miles on a full charge.")

    def upgrade_battery(self):
        """Check the battery size and set the capacity to 100 if it isn't already."""
        if self.battery_size != 100:
            self.battery_size = 100
            print("Upgraded the battery to 100 kWh.")
        else:
            print("The battery is already upgraded.")


class ElectricCar(Car):
    """Represent aspects of a car, specific to electric vehicles."""

    def __init__(self, manufacturer, model, year):
        super().__init__(manufacturer, model, year)
        self.battery = Battery()


# Create an electric car, check range, upgrade battery, and check range again
my_tesla = ElectricCar("tesla", "model s", 2024)
print(my_tesla.get_descriptive_name())

my_tesla.battery.describe_battery()
my_tesla.battery.get_range()

print("\nUpgrading battery...")
my_tesla.battery.upgrade_battery()
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()