

from colorama import init, Fore, Style
from src.cli import start_application

# Initialize colorama for Windows compatibility
init(autoreset=True)


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
    print_welcome_banner()
    
    start_application()


if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n" + Fore.YELLOW + "  👋 Goodbye! Thank you for using Ishuri Connect.\n" + Style.RESET_ALL)
    except Exception as e:
        print("\n" + Fore.RED + f"  ❌ An unexpected error occurred: {e}" + Style.RESET_ALL)
        print(Fore.CYAN + "  💡 Please try again or contact support." + Style.RESET_ALL)