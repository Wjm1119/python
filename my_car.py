from Car import Car
from Electric_Car import ElectricCar


my_new_car = Car('audi', 'a4', 2016)
print(my_new_car.get_descriptive())
my_new_car.update_odometer(23)
my_new_car.update_odometer(22)
my_new_car.read_odometer()
my_used_car = Car('subaru', 'outback', 2013)
print(my_used_car.get_descriptive())

my_used_car.update_odometer(23500)
my_used_car.read_odometer()

my_used_car.increment_odometer(100)
my_used_car.read_odometer()
my_tesla = ElectricCar('tesla', 'model s', 2016)
print(my_tesla.get_descriptive())
my_tesla.battery.describe_battery()
my_tesla.battery.get_range()