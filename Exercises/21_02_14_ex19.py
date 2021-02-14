# Defines the function that print a text containing the two input numbers
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Prints line with first variable
    print(f"You have {cheese_count} cheeses!")
    # Prints line with second variable
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    # Prints string
    print("Man that's enough for a party!")
    # Prints string
    print("Get a blanket.\n")

# Prints string
print("We can just give the function numbers directly:")
# Calls the function with numbers as parameters
cheese_and_crackers(20, 30)

# Prints string
print("OR, we can use variables from our script:")
# Assigning numbers to variables
amount_of_cheese = 10
# Assigning numbers to variables
amount_of_crackers = 50
# Calling the function with the assigned variables
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

# Prints string
print("We can even do math inside too:")
# Calling function AFTER doing math
cheese_and_crackers(10 + 20, 5 + 6)


# Prints string
print("And we can combine the two, variables and math:")
# Calling function AFTER doing math with initialized variables
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
