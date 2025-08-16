# importing all of my system related modules
import sys
from modules import network
from modules import login
from modules import printer
from modules import system_info

# defining the main function
def main():
    # writing a loop to interact with user in CLI to get inputs
    while True:
        print("\nWelcome to the System Assistant!")
        print("Please choose an option that best suits your needs:")
        print("1. Network Diagnostics")
        print("2. Login issues")
        print("3. Printer problems")
        print("4. System Information")
        print("5. Exit")

        # creating a choice variable to get user input
        choice = input("Select an option with a number (1-5):")

        # checking the choice and calling the respective function
        if choice == "1":
            network.run()
        elif choice == "2":
            login.run()
        elif choice == "3":
            printer.run()
        elif choice == "4":
            system_info.run()
        elif choice == "5":
            print("Exiting the System Assistant. Goodbye!")
            sys.exit()
        else:
            print("Invalid choice. Please try again.")

# checking if the script is run directly
if __name__ == "__main__":
    # calling the main function
    main()