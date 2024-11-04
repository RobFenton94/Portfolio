#  Class email.
class Email:
    def __init__(self, email_address, subject_line, email_content):
        """
        Constructor for the Email class.
        """
        self.email_address = email_address
        self.subject_line = subject_line
        self.email_content = email_content
        self.has_been_read = False  # Default value indicating email not read.

    def mark_as_read(self):
        # Method to mark the email as read.
        self.has_been_read = True


class EmailSimulator:
    def __init__(self):
        # Constructor for the EmailSimulator class.
        self.inbox = []  # List to store email objects.

    def populate_inbox(self):
        # Function to populate the inbox with sample emails.
        email1 = Email("john.doe@gmail.com", "Welcome to HyperionDev!", "Your Excellent Marks.")
        email2 = Email("rob.fenton@gmail.com", "Welcome to HyperionDev!", "Your Excellent Marks.")
        email3 = Email("olesya.chernaya@gmail.com", "Welcome to HyperionDev!", "Your Excellent Marks.")
        self.inbox.extend([email1, email2, email3])  # Add sample emails to the inbox.

    def list_emails(self):
        # Function to list all emails in the inbox.
        if not self.inbox:
            print("Your inbox is empty.")
        else:
            print("Your Inbox:")
            for count, email in enumerate(self.inbox):
                print(f"{count} {email.subject_line} (Read)" 
                      if email.has_been_read 
                      else f"{count} {email.subject_line} (Unread)")

    def read_email(self, index):
        # Function to read a selected email.
        if 0 <= index < len(self.inbox):
            email = self.inbox[index]
            print("\n------------------------------------")
            print(f"From: {email.email_address}")
            print(f"Subject: {email.subject_line}")
            print(f"Content: {email.email_content}")
            print("------------------------------------\n")
            email.mark_as_read()
        else:
            print("Invalid email index.")


def main():
    email_simulator = EmailSimulator()
    email_simulator.populate_inbox()  # Populate inbox with sample emails.

    while True:
        # Display options in main menu.
        print("\nMenu:")
        print("1. Read an email")
        print("2. View unread emails")
        print("3. Quit application")
        # Obtain user input.
        choice = input("Enter your choice: ")

        # Check user's choice and take relevant actions.
        if choice == "1":
            # Option 1: Read email.
            email_simulator.list_emails()
            index = int(input("Enter the index of the email you want to read: "))
            email_simulator.read_email(index)  # Read the selected email.
        elif choice == "2":
            # Option 2: View unread emails.
            unread_emails = [email for email in email_simulator.inbox
                             if not email.has_been_read]
            if unread_emails:
                # Print unread emails (if any).
                print("\nUnread Emails:")
                for email in unread_emails:
                    print(email.subject_line)
            else:
                # Inform user of no unread emails.
                print("\nNo unread emails.")
        elif choice == "3":
            # Option 2: Quit application.
            print("Exiting application...")
            break
        else:
            # Handle invalid user input.
            print("Invalid choice. Please select again.")

# Run main function.


if __name__ == "__main__":
    main()
