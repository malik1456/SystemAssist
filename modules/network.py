# network.py - Network diagnostics module
# ----------------------------------------
import platform  # Used to detect the operating system
import subprocess  # Used to run system commands

# Main function for network diagnostics
def run():
    print("\n[Network Diagnostics]")
    os_type = platform.system()  # Get the current OS type
    print(f"Detected OS: {os_type}")
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
        # Handle ping failure and show error output
        print("Ping failed. Here's what happened:")
        print(e.stdout)
        print(e.stderr)
        print("Troubleshooting steps:")
        if os_type == "Windows":
            print("- Trying to flush DNS cache...")
            try:
                subprocess.run(["ipconfig", "/flushdns"], check=True)
                print("DNS cache flushed.")
            except subprocess.CalledProcessError:
                print("Could not flush DNS.")
            print("- Try restarting your router or checking your network cables.")
        elif os_type in ["Linux", "Darwin"]:
            print("- Trying to restart network service (may require sudo)...")
            print("Warning: This may require your password and elevated privileges. Only run this if you trust the script and understand the risks.")
            try:
                subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"], check=True)
                print("NetworkManager restart attempted.")
            except subprocess.CalledProcessError:
                print("Could not restart network service.")
            print("- Try checking your network cables or Wi-Fi connection.")
        else:
            print("- No automated troubleshooting available for this OS.")
    except FileNotFoundError:
        # Handle case where ping command is missing
        print("Ping command not found. Is it installed and in your PATH?")
    except Exception:
        # Catch-all for any other errors, limit sensitive info
        print("An unexpected error occurred during network diagnostics. Please contact your system administrator if this persists.")
# End of network diagnostics module
