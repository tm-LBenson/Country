def display_menu():
    '''Display menu for terminal UI'''
    print("======================================")
    print("          COUNTRY DICTIONARY          ")
    print("======================================")
    print("1. View a country")
    print("2. Add a country")
    print("3. Delete a country")
    print("4. Exit")
    print("======================================")
    choice = input("Enter your choice (1/2/3/4): ")
    return choice

def seed_dictionary():
    '''Generate starter data as a dictionary'''
    return {
        'US': 'United States',
        'UK': 'United Kingdom',
        'CA': 'Canada'
    }

def view_country(country_dict):
    '''Takes in dictionary as parameter, and iterates over the dictionary to find a matching country'''
    print("\nAvailable keys:")
    for key in country_dict:
        print(key)
    key_choice = input("\nEnter a key to view the corresponding country: ")
    
    if key_choice in country_dict:
        print(f"The country for key {key_choice} is {country_dict[key_choice]}.\n")
    else:
        print(f"Invalid key '{key_choice}'. No such country found.\n")

def add_country(country_dict):
    '''takes in the dictionary as a parameter, and adds a new country to the list. Checks to ensure the country doesn't already exist first, if it does, it returns a message'''
    key_choice = input("\nEnter the key for the new country: ")
    if key_choice in country_dict:
        print(f"Key '{key_choice}' already exists. Choose a different key.\n")
        return
    
    country_name = input("Enter the name of the country: ")
    country_dict[key_choice] = country_name
    print(f"Country with key '{key_choice}' added successfully.\n")

def delete_country(country_dict):
    '''removes country from dictionary'''
    key_choice = input("\nEnter a key to delete the corresponding country: ")
    if key_choice in country_dict:
        del country_dict[key_choice]
        print(f"Country with key '{key_choice}' deleted successfully.\n")
    else:
        print(f"Invalid key '{key_choice}'. No such country found.\n")

def main():
    '''initialize the main function'''
    country_dict = seed_dictionary()
    while True:
        choice = display_menu()
        if choice == '1':
            view_country(country_dict)
        elif choice == '2':
            add_country(country_dict)
        elif choice == '3':
            delete_country(country_dict)
        elif choice == '4':
            print("Exiting program.")
            break
        else:
            print("Invalid command. Please enter a valid choice (1/2/3/4).\n")

if __name__ == "__main__":
    main()
