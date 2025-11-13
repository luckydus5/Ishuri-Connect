"""
Enhanced CLI for Ishuri-Connect
Demonstrates: Functions, Menu systems, User interaction, Lists, Dictionaries
"""

from colorama import Fore, Style, init
from utils import validate_email
from models import Student, School, Application, sort_schools_by_match
from db import Database

# Initialize colorama
init(autoreset=True)


# ==================== DISPLAY FUNCTIONS ====================

def print_header(title):
    """Print section header - demonstrates function"""
    print("\n" + Fore.CYAN + "  ┌─" + "─" * 64 + "┐")
    print(Fore.CYAN + "  │ " + Fore.WHITE + Style.BRIGHT + title.ljust(64) + Fore.CYAN + "│")
    print(Fore.CYAN + "  └─" + "─" * 64 + "┘" + Style.RESET_ALL)


def print_success(message):
    """Print success message"""
    print(Fore.GREEN + "  ✅ " + message + Style.RESET_ALL)


def print_error(message):
    """Print error message"""
    print(Fore.RED + "  ❌ " + message + Style.RESET_ALL)


def print_info(message):
    """Print info message"""
    print(Fore.CYAN + "  ℹ️  " + message + Style.RESET_ALL)


def print_menu(title, options):
    """
    Print menu with options
    Demonstrates: function with list parameter
    """
    print_header(title)
    print()
    for key, value in options.items():  # Using dictionary
        print(f"  {Fore.YELLOW}{key}.{Style.RESET_ALL} {value}")
    print()


def get_marks_input():
    """
    Get marks from user
    Demonstrates: list operations, while loop, input validation
    """
    marks = []  # Using list
    print(Fore.CYAN + "\n  📊 Enter your marks (press Enter to finish):\n" + Style.RESET_ALL)
    
    i = 1
    while True:
        try:
            mark_input = input(Fore.WHITE + f"  📝 Mark #{i}: " + Style.RESET_ALL).strip()
            if mark_input == "":
                break
            
            mark = float(mark_input)
            if 0 <= mark <= 100:
                marks.append(mark)  # List operation
                print(Fore.GREEN + f"     ✓ Added: {mark}%" + Style.RESET_ALL)
                i += 1
            else:
                print(Fore.RED + "     ✗ Mark must be between 0-100" + Style.RESET_ALL)
        except ValueError:
            print(Fore.RED + "     ✗ Invalid number" + Style.RESET_ALL)
    
    return marks


# ==================== STUDENT FUNCTIONS ====================

def register_student(db):
    """
    Register a new student
    Demonstrates: Object creation, database INSERT, function with return
    """
    print_header("📝  STUDENT REGISTRATION")
    
    # Get student information
    first_name = input("\n  👤 First name: ").strip()
    if not first_name:
        print_error("First name is required")
        return None
    
    last_name = input("  👤 Last name: ").strip()
    if not last_name:
        print_error("Last name is required")
        return None
    
    email = input("  📧 Email: ").strip()
    if not validate_email(email):  # Using function
        print_error("Invalid email format")
        return None
    
    # Check if email exists
    existing = db.get_student_by_email(email)
    if existing:
        print_error("Email already registered")
        return existing
    
    # Get marks
    marks = get_marks_input()
    if not marks:
        print_error("At least one mark is required")
        return None
    
    # Create Student object (OOP)
    student = Student(first_name, last_name, email, marks)
    
    # Save to database
    student_id = db.insert_student(student)
    if student_id:
        print_success(f"Registration successful! Student ID: {student_id}")
        print_info(f"Average mark: {student.average_mark}%")
        return student
    else:
        print_error("Failed to save student")
        return None


def view_student_profile(db, student):
    """
    Display student profile
    Demonstrates: Object methods, string formatting
    """
    print_header("👤  STUDENT PROFILE")
    
    print(f"\n  {Fore.CYAN}Name:{Style.RESET_ALL} {student.get_full_name()}")  # Using method
    print(f"  {Fore.CYAN}Email:{Style.RESET_ALL} {student.email}")
    print(f"  {Fore.CYAN}Average Mark:{Style.RESET_ALL} {student.average_mark}%")
    print(f"  {Fore.CYAN}Total Marks:{Style.RESET_ALL} {len(student.marks)}")  # Using list
    
    # Display marks if available
    if student.marks:
        print(f"\n  {Fore.YELLOW}Individual Marks:{Style.RESET_ALL}")
        for i, mark in enumerate(student.marks, 1):  # List iteration
            print(f"    {i}. {mark}%")


# ==================== SCHOOL FUNCTIONS ====================

