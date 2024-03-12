age = int(input("Please input your age: "))
if age > 100:
    print("Sorry, you are dead.")
elif age >= 65:
    print("Enjoy your retirement!")
elif age >= 40:
    print("You're over the hill")
elif 0 <= age < 13:
    print("You qualify for the kiddie discount")
elif age == 21:
    print("Congrats on your 21st")
else:
    print("Age is but a number")