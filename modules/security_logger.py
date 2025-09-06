# security_logger.py - Security logging utility module with detailed comments
import logging  # Import logging module for logging events
import os  # Import os module for file system operations
from datetime import datetime  # Import datetime for timestamping logs
import random  # Import random module at module level

class SecurityLogger:
    def __init__(self):
        # Initialize the logger instance
        self.logger = logging.getLogger('systemassist_security')  # Create logger named 'systemassist_security'
        self.logger.setLevel(logging.INFO)  # Set logging level to INFO

        # Create logs directory if it doesn't exist
        log_dir = os.path.join(os.path.dirname(__file__), 'logs')  # Define logs directory path
        os.makedirs(log_dir, exist_ok=True)  # Create directory if not exists

        # Define log file path with current date in filename
        log_file = os.path.join(log_dir, f'security_{datetime.now().strftime("%Y%m%d")}.log')
        handler = logging.FileHandler(log_file)  # Create file handler for logging to file
        handler.setLevel(logging.INFO)  # Set handler level to INFO

        # Define log message format
        formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
        handler.setFormatter(formatter)  # Set formatter for handler
        self.logger.addHandler(handler)  # Add handler to logger

    def log_security_event(self, event_type, details, user_safe_message=None):
        # Log security-related events with optional user-safe message
        self.logger.info(f"{event_type}: {details}")  # Log event details at INFO level
        if user_safe_message:
            print(user_safe_message)  # Print user-friendly message if provided

    def log_error(self, error, context):
        # Log errors securely with context information
        self.logger.error(f"Error in {context}: {str(error)}")  # Log error message at ERROR level
        # Decoy messaging to avoid revealing sensitive info to users
        decoy_messages = [
            "An error occurred. Please try again later.",
            "Operation failed. Contact support if the issue persists.",
            "Unexpected error. Please retry your request.",
            "An issue was detected. Please try again."
        ]
        print(random.choice(decoy_messages))  # Print a random generic error message

# End of security_logger.py
