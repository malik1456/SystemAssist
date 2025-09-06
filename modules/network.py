# network.py - Network diagnostics module
# ----------------------------------------
import platform  # Used to detect the operating system
import subprocess  # Used to run system commands

# Main function for network diagnostics
def run():
    print("\n[Network Diagnostics]")
    os_type = platform.system()  # Get the current OS type
    print("Pinging 8.8.8.8...\n")  # Notify user of the ping target
    try:
        # Choose the correct ping command based on OS
        if os_type == "Windows":
            result = subprocess.run(["ping", "-n", "4", "8.8.8.8"], capture_output=True, text=True, check=True)
            print(result.stdout)
        elif os_type in ["Linux", "Darwin"]:
            print("Warning: The 'ping' and network restart commands may require elevated privileges on some systems.")
            result = subprocess.run(["ping", "-c", "4", "8.8.8.8"], capture_output=True, text=True, check=True)
            print(result.stdout)
        else:
            # Unsupported OS case
            print("Unsupported OS for network diagnostics.")
            return
    except subprocess.CalledProcessError as e:
        # Log error securely and show generic message
        from modules.security_logger import SecurityLogger
        logger = SecurityLogger()
        logger.log_error(e, "network.run")
        print("Network diagnostics failed. Please try again later.")
    except FileNotFoundError:
        print("Ping command not found. Please ensure it is installed.")
    except Exception as e:
        from modules.security_logger import SecurityLogger
        logger = SecurityLogger()
        logger.log_error(e, "network.run")
        print("An unexpected error occurred during network diagnostics. Please try again later.")
# End of network diagnostics module
