# Initialisation
num = int(input("Please enter a number: "))
total = 0
num_of_inputs = 0
# Enter a number then add to the total and increment the number of inputs until -1 is entered
while num != -1:
    total += num
    num_of_inputs += 1
    num = int(input("Please enter a number: "))

# Calculate and display the average. If the number of inputs is 0 no number is entered except -1.
if num_of_inputs != 0:
    average = total/num_of_inputs
    print(f"The average of the numbers that are entered is {average}.")
else:
    print("No number except -1 is entered.")