def view_all_schools(db):
    """
    Display all schools
    Demonstrates: List operations, for loop
    """
    print_header("🏫  AVAILABLE SCHOOLS")
    
    schools = db.get_all_schools()  # Returns list of objects
    
    if not schools:
        print_info("No schools available")
        return schools
    
    print(f"\n  {Fore.GREEN}Found {len(schools)} schools:{Style.RESET_ALL}\n")
    
    for i, school in enumerate(schools, 1):  # List enumeration
        print(f"  {Fore.YELLOW}{i}. {school.name}{Style.RESET_ALL}")
        print(f"     📍 District: {school.district}")
        print(f"     📊 Minimum: {school.min_aggregate}%")
        print(f"     🏠 Type: {school.boarding_type}")
        print()
    
    return schools


def get_school_recommendations(db, student):
    """
    Get personalized school recommendations
    Demonstrates: Complex logic, sorting, tuple usage
    """
    print_header("🎯  PERSONALIZED RECOMMENDATIONS")
    
    # Get course interest
    course = input("\n  📚 Enter your course interest: ").strip()
    if not course:
        print_error("Course is required")
        return
    
    # Get all qualifying schools
    schools = db.get_schools_by_min_mark(student.average_mark)
    
    if not schools:
        print_error(f"No schools accept average of {student.average_mark}%")
        return
    
    # Sort by match score
    matches = sort_schools_by_match(schools, student.average_mark, course)
    
    if not matches:
        print_info("No matching schools found")
        return
    
    print(f"\n  {Fore.GREEN}✨ Found {len(matches)} matching schools!{Style.RESET_ALL}\n")
    
    # Display recommendations with scores
    for i, (school, score) in enumerate(matches, 1):  # Tuple unpacking
        print(f"  {Fore.CYAN}┌{'─' * 62}┐{Style.RESET_ALL}")
        print(f"  {Fore.CYAN}│{Style.RESET_ALL} {Fore.YELLOW}{i}. {school.name}{Style.RESET_ALL}" + " " * (60 - len(school.name)) + f"{Fore.CYAN}│{Style.RESET_ALL}")
        print(f"  {Fore.CYAN}│{Style.RESET_ALL}    📍 {school.district} | 📊 Min: {school.min_aggregate}% | 🎯 Match: {score}%" + " " * (60 - len(f"    📍 {school.district} | 📊 Min: {school.min_aggregate}% | 🎯 Match: {score}%")) + f" {Fore.CYAN}│{Style.RESET_ALL}")
        print(f"  {Fore.CYAN}└{'─' * 62}┘{Style.RESET_ALL}\n")
    
    return matches


# ==================== APPLICATION FUNCTIONS ====================

def apply_to_school(db, student):
    """
    Submit application to a school
    Demonstrates: Object creation, database operations
    """
    print_header("📋  APPLY TO SCHOOL")
    
    # Show schools
    schools = db.get_schools_by_min_mark(student.average_mark)
    
    if not schools:
        print_error("No schools available for your marks")
        return
    
    # Display schools
    print(f"\n  {Fore.GREEN}Schools you qualify for:{Style.RESET_ALL}\n")
    for i, school in enumerate(schools, 1):
        print(f"  {i}. {school.name} (Min: {school.min_aggregate}%)")
    
    # Get choice
    try:
        choice = int(input(f"\n  Select school (1-{len(schools)}): "))
        if 1 <= choice <= len(schools):
            selected_school = schools[choice - 1]  # List indexing
            
            # Check existing application
            if db.check_existing_application(student.student_id, selected_school.school_id):
                print_error("You already applied to this school")
                return
            
            # Create Application object
            application = Application(student.student_id, selected_school.school_id)
            
            # Save to database
            app_id = db.insert_application(application)
            if app_id:
                print_success(f"Application submitted successfully!")
                print_info(f"Application ID: {app_id}")
                print_info(f"School: {selected_school.name}")
                print_info("Status: Pending")
            else:
                print_error("Failed to submit application")
        else:
            print_error("Invalid choice")
    except ValueError:
        print_error("Invalid input")


