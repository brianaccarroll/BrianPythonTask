year = int(input("Please input a year: "))
# Logical error - A year is a leap year if it can be divided by 4.
if year % 4 != 0:
    print(f"{year} is a leap year")
else:
    print(f"{year} is not a leap year")
