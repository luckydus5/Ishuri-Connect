
from cli import student_registration
from colorama import init, Fore, Back, Style

# Initialize colorama for Windows compatibility
init(autoreset=True)

def print_header():
    """Print a beautiful header with colors."""
    print("\n" + Fore.CYAN + "╔" + "═" * 68 + "╗")
    print(Fore.CYAN + "║" + "" * 68 + "║")
    print(Fore.CYAN + "║" + Fore.YELLOW + Style.BRIGHT + "        🎓  ISHURI CONNECT - School Matching Platform  🎓" + Fore.CYAN + "        ║")
    print(Fore.CYAN + "║" + " " * 68 + "║")
    print(Fore.CYAN + "╚" + "═" * 68 + "╝" + Style.RESET_ALL)

def print_welcome():
    """Print welcome message."""
    print("\n" + Fore.GREEN + "  Welcome! " + Style.RESET_ALL + "This platform helps students find schools")
    print("  that match their " + Fore.YELLOW + "academic profile" + Style.RESET_ALL + " and " + Fore.YELLOW + "interests" + Style.RESET_ALL + ".")
    print("\n" + Fore.MAGENTA + "  💡 Tip: " + Style.RESET_ALL + "Press " + Fore.RED + "Ctrl+C" + Style.RESET_ALL + " at any time to exit.")
    print(Fore.CYAN + "\n  " + "─" * 66 + Style.RESET_ALL)

def print_footer():
    """Print goodbye footer."""
    print("\n" + Fore.CYAN + "  " + "─" * 66)
    print(Fore.GREEN + Style.BRIGHT + "  ✨ Thank you for using Ishuri Connect! ✨" + Style.RESET_ALL)
    print(Fore.CYAN + "  " + "─" * 66 + "\n" + Style.RESET_ALL)

def main():
    print_header()
    print_welcome()
    student_registration()
    print_footer()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n" + Fore.YELLOW + "  👋 Goodbye! See you next time.\n" + Style.RESET_ALL)