def view_my_applications(db, student):
    """
    View student's applications
    Demonstrates: Database JOIN, list operations, dictionary
    """
    print_header("📋  MY APPLICATIONS")
    
    applications = db.get_applications_by_student(student.student_id)
    
    if not applications:
        print_info("You haven't applied to any schools yet")
        return
    
    print(f"\n  {Fore.GREEN}Your Applications:{Style.RESET_ALL}\n")
    
    # Count by status using dictionary
    status_count = {}
    for app in applications:
        status = app.status
        status_count[status] = status_count.get(status, 0) + 1
    
    # Display each application
    for i, app in enumerate(applications, 1):
        school = db.get_school_by_id(app.school_id)
        
        # Color based on status
        if app.status == "Accepted":
            color = Fore.GREEN
            icon = "✅"
        elif app.status == "Rejected":
            color = Fore.RED
            icon = "❌"
        elif app.status == "Pending":
            color = Fore.YELLOW
            icon = "⏳"
        else:
            color = Fore.WHITE
            icon = "📋"
        
        print(f"  {color}{icon} Application #{app.application_id}{Style.RESET_ALL}")
        if school:
            print(f"     School: {school.name}")
        print(f"     Status: {color}{app.status}{Style.RESET_ALL}")
        print(f"     Applied: {app.applied_date}")
        print()
    
    # Show summary
    print(f"  {Fore.CYAN}Summary:{Style.RESET_ALL}")
    for status, count in status_count.items():  # Dictionary iteration
        print(f"    {status}: {count}")


# ==================== STATISTICS FUNCTIONS ====================

def view_statistics(db):
    """
    Display system statistics
    Demonstrates: Dictionary operations, formatted output
    """
    print_header("📊  SYSTEM STATISTICS")
    
    stats = db.get_statistics()  # Returns dictionary
    
    print(f"\n  {Fore.CYAN}{'─' * 60}{Style.RESET_ALL}")
    print(f"  {Fore.YELLOW}Total Students:{Style.RESET_ALL}        {stats['total_students']}")
    print(f"  {Fore.YELLOW}Total Schools:{Style.RESET_ALL}         {stats['total_schools']}")
    print(f"  {Fore.YELLOW}Total Applications:{Style.RESET_ALL}    {stats['total_applications']}")
    print(f"  {Fore.YELLOW}Pending Applications:{Style.RESET_ALL}  {stats['pending_applications']}")
    print(f"  {Fore.CYAN}{'─' * 60}{Style.RESET_ALL}\n")


# ==================== MAIN MENU SYSTEM ====================

def student_menu(db, student):
    """
    Student menu system
    Demonstrates: While loop, dictionary for menu, function calls
    """
    menu_options = {  # Using dictionary for menu
        "1": "View My Profile",
        "2": "View All Schools",
        "3": "Get Recommendations",
        "4": "Apply to School",
        "5": "View My Applications",
        "6": "View Statistics",
        "0": "Logout"
    }
    
    while True:
        print_menu(f"👤 STUDENT MENU - Welcome {student.get_full_name()}!", menu_options)
        
        choice = input(f"  {Fore.YELLOW}Choose an option: {Style.RESET_ALL}").strip()
        
        if choice == "1":
            view_student_profile(db, student)
        elif choice == "2":
            view_all_schools(db)
        elif choice == "3":
            get_school_recommendations(db, student)
        elif choice == "4":
            apply_to_school(db, student)
        elif choice == "5":
            view_my_applications(db, student)
        elif choice == "6":
            view_statistics(db)
        elif choice == "0":
            print_success("Logged out successfully!")
            break
        else:
            print_error("Invalid option")
        
        input(f"\n  {Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")


def main_menu(db):
    """
    Main menu - entry point
    Demonstrates: Menu system, while loop, function organization
    """
    menu_options = {
        "1": "Register New Student",
        "2": "Login (Existing Student)",
        "3": "View All Schools",
        "4": "View Statistics",
        "0": "Exit"
    }
    
    while True:
        print_menu("🏠 MAIN MENU", menu_options)
        
        choice = input(f"  {Fore.YELLOW}Choose an option: {Style.RESET_ALL}").strip()
        
        if choice == "1":
            student = register_student(db)
            if student:
                student_menu(db, student)
        
        elif choice == "2":
            email = input("\n  📧 Enter your email: ").strip()
            student = db.get_student_by_email(email)
            if student:
                print_success("Login successful!")
                student_menu(db, student)
            else:
                print_error("Student not found")
        
        elif choice == "3":
            view_all_schools(db)
            input(f"\n  {Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")
        
        elif choice == "4":
            view_statistics(db)
            input(f"\n  {Fore.CYAN}Press Enter to continue...{Style.RESET_ALL}")
        
        elif choice == "0":
            print_success("Thank you for using Ishuri Connect! Goodbye! 👋")
            break
        
        else:
            print_error("Invalid option")


def start_application():
    """
    Start the application
    Demonstrates: Function as entry point, error handling
    """
    # Connect to database
    db = Database()
    if not db.connect():
        print_error("Failed to connect to database!")
        print_info("Please check your .env configuration")
        return
    
    print_success("Database connected successfully!")
    
    try:
        main_menu(db)
    except KeyboardInterrupt:
        print("\n\n" + Fore.YELLOW + "  👋 Goodbye!" + Style.RESET_ALL)
    finally:
        db.disconnect()
