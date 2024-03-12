# Ask user to input the number of students to be registered
num_of_students = int(input("How many students are registering? "))
# Open the file to be written to
ofile = open('reg_form.txt', 'w')
# For each student, enter the student ID and
for i in range(num_of_students):
    # Ask the user for their student ID. When they enter it, it is stored as a string variable.
    student_id = input("Enter the student ID: ")
    # Use the write method to write the contents 'student_id' variable to the output file followed by a dotted line.
    ofile.write(student_id + " ......................" + "\n")

# Close the file at the end.
ofile.close()
