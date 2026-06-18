class ContactManager:
    def __init__(self):
        self.contacts = []

    
    # Validation Methods
    
    def validate_phone(self, phone):
        allowed_chars = "0123456789-+"

        for char in phone:
            if char not in allowed_chars:
                return False

        return True

    def validate_email(self, email):
        if email == "":
            return True

        return "@" in email and "." in email

    
    # Add Contact
    
    def add_contact(self, name, phone, email=""):

        # Check for duplicate contact
        for contact in self.contacts:
            if contact["name"].lower() == name.lower():
                print("Contact already exists.")
                return

        if not self.validate_phone(phone):
            print("Error: Invalid phone number. Use only digits and hyphens.")
            return

        if not self.validate_email(email):
            print("Error: Invalid email address.")
            return

        self.contacts.append({
            "name": name,
            "phone": phone,
            "email": email
        })

        print("Contact added successfully.")

    # View Contact
    def view_contact(self, name):

        for contact in self.contacts:
            if contact["name"].lower() == name.lower():

                print("-" * 30)
                print(f"Name  : {contact['name']}")
                print(f"Phone : {contact['phone']}")
                print(f"Email : {contact['email']}")
                print("-" * 30)

                return

        print("Contact not found.")

    # Update Contact
    
    def update_contact(self, name, new_phone=None, new_email=None):

        for contact in self.contacts:

            if contact["name"].lower() == name.lower():

                if new_phone:

                    if not self.validate_phone(new_phone):
                        print("Error: Invalid phone number.")
                        return

                    contact["phone"] = new_phone

                if new_email:

                    if not self.validate_email(new_email):
                        print("Error: Invalid email address.")
                        return

                    contact["email"] = new_email

                print("Contact updated successfully.")
                return

        print("Contact not found.")

    
    # Delete Contact
    
    def delete_contact(self, name):

        for contact in self.contacts:

            if contact["name"].lower() == name.lower():
                self.contacts.remove(contact)
                print("Contact deleted successfully.")
                return

        print("Contact not found.")

    # Advanced Search
   
    def search_contacts(self, keyword):

        results = []

        for contact in self.contacts:

            if (keyword.lower() in contact["name"].lower()
                    or keyword in contact["phone"]
                    or keyword.lower() in contact["email"].lower()):

                results.append(contact)

        if not results:
            print("No matching contacts found.")
            return

        print("\n=== Search Results ===")

        for contact in results:
            print("-" * 30)
            print(f"Name  : {contact['name']}")
            print(f"Phone : {contact['phone']}")
            print(f"Email : {contact['email']}")
            print("-" * 30)


    # List All Contacts
    
    def list_all_contacts(self):

      if not self.contacts:
        print("No contacts available.")
        return

      print("\n=== All Contacts ===")

      sorted_contacts = sorted(
        self.contacts,
        key=lambda contact: contact["name"].lower()
    )

      for contact in sorted_contacts:
        print("-" * 30)
        print(f"Name  : {contact['name']}")
        print(f"Phone : {contact['phone']}")
        print(f"Email : {contact['email']}")
        print("-" * 30)


# Main Menu Function

def main():

    manager = ContactManager()

    while True:

        print("\n=== Contact Manager Menu ===")
        print("1. Add Contact")
        print("2. View Contact")
        print("3. Update Contact")
        print("4. Delete Contact")
        print("5. Search Contacts")
        print("6. List All Contacts")
        print("7. Exit")

        choice = input("Choose an option (1-7): ")

        if choice == "1":

            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email (optional): ")

            manager.add_contact(name, phone, email)

        elif choice == "2":

            name = input("Enter contact name: ")
            manager.view_contact(name)

        elif choice == "3":

            name = input("Enter contact name to update: ")

            new_phone = input(
                "Enter new phone number (leave blank to keep current): "
            )

            new_email = input(
                "Enter new email (leave blank to keep current): "
            )

            manager.update_contact(
                name,
                new_phone if new_phone else None,
                new_email if new_email else None
            )

        elif choice == "4":

            name = input("Enter contact name to delete: ")
            manager.delete_contact(name)

        elif choice == "5":

            keyword = input(
                "Search by name, phone number, or email: "
            )

            manager.search_contacts(keyword)

        elif choice == "6":

            manager.list_all_contacts()

        elif choice == "7":

            print("Exiting Contact Manager...")
            break

        else:

            print("Invalid choice. Please enter a number from 1 to 7.")


if __name__ == "__main__":
    main()