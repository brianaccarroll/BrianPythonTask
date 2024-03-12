# Use replace() function to replace ! in a sentence
# Print the sentence in upper word
# Reprint the same sentence in the reversed order
manip_string = "The!quick!brown!fox!jump!over!the!lazy!dog."
manip_string = manip_string.replace("!", " ")
print(manip_string)
manip_string = manip_string.upper()
print(manip_string)
reverse_string = manip_string[::-1]
print(reverse_string)



