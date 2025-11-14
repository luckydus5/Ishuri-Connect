"""
Database Setup Script
Run this to initialize the database with the enhanced schema
Instructions:
1. Make sure MySQL is running
2. Update .env file with your database credentials
3. Run this script: python setup_db.py
"""

from colorama import Fore, Style, init
import mysql.connector
import os
from dotenv import load_dotenv

init(autoreset=True)
load_dotenv()

print(f"\n{Fore.CYAN}{'='*70}{Style.RESET_ALL}")
print(f"{Fore.YELLOW}  🚀 Ishuri-Connect Database Setup{Style.RESET_ALL}")
print(f"{Fore.CYAN}{'='*70}{Style.RESET_ALL}\n")

# Get credentials
DB_HOST = os.getenv('DB_HOST', 'localhost')
DB_USER = os.getenv('DB_USER', 'root')
DB_PASSWORD = os.getenv('DB_PASSWORD', '')
DB_NAME = os.getenv('DB_NAME', 'ishuri_connect')

print(f"{Fore.CYAN}Configuration:{Style.RESET_ALL}")
print(f"  Host: {DB_HOST}")
print(f"  User: {DB_USER}")
print(f"  Database: {DB_NAME}\n")

# Step 1: Test connection
print(f"{Fore.CYAN}Step 1:{Style.RESET_ALL} Testing MySQL connection...")
try:
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )
    print(f"{Fore.GREEN}✓ Connection successful!{Style.RESET_ALL}\n")
    conn.close()
except Exception as e:
    print(f"{Fore.RED}✗ Connection failed: {e}{Style.RESET_ALL}")
    print(f"{Fore.YELLOW}Please check your .env file and MySQL server.{Style.RESET_ALL}\n")
    exit(1)

# Step 2: Run schema
print(f"{Fore.CYAN}Step 2:{Style.RESET_ALL} Executing schema.sql...")
try:
    # Read schema file
    with open('sql/schema.sql', 'r', encoding='utf-8') as f:
        schema = f.read()
    
    # Execute schema
    conn = mysql.connector.connect(
        host=DB_HOST,
        user=DB_USER,
        password=DB_PASSWORD
    )
    cursor = conn.cursor()
    
    # Split and execute statements
    statements = schema.split(';')
    for statement in statements:
        if statement.strip():
            try:
                cursor.execute(statement)
            except mysql.connector.Error as err:
                if 'already exists' not in str(err).lower():
                    print(f"{Fore.YELLOW}Warning: {err}{Style.RESET_ALL}")
    
    conn.commit()
    cursor.close()
    conn.close()
    
    print(f"{Fore.GREEN}✓ Schema executed successfully!{Style.RESET_ALL}")
    print(f"{Fore.GREEN}  - Database created{Style.RESET_ALL}")
    print(f"{Fore.GREEN}  - Tables created (students, schools, programs, applications){Style.RESET_ALL}")
    print(f"{Fore.GREEN}  - 10 universities added{Style.RESET_ALL}")
    print(f"{Fore.GREEN}  - 30+ programs added{Style.RESET_ALL}\n")
    
except Exception as e:
    print(f"{Fore.RED}✗ Error executing schema: {e}{Style.RESET_ALL}\n")
    exit(1)

print(f"{Fore.GREEN}{'='*70}{Style.RESET_ALL}")
print(f"{Fore.GREEN}  ✨ Setup complete!{Style.RESET_ALL}")
print(f"{Fore.WHITE}  You can now run: {Fore.CYAN}python main.py{Style.RESET_ALL}")
print(f"{Fore.GREEN}{'='*70}{Style.RESET_ALL}\n")
print(f"{Fore.GREEN}{'='*60}{Style.RESET_ALL}\n")
