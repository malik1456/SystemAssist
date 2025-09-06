# printer.py - Printer diagnostics module
# ----------------------------------------
import platform  # Detect the operating system
import subprocess  # Run system commands
from modules.security_logger import SecurityLogger  # Import security logger at module level

# Helper function for troubleshooting steps
def print_troubleshooting(os_type):
    """Prints troubleshooting steps based on OS type."""
    if os_type == "Windows":
        print("- Trying to restart Print Spooler service...")
        try:
            subprocess.run(["net", "stop", "spooler"], check=True)
            subprocess.run(["net", "start", "spooler"], check=True)
            print("Print Spooler service restarted.")
        except subprocess.CalledProcessError as ex:
            print(f"Could not restart Print Spooler: {ex}")
        print("- Check printer cables and power.")
    elif os_type == "Linux":
        print("- Trying to restart CUPS service (may require sudo)...")
        try:
            subprocess.run(["sudo", "systemctl", "restart", "cups"], check=True)
            print("CUPS service restart attempted.")
        except subprocess.CalledProcessError as ex:
            print(f"Could not restart CUPS: {ex}")
        print("- Check printer connection and status.")
    elif os_type == "Darwin":
        print("- Trying to restart CUPS service (may require sudo)...")
        try:
            subprocess.run(["sudo", "launchctl", "stop", "org.cups.cupsd"], check=True)
            subprocess.run(["sudo", "launchctl", "start", "org.cups.cupsd"], check=True)
            print("CUPS service restart attempted.")
        except (subprocess.CalledProcessError, FileNotFoundError) as ex:
            print(f"Could not restart CUPS: {ex}")
        print("- Check printer connection and status.")
    else:
        print("- No automated troubleshooting available for this OS.")

# Main function for printer diagnostics
def run():
    print("\n[Printer Diagnostics]")
    os_type = platform.system()  # Get the current OS type

    try:
        # Run the correct command based on OS to get printer info
        if os_type == "Windows":
            # Windows: Use PowerShell to list printers
            result = subprocess.run(
                ["powershell", "-Command", "Get-Printer"],
                capture_output=True, text=True, check=True
            )
            print(result.stdout)  # Display printer list
        elif os_type in ["Linux", "Darwin"]:
            # Linux/macOS: Use lpstat to show printer status
            result = subprocess.run(
                ["lpstat", "-p"],
                capture_output=True, text=True, check=True
            )
            print(result.stdout)  # Display printer status
        else:
            # Unsupported OS case
            print("Unsupported OS.")
    except subprocess.CalledProcessError as e:
        # Log error securely and show generic message
        logger = SecurityLogger()
        logger.log_error(e, "printer.run")
        print("Error checking printer status. Please try again later.")
        print_troubleshooting(os_type)
    except FileNotFoundError:
        print("Printer diagnostic command not found. Please ensure required utilities are installed.")
        print("Troubleshooting in progress")
        print_troubleshooting(os_type)
    except Exception as e:
        logger = SecurityLogger()
        logger.log_error(e, "printer.run")
        print("An unexpected error occurred while checking printer status. Please try again later.")
        print("Troubleshooting in progress")
        print_troubleshooting(os_type)
# End of printer diagnostics module
