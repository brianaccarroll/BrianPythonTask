# This example program is meant to demonstrate errors.

print "Welcome to the error program" # Syntax error - the print statement is missing parentheses
    print "\n" # Compilation error - incorrect space indentation, needs to be in line with the last print statement. Syntax error - the print statement is missing parentheses

    # Variables declaring the user's age, casting the str to an int, and printing the result
    age_Str == "24 years old" # The line is unnecessarily indented and syntax error that it uses "==" to assign variable instead of "="
    age = int(age_Str) # The line is unnecessarily indented and cannot case age_Str to integer as it contains string that cannot be casted to integer
    print("I'm" + age + "years old.") # The line is unnecessarily indented. Syntax error; message does not have appropriate spacing requiring: + " " + and Runtime error; 'age' needs to be cast to a str()

    # Variables declaring additional years and printing the total years of age
    years_from_now = "3" # The line is unnecessarily indented.
    total_years = age + years_from_now # The line is unnecessarily indented. Runtime error; 'years_from_now' needs to be cast to an integer

print "The total number of years:" + "answer_years" # The print statement is missing parentheses and message is not correct.

# Variable to calculate the total amount of months from the total amount of years and printing the result
total_months = total * 12 # Referring a variable which is not declared. Can be simply changed to refer to total_years
print "In 3 years and 6 months, I'll be " + total_months + " months old" # The print statement is missing parentheses

#HINT, 330 months is the correct answer

