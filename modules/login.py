# login.py - User login information module
# ----------------------------------------
import platform  # Used to detect the operating system
import subprocess  # Used to run system commands

# Helper function for troubleshooting steps
def print_troubleshooting(os_type):
    """Prints troubleshooting steps based on OS type."""
    if os_type == "Windows":
        print("- Ensure your user account is active and not locked.")
        print("- Make sure you have permission to run system commands.")
        print("- Try running the script as an administrator.")
        print("- Check if 'whoami' command is available.")
    elif os_type in ["Linux", "Darwin"]:
        print("- Ensure your user account is active and not locked.")
        print("- Make sure you have permission to run system commands.")
        print("- Try running the script with sudo.")
        print("- Check if 'id' command is available.")
    else:
        print("- Unsupported OS. No troubleshooting steps available.")

# Main function for displaying login information
def run():
    print("\n[Login Info]")
    os_type = platform.system()  # Get the current OS type
    try:
        # Choose the correct command based on OS to get login info
        if os_type == "Windows":
            result = subprocess.run(["whoami"], capture_output=True, text=True, check=True)
            print(f"Username: {result.stdout.strip()}")  # Display formatted username
        elif os_type in ["Linux", "Darwin"]:
            print("Warning: The 'id' command may require elevated privileges on some systems.")
            result = subprocess.run(["id"], capture_output=True, text=True, check=True)
            print(f"User/Group Info: {result.stdout.strip()}")  # Display formatted user/group info
        else:
            # Unsupported OS case
            print("Unsupported OS.")
    except subprocess.CalledProcessError as e:
        # Log error securely and show generic message
        from modules.security_logger import SecurityLogger
        logger = SecurityLogger()
        logger.log_error(e, "login.run")
        print("Error retrieving login info. Please try again later.")
    except FileNotFoundError:
        print("Login info command not found. Please ensure required utilities are installed.")
    except Exception as e:
        from modules.security_logger import SecurityLogger
        logger = SecurityLogger()
        logger.log_error(e, "login.run")
        print("An unexpected error occurred while retrieving login info. Please try again later.")
# End of login information module
