"""
Database Setup Script
Run this to initialize the database with sample data
"""

from db import Database, initialize_sample_data, test_connection
from colorama import Fore, Style

print(f"\n{Fore.CYAN}{'='*60}{Style.RESET_ALL}")
print(f"{Fore.YELLOW}  Ishuri-Connect Database Setup{Style.RESET_ALL}")
print(f"{Fore.CYAN}{'='*60}{Style.RESET_ALL}\n")

# Test connection
print(f"{Fore.CYAN}Step 1:{Style.RESET_ALL} Testing database connection...")
if test_connection():
    print(f"{Fore.GREEN}✓ Connection successful!{Style.RESET_ALL}\n")
else:
    print(f"{Fore.RED}✗ Connection failed!{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Please check your .env file configuration.{Style.RESET_ALL}\n")
    exit(1)

# Initialize sample data
print(f"{Fore.CYAN}Step 2:{Style.RESET_ALL} Adding sample schools...")
if initialize_sample_data():
    print(f"{Fore.GREEN}✓ Sample schools added!{Style.RESET_ALL}\n")
else:
    print(f"{Fore.YELLOW}⚠ Some schools may already exist{Style.RESET_ALL}\n")

print(f"{Fore.GREEN}{'='*60}{Style.RESET_ALL}")
print(f"{Fore.GREEN}  Setup complete! You can now run main.py{Style.RESET_ALL}")
print(f"{Fore.GREEN}{'='*60}{Style.RESET_ALL}\n")
