# Number of cars
cars = 100
# Number of free seats in a car
space_in_a_car = 4.0
# Number of drivers
drivers = 30
# Number of passengers
passengers = 90
# Remaining cars as a difference
cars_not_driven = cars - drivers
# incorrect formula for the number of cars that are driven
cars_driven = drivers
# Capacity as a product of driven cars with free seats
carpool_capacity = cars_driven * space_in_a_car
# Average number of passangers per car
average_passengers_per_car = passengers / cars_driven


print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car, "in each car.")
