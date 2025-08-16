# import necessary modules
import platform  # used to get system information
import psutil  # used to get hardware and usage stats
import subprocess  # used to run system commands

# defining the run function for system information
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
                    subprocess.run(["cleanmgr"], check=False)
                except Exception as e:
                    print(f"Could not launch Disk Cleanup: {e}")
            elif os_type in ["Linux", "Darwin"]:
                print("You can clear package cache to free up space.")
                print("Attempting to run 'sudo apt-get clean' (Linux only)...")
                try:
                    subprocess.run(["sudo", "apt-get", "clean"], check=False)
                except Exception as e:
                    print(f"Could not run 'apt-get clean': {e}")
            else:
                print("No automatic cleanup available for this OS.")
    except Exception as e:
        # catch-all for any errors during info retrieval
        print(f"Error retrieving system info: {e}")
