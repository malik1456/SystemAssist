#!/usr/bin/env python3
# Import system-related modules
import sys  # Import sys module for system-specific parameters and functions
import re  # Import re module for input validation patterns
from modules import network  # Import network diagnostics module
from modules import login  # Import login information module
from modules import printer  # Import printer diagnostics module
from modules import system_info  # Import system information module
from modules.security_logger import SecurityLogger  # Import security logging module

# Initialize security logger
security_logger = SecurityLogger()

# Define a function to get and validate user menu choice with enhanced security
def get_valid_choice():
    valid_choices = {'1', '2', '3', '4', '5'}  # Set of valid menu options
    max_attempts = 3  # Maximum number of attempts allowed
    max_input_length = 1  # Maximum allowed input length to prevent buffer overflow

    for attempt in range(max_attempts):  # Loop to allow multiple attempts
        try:
            choice = input("Select an option with a number (1-5): ").strip()  # Get user input and strip whitespace

            # Security: Check input length to prevent buffer overflow attacks
            if len(choice) > max_input_length:
                security_logger.log_security_event("INPUT_TOO_LONG", f"Input length {len(choice)} exceeds maximum {max_input_length}")
                print("Input too long. Please enter a single digit.")
                continue

            # Security: Check for potentially malicious patterns (basic injection prevention)
            if re.search(r'[;&|`$()<>]', choice):
                security_logger.log_security_event("SUSPICIOUS_INPUT", f"Potentially malicious input detected: {choice}")
                print("Invalid input detected. Please enter a number between 1 and 5.")
                continue

            if not choice:  # Check if input is empty
                print("Input cannot be empty.")  # Inform user
                continue  # Prompt again

            if len(choice) > 1:  # Check if input length is more than one character
                print("Please enter a single digit.")  # Inform user
                continue  # Prompt again

            if choice in valid_choices:  # Check if input is a valid choice
                security_logger.log_security_event("VALID_INPUT", f"User selected option: {choice}")
                return choice  # Return valid choice

            try:
                num = int(choice)  # Try converting input to integer
                if 1 <= num <= 5:  # Check if number is within valid range
                    security_logger.log_security_event("VALID_INPUT", f"User selected option: {choice}")
                    return choice  # Return valid choice
                else:
                    print("Please enter a number between 1 and 5.")  # Inform user of invalid range
            except ValueError:
                print("Please enter a valid number.")  # Inform user of invalid input

        except (EOFError, KeyboardInterrupt):
            # Security: Handle interruption gracefully without exposing system details
            security_logger.log_security_event("INPUT_INTERRUPTION", "User interrupted input")
            print("\nInput interrupted. Exiting for security.")
            sys.exit(1)
        except Exception as e:
            # Security: Log unexpected errors without exposing details
            security_logger.log_error(e, "get_valid_choice")
            print("An unexpected error occurred. Please try again.")

    # Security: Log excessive failed attempts
    security_logger.log_security_event("EXCESSIVE_INVALID_ATTEMPTS", f"User exceeded {max_attempts} invalid attempts")
    print("Too many invalid attempts. Exiting.")  # Inform user of too many invalid attempts
    sys.exit(1)  # Exit program with error code

# Define the main function to run the CLI loop
def main():
    while True:  # Infinite loop to keep program running until exit
        print("\nWelcome to the System Assistant!")  # Welcome message
        print("Please choose an option that best suits your needs:")  # Prompt message
        print("1. Network Diagnostics")  # Option 1
        print("2. Login issues")  # Option 2
        print("3. Printer problems")  # Option 3
        print("4. System Information")  # Option 4
        print("5. Exit")  # Option 5

        choice = get_valid_choice()  # Get validated user choice

        if choice == "1":  # If choice is 1
            network.run()  # Run network diagnostics
        elif choice == "2":  # If choice is 2
            login.run()  # Run login info
        elif choice == "3":  # If choice is 3
            printer.run()  # Run printer diagnostics
        elif choice == "4":  # If choice is 4
            system_info.run()  # Run system info
        elif choice == "5":  # If choice is 5
            print("Exiting the System Assistant. Goodbye!")  # Exit message
            sys.exit()  # Exit program
        else:
            print("Invalid choice. Please try again.")  # Fallback invalid choice message

# Check if script is run directly and call main function
if __name__ == "__main__":
    main()
