# Create an empty dictionary to store contacts
contacts = {}

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    contacts[name] = phone
    print(f"Contact '{name}' added successfully.")

def view_contacts():
    if not contacts:
        print("Your contact book is empty.")
    else:
        print("Your contacts:")
        for name, phone in contacts.items():
            print(f"{name}: {phone}")
            
def update_contact():
    name = input("Enter the name of the contact to update: ")
    if name in contacts:
        new_phone = input(f"Enter the new phone number for {name}: ")
        contacts[name] = new_phone
        print(f"Contact '{name}' updated successfully.")
    else:
        print(f"Contact '{name}' not found in your contact book. You can add a new contact.")

def search_contact():
    name = input("Enter the name you want to search for: ")
    if name in contacts:
        print(f"{name}: {contacts[name]}")
def delete_contact():
    name = input("Enter the name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully.")
    else:
        print(f"Contact '{name}' not found in your contact book.")

while True:
    print("Options:")
    print("Enter 'add' to add a new contact")
    print("Enter 'view' to view all contacts")
    print("Enter 'update' to update a contact")
    print("Enter 'search' to search for a contact")
    print("Enter 'delete' to delete a contact")
    print("Enter 'quit' to exit the program")

    choice = input("Enter your choice: ")

    if choice == "quit":
        break
    elif choice == "add":
        add_contact()
    elif choice == "view":
        view_contacts()
    elif choice == "search":
        search_contact()
    elif choice == "update":
        update_contact()
    elif choice == "delete":
        delete_contact()
    else:
        print("Invalid choice. Please try again.")
