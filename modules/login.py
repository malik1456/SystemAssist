# downloading modules
import platform  # used to detect the operating system
import subprocess  # used to run system commands

# defining the run function for login information
def run():
    print("\n[Login Info]")
    os_type = platform.system()  # get the current OS type

    try:
        # choose the correct command based on OS to get login info
        if os_type == "Windows":
            result = subprocess.run(["whoami"], capture_output=True, text=True)
            print(result.stdout)  # print the username
        elif os_type in ["Linux", "Darwin"]:
            result = subprocess.run(["id"], capture_output=True, text=True)
            print(result.stdout)  # print the user and group info
        else:
            print("Unsupported OS.")  # handle unsupported OS
    except Exception as e:
        # catch-all for any errors during command execution
        print(f"Error retrieving login info: {e}")
        print("Troubleshooting steps:")
        print("- Ensure your user account is active and not locked.")
        print("- Make sure you have permission to run system commands.")
        print("- Try running the script as an administrator or with sudo.")
        print("- On Linux/Mac, check if 'id' command is available. On Windows, check 'whoami'.")
