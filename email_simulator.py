"""
This program email simulator used OOP The code defines classes 
for Email and EmailSimulator, allowing users to manage and interact with
a simulated email inbox through functions like reading emails, viewing 
unread emails, and quitting the application.
"""

import os # imports libraries for clearscreen function
    

class Email:
    """
    Represents an email object.

    Attributes:
    - email_address
    - subject_line
    - email_content

    """


    def __init__(self, email_address, subject_line, email_content):
        """
        This function initializes an email object with specified 
        email address, subject line, email content, and sets a flag
        indicating whether the email has been read.
        
        Parameters:
        - email_address: is used to store the email address of 
          the recipient to whom the email will be sent. 
        - subject_line:  is used to store the subject line of the email.
          It is a string that represents the subject or title of email.
        - email_content: is used to store the content of the email message
          that will be sent. This could include the main body of the email,
        """

        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False

    def mark_as_read(self):
        """
        This function sets the `has_been_read`
        attribute to True. Mark the email as read
        """

        self.has_been_read = True


class EmailSimulator:
    """
    Represents an email simulator that allows users to manage and
    interact with simulated email box.
    """

    
    def __init__(self):
        """
        This constructor initializes an empty list called "inbox".
        """

        self.inbox = []
        
    def populate_inbox(self):
        # Creating sample email objects and adding them to the inbox

        sample_emails = [
            Email("hyperion@hyperiondev.com", "Welcome to HyperionDev!",
                   ("Congratulations on taking the first step into a "
                    "transformative journey.")),
            Email("cogrammar@noreply.com", "Great work on the bootcamp!",
                   "You are blazing the trail in your skills bootcamp journey"),
            Email("noreply@yahoo.com", "Your excellent marks!",
                   "You've done a commendable job in developing your task")
        ]
        self.inbox.extend(sample_emails)

    def count_unread_emails(self):
        """
        This function counts the number of unread emails in a given
        inbox.

        :return: This method returns the number of unread emails in the 
        inbox of the object calling the method.
        """

        count = 0
        for email in self.inbox:
            if not email.has_been_read:
                count += 1
        return count

    def list_emails(self, status=None):
        """
        This function prints the subject lines of emails in the inbox 
        based on their read status.
        
        :param status: is used to filter the emails based on their 
        read status. If `status` is set to "Unread", only unread 
        emails will be displayed. 
        """

        print("Inbox\n")
        for index, email in enumerate(self.inbox, 1):
            if status is None or \
                (status == "Unread" and not email.has_been_read) or \
                (status == "Read" and email.has_been_read):
                status_str = "Unread" if not email.has_been_read else "Read"
                print(f"{index} {status_str}: {email.subject_line}")

    def read_email(self, index):
        """
        This function reads and displays an email from an inbox based
        on the provided index.
        
        :param index: is used to specify the position of the email in
        the inbox that you want to read. 
        """


        clearscr()
        title = " EMAIL SIMULATOR "
        print("="*(40-(len(title)//2)), title, "="*(40-(len(title)//2)))
        print("\n")
        if 0 <= (index - 1) < len(self.inbox):
            email = self.inbox[index - 1]
            print(f"\nFrom: {email.email_address}")
            print(f"Subject: {email.subject_line}")
            print("\nContent:")
            print(f" {email.email_content}")
            email.mark_as_read()
            print(f"\n\nEmail marked as read.\n")
        else:
            print("\nOoops. Incorrect input..")
            

def clearscr():
    """This function clears the terminal screen."""

    os.system("cls||clear")


def get_input(prompt):
    """
    This takes a prompt as input and repeatedly prompts the user for
    an integer input until a valid integer is entered.
    
    :param prompt: is used to guide the user on what type of input 
     is expected from them
    :return: returns the user input as an integer if the input is 
    successfully converted to an integer. If the input cannot be 
    converted to an integer (i.e., if a `ValueError` is raised), 
    the function will print an error message and prompt the user 
    to enter the input again.
    """
    
    while True:
        try:
            user_input = int(input(prompt))
            return user_input
        except ValueError:
            print("\nOoops. Incorrect input..")
            

def main():
    """
    The main function simulates an email application where users can
    read emails, view unread emails, and quit the application.
    """

    # Creates an instance of the `EmailSimulator` class, 
    # which represents a simulation of an email application.

    email_simulator = EmailSimulator()
    email_simulator.populate_inbox()

    while True:
        clearscr()
        title = " EMAIL SIMULATOR "
        print("="*(40-(len(title)//2)), title, "="*(40-(len(title)//2)))
        print("\n")
        menu = '''\nWould you like to:
        
        1. Read an email
        2. View unread emails
        3. Quit application
        '''
        print(menu)
        user_choice = get_input("\n\nEnter your choice: ")

        if user_choice == 1:
            clearscr()
            title = " EMAIL SIMULATOR "
            print("="*(40-(len(title)//2)), title, "="*(40-(len(title)//2)))
            print("\n")
            email_simulator.list_emails()
            index = get_input("\nEnter the index of the email you want to read: ")
            email_simulator.read_email(index)
            input("\n\nPlease press Enter to back to menu:")

        elif user_choice == 2:
            clearscr()
            title = " EMAIL SIMULATOR "
            print("="*(40-(len(title)//2)), title, "="*(40-(len(title)//2)))
            print("\n")
            unread_count = email_simulator.count_unread_emails()
            print(f"You have {unread_count} unread emails")
            email_simulator.list_emails(status = "Unread")
            input("\n\nPlease press Enter to back to menu:")

        elif user_choice == 3:
            print("\nThank you for using the application...")
            break

        else:
            clearscr()
            print("\nOoops. Incorrect input.")
            input("\n\nPlease press Enter to back to menu:")

if __name__ == "__main__":
    main()