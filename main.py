"""
Ishuri-Connect - Main Entry Point
Auto-initializes database on first run
Demonstrates: Program structure, imports, main function, database setup
"""

from colorama import init, Fore, Style
from cli import start_application
import mysql.connector
import os
from dotenv import load_dotenv

# Initialize colorama for Windows compatibility
init(autoreset=True)

# Load environment variables
load_dotenv()


def check_and_setup_database():
    """
    Check if database exists and set it up automatically if needed
    Demonstrates: MySQL operations, file reading, error handling
    """
    DB_HOST = os.getenv('DB_HOST', 'localhost')
    DB_USER = os.getenv('DB_USER', 'root')
    DB_PASSWORD = os.getenv('DB_PASSWORD', '')
    DB_NAME = os.getenv('DB_NAME', 'ishuri_connect')
    
    try:
        # Check if database and tables exist
        conn = mysql.connector.connect(
            host=DB_HOST,
            user=DB_USER,
            password=DB_PASSWORD
        )
        cursor = conn.cursor()
        cursor.execute(f"SHOW DATABASES LIKE '{DB_NAME}'")
        db_exists = cursor.fetchone() is not None
        
        # Check if tables exist
        tables_exist = False
        if db_exists:
            cursor.execute(f"USE {DB_NAME}")
            cursor.execute("SHOW TABLES LIKE 'students'")
            students_table = cursor.fetchone() is not None
            cursor.execute("SHOW TABLES LIKE 'applications'")
            applications_table = cursor.fetchone() is not None
            tables_exist = students_table and applications_table
        
        if not db_exists or not tables_exist:
            print(f"\n{Fore.YELLOW}⚙️  First time setup: Creating database and tables...{Style.RESET_ALL}")
            
            # Read and execute schema
            with open('sql/schema.sql', 'r', encoding='utf-8') as f:
                schema = f.read()
            
            # Split by semicolon and execute each statement
            statements = [s.strip() for s in schema.split(';') if s.strip()]
            
            for statement in statements:
                try:
                    cursor.execute(statement)
                    conn.commit()
                except mysql.connector.Error as err:
                    # Ignore "already exists" errors
                    if 'already exists' not in str(err).lower():
                        print(f"{Fore.YELLOW}Warning: {err}{Style.RESET_ALL}")
            
            print(f"{Fore.GREEN}✓ Database setup complete!{Style.RESET_ALL}")
            print(f"{Fore.GREEN}  - 10 universities loaded{Style.RESET_ALL}")
            print(f"{Fore.GREEN}  - 30+ programs available{Style.RESET_ALL}\n")
        
        cursor.close()
        conn.close()
        return True
        
    except mysql.connector.Error as e:
        print(f"\n{Fore.RED}❌ Database Error: {e}{Style.RESET_ALL}")
        print(f"{Fore.YELLOW}Please check your .env file:{Style.RESET_ALL}")
        print(f"  DB_HOST={DB_HOST}")
        print(f"  DB_USER={DB_USER}")
        print(f"  DB_NAME={DB_NAME}")
        print(f"\n{Fore.YELLOW}Make sure MySQL is running and credentials are correct.{Style.RESET_ALL}\n")
        return False


def print_welcome_banner():
    """Print welcome banner - demonstrates function"""
    print("\n" + Fore.CYAN + "╔" + "═" * 68 + "╗")
    print(Fore.CYAN + "║" + " " * 68 + "║")
    print(Fore.CYAN + "║" + Fore.YELLOW + Style.BRIGHT + "        🎓  ISHURI CONNECT - School Matching Platform  🎓" + Fore.CYAN + "        ║")
    print(Fore.CYAN + "║" + " " * 68 + "║")
    print(Fore.CYAN + "╚" + "═" * 68 + "╝" + Style.RESET_ALL)
    
    print("\n" + Fore.GREEN + "  Welcome to Ishuri Connect!" + Style.RESET_ALL)
    print("  " + Fore.WHITE + "Find the perfect school that matches your academic profile." + Style.RESET_ALL)
    print("\n" + Fore.MAGENTA + "  💡 Tip: " + Style.RESET_ALL + "Press " + Fore.RED + "Ctrl+C" + Style.RESET_ALL + " at any time to exit.")
    print(Fore.CYAN + "  " + "─" * 66 + Style.RESET_ALL)


def main():
    """
    Main function - entry point
    Demonstrates: Main program structure, function calls
    """
    print_welcome_banner()
    
    # Auto-setup database on first run
    if not check_and_setup_database():
        return
    
    start_application()


if __name__ == "__main__":
    """
    Entry point when script is run directly
    Demonstrates: Python __main__ pattern
    """
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n" + Fore.YELLOW + "  👋 Goodbye! Thank you for using Ishuri Connect.\n" + Style.RESET_ALL)
    except Exception as e:
        print("\n" + Fore.RED + f"  ❌ An unexpected error occurred: {e}" + Style.RESET_ALL)
        print(Fore.CYAN + "  💡 Please try again or contact support." + Style.RESET_ALL)