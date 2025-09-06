# SystemAssist Functionality Fixes

## Critical Issues (Fix Immediately)

### 1. modules/login.py - NameError Bug
- **Issue**: `print_troubleshooting(os_type)` called but function not defined in this module
- **Fix**: Import `print_troubleshooting` from `modules.printer` or define it locally
- **Impact**: Currently crashes on exceptions

### 2. modules/system_info.py - OS Compatibility
- **Issue**: Hardcoded `apt-get` for Linux cleanup (Debian/Ubuntu only)
- **Fix**: Detect Linux distro and use appropriate package manager (apt, yum, pacman, etc.)
- **Issue**: Uses `systemctl` for macOS (Darwin)
- **Fix**: Use `launchctl` for macOS service management
- **Issue**: SecurityLogger import inside except block
- **Fix**: Move import to module level

### 3. modules/printer.py - Service Management
- **Issue**: Uses `systemctl` for Linux/macOS printer service restart
- **Fix**: Use platform-appropriate service management:
  - Linux: Check if systemd, fallback to service/init.d
  - macOS: Use `launchctl` for CUPS
- **Issue**: SecurityLogger import inside except block
- **Fix**: Move import to module level

## Moderate Issues

### 4. modules/security_logger.py - Performance
- **Issue**: `random` imported inside `log_error` function
- **Fix**: Move `import random` to module level

### 5. sysassist.py - Code Quality
- **Issue**: Redundant length checks in `get_valid_choice()`
- **Fix**: Remove duplicate `len(choice) > 1` check since `max_input_length = 1`

### 6. requirements.txt - Dependency Cleanup
- **Issue**: `requests` listed but not used
- **Fix**: Remove `requests` from requirements.txt

### 7. General - SecurityLogger Imports
- **Issue**: SecurityLogger imported in except blocks across multiple modules
- **Fix**: Move all SecurityLogger imports to module level for reliability

## Testing After Fixes
- [ ] Test login functionality with forced exceptions
- [ ] Test system info cleanup on different Linux distros
- [ ] Test printer troubleshooting on macOS
- [ ] Test all modules on Windows, Linux, macOS
- [ ] Verify no import errors in exception paths
- [ ] Run full application flow without errors

## Priority Order
1. Fix login.py NameError (critical)
2. Fix OS-specific commands in system_info.py and printer.py
3. Move SecurityLogger imports to module level
4. Clean up redundant code and unused dependencies
5. Performance optimizations (random import)
6. Comprehensive testing
