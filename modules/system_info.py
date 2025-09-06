# Import necessary modules
import platform  # used to get system information
import psutil  # used to get hardware and usage stats
import subprocess  # used to run system commands
from modules.security_logger import SecurityLogger  # Import security logger at module level

# Define the run function for system information
def run():
    print("\n[System Info]")

    try:
        # print OS name and version
        print(f"OS: {platform.system()} {platform.release()}")
        # print system architecture
        print(f"Architecture: {platform.machine()}")
        # print processor information
        print(f"Processor: {platform.processor()}")
        # print number of CPU cores
        print(f"CPU Cores: {psutil.cpu_count(logical=True)}")
        # print total memory in GB
        print(f"Memory: {round(psutil.virtual_memory().total / (1024 ** 3), 2)} GB")
        # print disk usage percentage
        disk_usage = psutil.disk_usage('/')
        print(f"Disk Usage: {disk_usage.percent}% used")
        # if disk usage is over 60%, suggest clearing space
        if disk_usage.percent > 60:
            print("Warning: Disk usage is over 60%.")
            os_type = platform.system()
            if os_type == "Windows":
                print("You can run Disk Cleanup to free up space.")
                print("Attempting to launch Disk Cleanup...")
                try:
                    subprocess.run(["cleanmgr"], check=True)
                except FileNotFoundError:
                    print("Disk Cleanup utility not found on this system.")
                except subprocess.CalledProcessError:
                    print("Disk Cleanup failed to launch. Try running manually.")
            elif os_type == "Linux":
                print("You can clear package cache to free up space.")
                print("Attempting to detect package manager and clear cache...")
                print("Warning: This may require your password and elevated privileges. Only run this if you trust the script and understand the risks.")

                # Detect Linux distribution and use appropriate package manager
                try:
                    # Try to detect distro
                    with open('/etc/os-release', 'r') as f:
                        os_release = f.read().lower()

                    if 'ubuntu' in os_release or 'debian' in os_release:
                        subprocess.run(["sudo", "apt-get", "clean"], check=True)
                        print("Package cache cleared using apt-get.")
                    elif 'fedora' in os_release or 'centos' in os_release or 'rhel' in os_release:
                        subprocess.run(["sudo", "dnf", "clean", "all"], check=True)
                        print("Package cache cleared using dnf.")
                    elif 'arch' in os_release or 'manjaro' in os_release:
                        subprocess.run(["sudo", "pacman", "-Sc", "--noconfirm"], check=True)
                        print("Package cache cleared using pacman.")
                    else:
                        print("Unsupported Linux distribution for automatic cleanup.")
                except (FileNotFoundError, subprocess.CalledProcessError):
                    print("Automatic cleanup failed. Try clearing package cache manually.")
            elif os_type == "Darwin":
                print("You can clear Homebrew cache to free up space.")
                print("Attempting to run 'brew cleanup'...")
                print("Warning: This may require your password and elevated privileges. Only run this if you trust the script and understand the risks.")
                try:
                    subprocess.run(["brew", "cleanup"], check=True)
                    print("Homebrew cache cleared.")
                except (FileNotFoundError, subprocess.CalledProcessError):
                    print("Homebrew cleanup failed. Try running 'brew cleanup' manually.")
            else:
                print("No automatic cleanup available for this OS.")
    except Exception as e:
        logger = SecurityLogger()
        logger.log_error(e, "system_info.run")
        print("Error retrieving system info. Please try again later.")
