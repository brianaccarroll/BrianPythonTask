# Open the file
f = open('./10-018 IO Operations - Input/Task file/DOB.txt', 'r+')
names = []
dobs = []

# Loop through each line of the file and split the line. Join the first two words as the name and append
# the list of the names. Join the rest words into date of birth and append to the date of birth list.
for line in f:
    words = line.split()
    names.append((" ".join(words[0:2])))
    dobs.append(" ".join(words[2:]))
f.close()
# Print out names and date of birth into two separate sections
print("Name")
for n in names:
    print(n)
print("\nBirthdate")
for d in dobs:
    print(d)

