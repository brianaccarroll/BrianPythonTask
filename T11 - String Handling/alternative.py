# Take a string input
s = input("Please input a string: ")
# Split the string into words
words = s.split()
string_builder = []
# For each word in the string make each alternate character upper case
# and each other alternate character a lower case. Then append each word to a list of strings.
for w in words:
    w_alternative = [c.upper() if not i % 2 else c.lower()
                     for i, c in enumerate(w)]
    w_alternative = "".join(w_alternative)
    string_builder.append(w_alternative)

# Join the words and print out the string
print(" ".join(string_builder))

# For the same string make each alternative word upper case and lower case and print out
w_alternative = [w.lower() if not i % 2 else w.upper() for i, w in enumerate(words)]
print(" ".join(w_alternative))
