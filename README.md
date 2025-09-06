# SystemAssist V1.1
A cross-platform command line tool for help desk troubleshooting automation.

[![Python Version](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)
[![Platform](https://img.shields.io/badge/platform-Windows%20%7C%20macOS%20%7C%20Linux-lightgrey.svg)]()

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
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Demo](#demo)
- [Troubleshooting](#troubleshooting)
- [Changelog](#changelog)
- [Support](#support)
- [Project Structure](#project-structure)

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
- Windows, macOS, Linux.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/SystemAssist.git
   cd SystemAssist
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Make the script executable (Linux/macOS):
   ```bash
   chmod +x sysassist.py
   ```

## Usage

Run the diagnostic tool:
```bash
python3 sysassist.py
```

Or make it executable and run:
```bash
./sysassist.py
```

### Menu Options:
1. **Network Diagnostics** - Test internet connectivity
2. **Login Info** - Display current user information  
3. **Printer Status** - Check printer status and configuration
4. **System Information** - View system specs and resource usage
5. **Exit** - Close the application

## Contributing

1. Fork the repository  
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)  
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)  
4. Push to the branch (`git push origin feature/AmazingFeature`)  
5. Open a Pull Request  

## License

This project is licensed under the MIT License - see the [LICENSE](./LICENSE) file for details.

## Demo

![SystemAssist Demo](./Demo.png)

## Troubleshooting

### Common Issues:

**Permission Errors:**
- On macOS/Linux, some commands may require sudo privileges
- The tool will warn you when elevated permissions are needed

**Missing Dependencies:**
- Ensure all Python packages are installed: `pip install -r requirements.txt`
- On some systems, you may need to install system tools (ping, lpstat, etc.)

**Network Issues:**
- The network diagnostic requires internet connectivity
- Firewall settings may block ping requests

## Changelog

### v1.1.0
- Enhanced security features
- Improved error handling
- Added cross-platform support
- Updated documentation

### v1.0.0
- Initial release
- Basic diagnostic functionality
- Support for Windows, macOS, and Linux

## Support

If you encounter any issues or have questions:
- Open an issue on GitHub
- Check the troubleshooting section above
- Review the security practices documentation

## Project Structure

```
SystemAssist/
├── sysassist.py          # Main CLI application
├── requirements.txt      # Python dependencies
├── README.md             # This file
├── .gitignore            # Git ignore rules
├── Demo.png              # Demo screenshot of SystemAssist CLI
└── modules/
    ├── network.py        # Network diagnostics
    ├── login.py          # User login information
    ├── printer.py        # Printer status checks
    ├── system_info.py    # System information display
    └── security_logger.py # Security event logging
