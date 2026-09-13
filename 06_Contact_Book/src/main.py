
class Contact_book:
    """A simple contact book to manage contacts."""
    
    def __init__(self):
        self.contacts = {}
    
            
    def add_contact(self, name, phone_number, email=None):
        if name in self.contacts:
            print(f"\nContact with name '{name}' already exists.")
            return

        self.contacts[name] = {}
        if phone_number.isdigit() and len(phone_number) == 10:
            self.contacts[name]['phone_number'] = phone_number
        else:
            print("Invalid phone number. It should be a 10-digit number.")
            return
        self.contacts[name]['email'] = email
        print(f"Contact '{name}' added successfully.")
    
    
    def view_contacts(self):
        if not self.contacts:
            print("\nNo contacts found.")
            return

        for name, details in self.contacts.items():
            print("\n_" * 50)
            print("View Contacts")
            print(f"Name: {name}")
            print(f"Phone Number: {details['phone_number']}")
            if details['email']:
                print(f"Email: {details['email']}")
            print("_" * 50)
        
        
    def delete_contact(self, name):
        if name not in self.contacts:
            print(f"\nContact with name '{name}' does not exist.")
            return

        del self.contacts[name]
        print(f"\nContact '{name}' deleted successfully.")
    
    
    def update_contact(self, name, phone_number=None, email=None):
        if name not in self.contacts:
            print(f"\nContact with name '{name}' does not exist.")
            return

        else :
            if phone_number.isdigit() and len(phone_number) == 10:
                self.contacts[name]['phone_number'] = phone_number
            else:
                print("\nInvalid phone number. It should be a 10-digit number.")
                return
            if email:
                self.contacts[name]['email'] = email
            print(f"\nContact '{name}' updated successfully.")
            

if __name__ == "__main__":
    contact_book = Contact_book()
    
    while True:
        print("=" * 50)
        print("\n\nWelcome to the Contact Book !!")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Delete Contact")
        print("4. Update Contact")
        print("5. Exit")
        
        choice = input("Enter your choice (1-5): ")
        
        if choice == '1':
            name = input("Enter contact name: ")
            phone_number = input("Enter phone number: ")
            email = input("Enter email (optional): ")
            contact_book.add_contact(name, phone_number, email)
        
        elif choice == '2':
            contact_book.view_contacts()
        
        elif choice == '3':
            name = input("Enter contact name to delete: ")
            contact_book.delete_contact(name)
        
        elif choice == '4':
            name = input("Enter contact name to update: ")
            phone_number = input("Enter new phone number (leave blank to keep unchanged): ")
            email = input("Enter new email (leave blank to keep unchanged): ")
            contact_book.update_contact(name, phone_number if phone_number else None, email if email else None)
        
        elif choice == '5':
            print("\nExiting the Contact Book. Goodbye!")
            break
        
        else:
            print("\nInvalid choice. Please try again.")