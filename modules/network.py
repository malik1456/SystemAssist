# network information modules
import platform  # used to detect the operating system
import subprocess  # used to run system commands

# defining the run function for network diagnostics
def run():
    print("\n[Network Diagnostics]")
    os_type = platform.system()  # get the current OS type
    print(f"Detected OS: {os_type}")
    print("Pinging 8.8.8.8...\n")  # notify user of the ping target
    try:
        # choose the correct ping command based on OS
        if os_type == "Windows":
            result = subprocess.run(["ping", "-n", "4", "8.8.8.8"], capture_output=True, text=True, check=True)
        elif os_type in ["Linux", "Darwin"]:
            result = subprocess.run(["ping", "-c", "4", "8.8.8.8"], capture_output=True, text=True, check=True)
        else:
            print("Unsupported OS for network diagnostics.")
            return
        # displays ping results to the user
        print(result.stdout)
    except subprocess.CalledProcessError as e:
        # handle ping failure and show error output
        print("Ping failed. Here's what happened:")
        print(e.stdout)
        print(e.stderr)
        # troubleshooting steps
        print("Troubleshooting steps:")
        if os_type == "Windows":
            print("- Trying to flush DNS cache...")
            try:
                subprocess.run(["ipconfig", "/flushdns"], check=False)
                print("DNS cache flushed.")
            except Exception as ex:
                print(f"Could not flush DNS: {ex}")
            print("- Try restarting your router or checking your network cables.")
        elif os_type in ["Linux", "Darwin"]:
            print("- Trying to restart network service (may require sudo)...")
            try:
                subprocess.run(["sudo", "systemctl", "restart", "NetworkManager"], check=False)
                print("NetworkManager restart attempted.")
            except Exception as ex:
                print(f"Could not restart network service: {ex}")
            print("- Try checking your network cables or Wi-Fi connection.")
        else:
            print("- No automated troubleshooting available for this OS.")
    except FileNotFoundError:
        # handle case where ping command is missing
        print("Ping command not found. Is it installed and in your PATH?")
    except Exception as e:
        # catch-all for any other errors
        print(f"Unexpected error: {e}")
# end of network information modules
