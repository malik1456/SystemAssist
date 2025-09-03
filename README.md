# SystemAssist V1.0
A cross-platform command line tool for help desk troubleshooting automation.

## Prerequisites
- Python 3.x installed ([Download Python](https://www.python.org/downloads/))
- Git installed ([Download Git](https://git-scm.com/downloads))

## Features
- **Network Diagnostics** - Tests connectivity, checks IPs.
- **User Login Info** - Displays user information.
- **Printer Status Check** - Gets printer status using platform tools (PowerShell/CUPS).
- **System Insights** - Displays OS, CPU, memory, and disk usage using 'psutil'.

### Module Breakdown
| Module             | Description                                               |
|--------------------|-----------------------------------------------------------|
| [`network.py`](network.py)     | Runs ping tests, gathers IP info, and checks DNS resolution |
| [`login.py`](login.py)         | Displays current user session and login details          |
| [`printer.py`](printer.py)     | Checks printer status using PowerShell (Windows) or CUPS (macOS/Linux) |
| [`system_info.py`](system_info.py) | Reports OS, CPU, memory, and disk usage using `psutil`      |

#### Quick Start
```bash
git clone git@github.com:malik1456/SystemAssist.git
cd SystemAssist
pip install -r requirements.txt
python sysassist.py
```
