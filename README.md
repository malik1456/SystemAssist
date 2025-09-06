# SystemAssist V1.1
A cross-platform command line tool for help desk troubleshooting automation.

## Navigation
- [Security Practices](#security-practices)
  - [Input Validation & Sanitization](#input-validation--sanitization)
  - [Error Handling & Information Disclosure Prevention](#error-handling--information-disclosure-prevention)
  - [Subprocess Security](#subprocess-security)
  - [Logging & Monitoring](#logging--monitoring)
- [Prerequisites](#prerequisites)
- [Features](#features)
- [Module Breakdown](#module-breakdown)
- [Quick Start](#quick-start)

## Security Practices
### Note: This tool is intended for local diagnostics. If deployed in shared or remote environments, additional hardening is recommended.
This project implements several security best practices to protect against common vulnerabilities:

### Input Validation & Sanitization
- **Length Limits**: Input is restricted to prevent buffer overflow attacks
- **Pattern Matching**: Regular expressions detect and block potentially malicious input patterns
- **Type Validation**: Strict validation ensures only expected data types are accepted

### Error Handling & Information Disclosure Prevention
- **Generic Error Messages**: User-facing errors are generic to prevent information leakage
- **Secure Logging**: Detailed error information is logged securely for administrators
- **Decoy Messaging**: Randomized error messages to confuse potential attackers

### Subprocess Security
- **No Shell Injection**: Commands are executed without shell=True to prevent injection
- **Privilege Awareness**: Warnings for operations that may require elevated privileges
- **Safe Command Execution**: Input is never passed directly to system commands
- **Cross-Platform Security**: SystemAssist is platform aware, adapting security measures based on the operating system (Windows, macOS, Linux) to ensure consistent security across platforms

### Logging & Monitoring
- **Security Event Logging**: All security-related events are logged with timestamps
- **Attempt Limiting**: Maximum attempts prevent brute force attacks
- **Interruption Handling**: Graceful handling of keyboard interrupts and EOF

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
| [`network.py`](modules/network.py)     | Runs ping tests, gathers IP info, and checks DNS resolution |
| [`login.py`](modules/login.py)         | Displays current user session and login details          |
| [`printer.py`](modules/printer.py)     | Checks printer status using PowerShell (Windows) or CUPS (macOS/Linux) |
| [`system_info.py`](modules/system_info.py) | Reports OS, CPU, memory, and disk usage using `psutil`      |

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
