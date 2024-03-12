# --- OOP Email Simulator --- #

# --- Email Class --- #
# Create the class, constructor and methods to create a new Email object.
class Email:
    # Declare the class variable, with default value, for emails.
    has_been_read = False

    def __init__(self, email_address, subject_line, email_content):
        """
        This is the constructor for the class Email. It takes 3 arguments
        :param email_address: the email address of the sender
        :param subject_line: the subject line of the email
        :param email_content: the content of the email
        """
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content

    def mark_as_read(self):
        """
        Mark the email to read
        """
        self.has_been_read = True
        print(f"Email from {self.email_address} is marked as read {self.has_been_read}")

    # Get method to get the email subject line
    def get_email_subject(self):
        return self.subject_line

    # Get method to get the email address
    def get_email_address(self):
        return self.email_address

    # Get method to get the email content
    def get_email_content(self):
        return self.email_content

    def __str__(self):
        """
        This special method is called by Python when using the 'print' command
        :return: string
        """
        return self.email_address + ' ' + self.subject_line + ' ' + self.email_content


# --- Lists --- #
# Initialise an empty list to store the email objects.
inbox = []
# --- Functions --- #
# Build out the required functions for your program.


def populate_inbox():
    # Create 3 sample emails and add it to the Inbox list.
    email_1 = Email("Brian@hotmail.com", "Learning python", "Here are some notes I take while learning python language.")
    email_2 = Email("Lizzy@hotmail.com", "Holiday plan", "There are a few destinations I am thinking we can plan "
                                                         "this year for our holiday.")
    email_3 = Email("Colin@gmail.com", "Family photos", "I took some nice photos for the family meal out.")
    inbox.append(email_1)
    inbox.append(email_2)
    inbox.append(email_3)


def list_emails():
    """
    A function which prints the email’s subject_line, along with a corresponding number.
    :return:
    """
    for count, e in enumerate(inbox):
        print(str(count) + " " + e.get_email_subject())


def read_email(index):
    """
    A function which displays a selected email.
    Once displayed, call the class method to set its 'has_been_read' variable to True.
    :param index: The index of the email in the inbox
    :return:
    """
    email_to_read = inbox[index]
    print(f"From: {email_to_read.get_email_address()}")
    print(f"Subject - {email_to_read.get_email_subject()}")
    print(f"Content - {email_to_read.get_email_content()}")
    inbox[index].mark_as_read()

# --- Email Program --- #


# Call the function to populate the Inbox for further use in your program.
populate_inbox()
list_emails()

# Fill in the logic for the various menu operations.
menu = True

while True:
    user_choice = int(input('''\nWould you like to:
    1. Read an email
    2. View unread emails
    3. Quit application

    Enter selection: '''))

    # Call read an email function
    if user_choice == 1:
        read_index = int(input("Please input the index of the email to read: "))
        read_email(read_index)
    elif user_choice == 2:
        # View unread emails in the inbox
        for email in inbox:
            if email.has_been_read is False:
                print(f"Unread email subject - {email.subject_line}")
    elif user_choice == 3:
        # Print goodbye and quit the application
        print('Goodbye!!!')
        exit()
    else:
        print("Oops - incorrect input.")
