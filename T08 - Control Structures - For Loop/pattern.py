# Loop from 1 to 10. If i is more than 5 print the pattern with number of 5 - the reminder of i divide by 5.
# else print the pattern with number of i
for i in range(1, 10):
    if i > 5:
        r = i % 5
        print("*" * (5-r))
    else:
        print("*" * i)
