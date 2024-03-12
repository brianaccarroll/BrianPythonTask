# Read time to complete swimming, cycling and running of a participant
swimming = int(input("Please input a participant's time in swimming: "))
cycling = int(input("Please input a participant's time in cycling: "))
running = int(input("Please input a participant's time in running: "))
# Calculate and display the total time a participant spent in triathlon
total = swimming + cycling + running
print(f"Total time the participant spent in completing the triathlon is {total}")
# Check and display the award that a participant will receive based on the total time
if 0 < total <= 100:
    print("A participant receives Provincial Colours Award")
elif 101 <= total <= 105:
    print("A participant receives Provincial Half Colours Award")
elif 106 <= total <= 110:
    print("A participant receives Provincial Scroll Award")
elif total >= 111:
    print("A participant receives no award")
else:
    print("Invalid record")

