# This example program is meant to demonstrate errors.
# Syntax error - the print statement is missing parentheses
print("Welcome to the error program")
# Syntax error - incorrect space indentation, needs to be in line with the last print statement.
# and the print statement is missing parentheses
print("\n")

# Variables declaring the user's age, casting the str to an int, and printing the result
# Syntax error - The line is unnecessarily indented
# and that it uses "==" to assign variable instead of "="
age_Str = "24 years old"
# Syntax error - The line is unnecessarily indented
# Runtime error -  cannot cast age_Str to integer as it contains string that cannot be cast to integer
age = int(age_Str[0:2])
# Syntax error - the line is unnecessarily indented
# and message does not have appropriate spacing requiring: + " " +
# Runtime error - 'age' needs to be cast to a str()
print("I'm " + str(age) + " years old.")

# Variables declaring additional years and printing the total years of age
# Syntax error - The line is unnecessarily indented.
# Runtime error; 'years_from_now' needs to be cast to an integer
years_from_now = "3"
total_years = age + int(years_from_now)

# Syntax error - The print statement is missing parentheses
# Logic error - message is not correct.
print("The total number of years: " + str(total_years))

# Variable to calculate the total amount of months from the total amount of years and printing the result
# Syntax error - Referring to a variable which is not declared. Can be simply changed to refer to total_years
total_months = total_years * 12 + 6
# Syntax error - The print statement is missing parentheses
print("In 3 years and 6 months, I'll be " + str(total_months) + " months old")

