# This example program is meant to demonstrate errors.

# There are some errors in this program. Run the program, look at the error messages, and find and fix the errors.
# Syntax error - the string variable is missing ""
animal = "Lion"
animal_type = "cub"
number_of_teeth = 16

# Syntax error - f string is missing f and
# logical error that the message refers to the wrong variable to what it meant to say
full_spec = f"This is a {animal}. It is a {animal_type} and it has {number_of_teeth} teeth"
# Syntax error - the print statement is missing parentheses
print(full_spec)
