# Runtime error - input str needs to be cast to integer
year = input("Please input a year: ")
# Logical error - A year is a leap year if it can be divided by 4.
if year % 4 != 0:
    # Compilation error - f string missing f
    print("{year} is a leap year")
else:
    # Compilation error - incorrect indentation
print(f"{year} is not a leap year")
