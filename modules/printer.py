# import modules
import platform  # used to detect the operating system
import subprocess  # used to run system commands

# defining the run function for printer diagnostics
def run():
    print("\n[Printer Diagnostics]")
    os_type = platform.system()  # get the current OS type

    try:
        # choose the correct command based on OS to get printer info
        if os_type == "Windows":
            result = subprocess.run(["powershell", "-Command", "Get-Printer"], capture_output=True, text=True)
            print(result.stdout)  # print the printer list
        elif os_type in ["Linux", "Darwin"]:
            result = subprocess.run(["lpstat", "-p"], capture_output=True, text=True)
            print(result.stdout)  # print the printer status
        else:
            print("Unsupported OS.")  # handle unsupported OS
    except Exception as e:
        # catch-all for any errors during command execution
        print(f"Error checking printer status: {e}")
        print("Troubleshooting steps:")
        if os_type == "Windows":
            print("- Trying to restart Print Spooler service...")
            try:
                subprocess.run(["net", "stop", "spooler"], check=False)
                subprocess.run(["net", "start", "spooler"], check=False)
                print("Print Spooler service restarted.")
            except Exception as ex:
                print(f"Could not restart Print Spooler: {ex}")
            print("- Check printer cables and power.")
        elif os_type in ["Linux", "Darwin"]:
            print("- Trying to restart CUPS service (may require sudo)...")
            try:
                subprocess.run(["sudo", "systemctl", "restart", "cups"], check=False)
                print("CUPS service restart attempted.")
            except Exception as ex:
                print(f"Could not restart CUPS: {ex}")
            print("- Check printer connection and status.")
        else:
            print("- No automated troubleshooting available for this OS.")
