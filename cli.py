from utils import get_marks, calculate_average, validate_email, recommend_universities
from colorama import Fore, Back, Style

def print_section_header(title):
    """Print a section header with styling."""
    print("\n" + Fore.CYAN + "  ┌─" + "─" * 64 + "┐")
    print(Fore.CYAN + "  │ " + Fore.WHITE + Style.BRIGHT + title.ljust(64) + Fore.CYAN + "│")
    print(Fore.CYAN + "  └─" + "─" * 64 + "┘" + Style.RESET_ALL)

def print_success_box(message):
    """Print a success message in a box."""
    lines = message.split('\n')
    max_len = max(len(line) for line in lines)
    print("\n" + Fore.GREEN + "  ┌─" + "─" * (max_len + 2) + "┐")
    for line in lines:
        print(Fore.GREEN + "  │ " + Style.BRIGHT + line.ljust(max_len) + Style.NORMAL + " │")
    print(Fore.GREEN + "  └─" + "─" * (max_len + 2) + "┘" + Style.RESET_ALL)

def print_error(message):
    """Print an error message."""
    print(Fore.RED + "  ❌ " + message + Style.RESET_ALL)

def print_info(message):
    """Print an info message."""
    print(Fore.CYAN + "  ℹ️  " + message + Style.RESET_ALL)

def student_registration():
    try:
        print_section_header("📝  STUDENT REGISTRATION")

        print("\n" + Fore.YELLOW + "  Please provide your details below:" + Style.RESET_ALL + "\n")
        
        first_name = input(Fore.WHITE + "  👤 First name: " + Style.RESET_ALL).strip()
        if not first_name:
            print_error("First name cannot be empty.")
            return
        
        last_name = input(Fore.WHITE + "  👤 Last name: " + Style.RESET_ALL).strip()
        if not last_name:
            print_error("Last name cannot be empty.")
            return
        
        email = input(Fore.WHITE + "  📧 Email address: " + Style.RESET_ALL).strip()
        if not validate_email(email):
            print_error("Invalid email format. Please provide a valid email address.")
            return
        
        course = input(Fore.WHITE + "  📚 Course interest: " + Style.RESET_ALL).strip()
        if not course:
            print_error("Course cannot be empty.")
            return

        print("\n" + Fore.GREEN + "  ✅ Thank you " + Style.BRIGHT + f"{first_name} {last_name}" + Style.NORMAL + "!" + Style.RESET_ALL)
        print(Fore.CYAN + "  📊 Now enter your marks (press Enter without typing to finish):" + Style.RESET_ALL + "\n")
        
        marks = get_marks()

        if not marks:
            print_error("No marks were entered. Registration cannot proceed.")
            return
        
        average = calculate_average(marks)
        
        # Success message
        success_msg = f"✨ Registration Successful! ✨\n" \
                     f"Welcome {first_name} {last_name}!\n" \
                     f"📊 Your Average: {average:.2f}%"
        print_success_box(success_msg)
        
        # Show recommendations
        print_section_header(f"🎯  SCHOOL RECOMMENDATIONS FOR {course.upper()}")
        print(Fore.CYAN + "\n  🔍 Searching for matching schools..." + Style.RESET_ALL)
        
        recommendations = recommend_universities(course, average)
        
        if recommendations:
            print(Fore.GREEN + f"\n  ✨ Found {len(recommendations)} school(s) that match your profile!\n" + Style.RESET_ALL)
            
            for idx, school in enumerate(recommendations, 1):
                print(Fore.CYAN + "  ┌─" + "─" * 60 + "┐")
                print(Fore.CYAN + "  │ " + Fore.YELLOW + Style.BRIGHT + f"{idx}. {school['name']}" + Style.RESET_ALL + " " * (58 - len(school['name'])) + Fore.CYAN + "│")
                print(Fore.CYAN + "  │    " + Fore.WHITE + f"📌 Required minimum: " + Fore.YELLOW + f"{school['min_mark']}%" + " " * (47 - len(str(school['min_mark']))) + Fore.CYAN + "│")
                print(Fore.CYAN + "  │    " + Fore.WHITE + f"✅ Your average:     " + Fore.GREEN + f"{average:.2f}%" + " " * (47 - len(f"{average:.2f}")) + Fore.CYAN + "│")
                print(Fore.CYAN + "  └─" + "─" * 60 + "┘" + Style.RESET_ALL)
                print()
        else:
            print(Fore.YELLOW + f"\n  ⚠️  No schools found for '{course}' with average {average:.2f}%" + Style.RESET_ALL)
            print(Fore.CYAN + "  💡 Tip: Try exploring other courses or improving your marks.\n" + Style.RESET_ALL)
    
    except KeyboardInterrupt:
        print("\n\n" + Fore.YELLOW + "  ⚠️  Registration cancelled by user." + Style.RESET_ALL)
    except Exception as e:
        print("\n" + Fore.RED + f"  ❌ An error occurred: {e}" + Style.RESET_ALL)
        print(Fore.CYAN + "  💡 Please try again or contact support." + Style.RESET_ALL)