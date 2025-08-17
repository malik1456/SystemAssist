# SystemAssist V1.0
A cross-platform command line tool for help desk troubleshooting automation.

## Features
- **Netork Diagnostics** - Tests connectivity checks ips.
- **User Login Info** - Allows for user information.
- **Printer Status Check** - Gets printer using platform(powershell).
- **System Insights** -Displays OS,CPU,memory, and disk usage using 'psutil'.

### Module Breakdown
| Module             | Description                                               |
|--------------------|-----------------------------------------------------------|
| [`network.py`](network.py)     | Runs ping tests, gathers IP info, and checks DNS resolution |
| [`login.py`](login.py)         | Displays current user session and login details          |
| [`printer.py`](printer.py)     | Checks printer status using PowerShell (Windows) or CUPS (macOS/Linux) |
| [`system_info.py`](system_info.py) | Reports OS, CPU, memory, and disk usage using `psutil`      |

#### Quick Start

##### Requirements
- Python 3.8+ installed.
- Git installed.
- Windows,Macos,Linux.

```bash
git clone git@github.com:malik1456/SystemAssist.git
cd SystemAssist
pip install -r requirements.txt
python sysassist.py
