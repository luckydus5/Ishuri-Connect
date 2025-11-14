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
    print(Fore.GREEN + "  ✅ " + message + Style.RESET_ALL)


def print_error(message):
    print(Fore.RED + "  ❌ " + message + Style.RESET_ALL)


def print_info(message):
    print(Fore.CYAN + "  ℹ️  " + message + Style.RESET_ALL)


def print_menu(title, options):
    print_header(title)
    print()
    for key, value in options.items():  # Using dictionary
        print(f"  {Fore.YELLOW}{key}.{Style.RESET_ALL} {value}")
    print()


def get_marks_input():
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


def get_subject_combination():
    """
    Get student's subject combination with menu
    Demonstrates: dictionary for menu, lists, user input
    """
    combinations = {
        "1": ("PCM", "Physics-Chemistry-Mathematics"),
        "2": ("PCB", "Physics-Chemistry-Biology"),
        "3": ("MEG", "Mathematics-Economics-Geography"),
        "4": ("HEG", "History-Economics-Geography"),
        "5": ("LKE", "Literature-Kinyarwanda-English"),
        "6": ("MCB", "Mathematics-Chemistry-Biology"),
        "7": ("BCG", "Biology-Chemistry-Geography"),
        "8": ("PEM", "Physics-Economics-Mathematics"),
        "9": ("OTHER", "Other Combination")
    }
    
    print(Fore.CYAN + "\n  📚 Select your subject combination:\n" + Style.RESET_ALL)
    for key, (code, name) in combinations.items():
        print(f"  {Fore.YELLOW}{key}.{Style.RESET_ALL} {code} - {name}")
    
    choice = input(Fore.WHITE + "\n  Your choice: " + Style.RESET_ALL).strip()
    
    if choice in combinations:
        return combinations[choice][0]
    elif choice == "9":
        custom = input(Fore.WHITE + "  Enter your combination (e.g., PCM): " + Style.RESET_ALL).strip().upper()
        return custom if custom else "OTHER"
    return "PCM"  # Default


def get_district_choice():
    """
    Get student's district/province with organized menu
    Demonstrates: nested dictionaries, complex data structures
    """
    districts = {
        "Kigali": ["Kigali City", "Gasabo", "Kicukiro", "Nyarugenge"],
        "Northern": ["Musanze", "Gicumbi", "Burera", "Gakenke", "Rulindo"],
        "Southern": ["Huye", "Nyanza", "Muhanga", "Ruhango", "Nyamagabe", "Nyaruguru", "Gisagara", "Kamonyi"],
        "Eastern": ["Rwamagana", "Nyagatare", "Gatsibo", "Kayonza", "Kirehe", "Ngoma", "Bugesera"],
        "Western": ["Rubavu", "Rusizi", "Nyamasheke", "Karongi", "Rutsiro", "Ngororero", "Nyabihu"]
    }
    
    print(Fore.CYAN + "\n  🌍 Select your province first:\n" + Style.RESET_ALL)
    provinces = list(districts.keys())
    for i, province in enumerate(provinces, 1):
        print(f"  {Fore.YELLOW}{i}.{Style.RESET_ALL} {province}")
    
    try:
        province_choice = int(input(Fore.WHITE + "\n  Province: " + Style.RESET_ALL).strip())
        if 1 <= province_choice <= len(provinces):
            selected_province = provinces[province_choice - 1]
            
            print(Fore.CYAN + f"\n  📍 Select district in {selected_province}:\n" + Style.RESET_ALL)
            district_list = districts[selected_province]
            for i, district in enumerate(district_list, 1):
                print(f"  {Fore.YELLOW}{i}.{Style.RESET_ALL} {district}")
            
            district_choice = int(input(Fore.WHITE + "\n  District: " + Style.RESET_ALL).strip())
            if 1 <= district_choice <= len(district_list):
                return (district_list[district_choice - 1], selected_province)
    except:
        pass
    
    return ("Kigali City", "Kigali")  # Default


def get_boarding_preference():
    """Get student's boarding preference"""
    print(Fore.CYAN + "\n  🏠 Boarding preference:\n" + Style.RESET_ALL)
    print(f"  {Fore.YELLOW}1.{Style.RESET_ALL} Boarding (Live on campus)")
    print(f"  {Fore.YELLOW}2.{Style.RESET_ALL} Day (Commute daily)")
    print(f"  {Fore.YELLOW}3.{Style.RESET_ALL} No preference")
    
    choice = input(Fore.WHITE + "\n  Your choice: " + Style.RESET_ALL).strip()
    
    if choice == "1":
        return "boarding"
    elif choice == "2":
        return "day"
    return "no_preference"


# ==================== STUDENT FUNCTIONS ====================

def register_student(db):
    """
    Register a new student with comprehensive profile
    Demonstrates: Object creation, database INSERT, function with return
    """
    print_header("📝  COMPREHENSIVE STUDENT REGISTRATION")
    
    # Basic information
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
    
    # Previous education
    secondary_school = input("  🏫 Secondary school attended: ").strip()
    
    # Get marks for aggregate calculation
    marks = get_marks_input()
    if not marks:
        print_error("At least one mark is required")
        return None
    
    # Calculate aggregate (can be different from average)
    aggregate_input = input(f"  📊 Aggregate marks (press Enter for calculated {round(sum(marks)/len(marks), 2)}): ").strip()
    if aggregate_input:
        try:
            aggregate_marks = float(aggregate_input)
        except:
            aggregate_marks = round(sum(marks)/len(marks), 2)
    else:
        aggregate_marks = round(sum(marks)/len(marks), 2)
    
    # Subject combination
    subject_combination = get_subject_combination()
    print_success(f"Selected: {subject_combination}")
    
    # Location information
    print(Fore.CYAN + "\n  🌍 Where are you from?" + Style.RESET_ALL)
    location_from, province_from = get_district_choice()
    print_success(f"From: {location_from}, {province_from}")
    
    print(Fore.CYAN + "\n  🎯 Where would you like to study?" + Style.RESET_ALL)
    preferred_location, preferred_province = get_district_choice()
    print_success(f"Preferred: {preferred_location}, {preferred_province}")
    
    # Program interest
    desired_program = input("\n  🎓 What do you want to study (e.g., Computer Science, Medicine): ").strip()
    
    # Boarding preference
    preferred_boarding = get_boarding_preference()
    print_success(f"Boarding preference: {preferred_boarding}")
    
    # Create comprehensive Student object (OOP)
    student = Student(
        first_name=first_name,
        last_name=last_name,
        email=email,
        marks=marks,
        secondary_school=secondary_school,
        aggregate_marks=aggregate_marks,
        subject_combination=subject_combination,
        location_from=location_from,
        preferred_location=preferred_location,
        desired_program=desired_program,
        preferred_boarding=preferred_boarding
    )
    
    # Save to database
    student_id = db.insert_student(student)
    if student_id:
        print_success(f"✅ Registration successful! Student ID: {student_id}")
        print(f"  {Fore.CYAN}Welcome {student.get_full_name()}!{Style.RESET_ALL}")
        print_info(f"Aggregate: {student.aggregate_marks}% | Combination: {student.subject_combination}")
        print_info(f"Looking for: {student.desired_program or 'Any program'}")
        
        # Automatically show recommendations
        print("\n" + "─" * 66)
        get_school_recommendations(db, student)
        input(f"\n  {Fore.CYAN}Press Enter to continue to your dashboard...{Style.RESET_ALL}")
        
        return student
    else:
        print_error("Failed to save student")
        return None


def view_student_profile(db, student):
    """
    Display comprehensive student profile
    Demonstrates: Object methods, string formatting
    """
    print_header("👤  STUDENT PROFILE")
    
    print(f"\n  {Fore.CYAN}Name:{Style.RESET_ALL} {student.get_full_name()}")  # Using method
    print(f"  {Fore.CYAN}Email:{Style.RESET_ALL} {student.email}")
    print(f"  {Fore.CYAN}Student ID:{Style.RESET_ALL} {student.student_id}")
    print(f"  {Fore.CYAN}Aggregate:{Style.RESET_ALL} {student.aggregate_marks}%")
    
    # Educational background
    if student.secondary_school:
        print(f"\n  {Fore.YELLOW}Education:{Style.RESET_ALL}")
        print(f"    Secondary School: {student.secondary_school}")
        print(f"    Combination: {student.subject_combination}")
    
    # Location & preferences
    print(f"\n  {Fore.YELLOW}Preferences:{Style.RESET_ALL}")
    if student.location_from:
        print(f"    From: {student.location_from}")
    if student.preferred_location:
        print(f"    Wants to study in: {student.preferred_location}")
    if student.desired_program:
        print(f"    Desired program: {student.desired_program}")
    print(f"    Boarding: {student.preferred_boarding}")
    
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
        print(f"     📍 Location: {school.district}, {school.province}")
        print(f"     📊 Cutoff Range: {school.min_cutoff}% - {school.max_cutoff}%")
        print(f"     🏠 Boarding: {school.boarding_type}")
        print(f"     📚 Programs: {len(school.programs)}")
        print()
    
    return schools


def get_school_recommendations(db, student):
    """
    Get intelligent personalized school recommendations
    Demonstrates: Complex logic, sorting, tuple usage, multi-criteria matching
    """
    print_header("🎯  INTELLIGENT SCHOOL MATCHING")
    
    print(f"\n  {Fore.CYAN}Your Profile:{Style.RESET_ALL}")
    print(f"  Aggregate: {student.aggregate_marks}%")
    print(f"  Combination: {student.subject_combination}")
    print(f"  Desired Program: {student.desired_program or 'Any'}")
    print(f"  Preferred Location: {student.preferred_location or 'Any'}")
    
    # Get ALL schools that accept the student's marks (ignore location/combination)
    schools = db.get_schools_by_min_mark(student.aggregate_marks)
    
    if not schools:
        print_error(f"No schools accept your aggregate of {student.aggregate_marks}%")
        print_info("The minimum cutoff in our database may be higher than your marks")
        return
    
    # Remove duplicates by school ID
    unique_schools = {}
    for school in schools:
        if school.school_id not in unique_schools:
            unique_schools[school.school_id] = school
    schools = list(unique_schools.values())
    
    # Sort schools: prioritize those offering student's desired program
    if student.desired_program:
        desired_lower = student.desired_program.lower()
        schools_with_program = []
        schools_without_program = []
        
        for school in schools:
            has_desired_program = False
            if school.programs:
                for prog in school.programs:
                    prog_name = prog.get('program_name', '').lower()
                    if desired_lower in prog_name or prog_name in desired_lower:
                        has_desired_program = True
                        break
            
            if has_desired_program:
                schools_with_program.append(school)
            else:
                schools_without_program.append(school)
        
        # Show schools with desired program first, then others
        schools = schools_with_program + schools_without_program
        
        if schools_with_program:
            print(f"\n  {Fore.GREEN}✨ Found {len(schools_with_program)} schools offering '{student.desired_program}':{Style.RESET_ALL}")
            print(f"  {Fore.CYAN}💡 {len(schools_without_program)} other schools also shown below{Style.RESET_ALL}\n")
        else:
            print(f"\n  {Fore.YELLOW}⚠️  No schools offer '{student.desired_program}' in our database{Style.RESET_ALL}")
            print(f"  {Fore.CYAN}💡 Showing {len(schools)} schools you qualify for based on marks:{Style.RESET_ALL}\n")
    else:
        print(f"\n  {Fore.GREEN}✨ Found {len(schools)} schools that accept your marks:{Style.RESET_ALL}\n")
    
    # Display all matching schools sorted by cutoff (highest to lowest)
    for i, school in enumerate(schools[:15], 1):  # Show top 15
        # Color code by how much above cutoff the student is
        marks_above = student.aggregate_marks - school.min_cutoff
        if marks_above >= 15:
            badge = "🌟 Excellent Match"
            color = Fore.GREEN
        elif marks_above >= 5:
            badge = "✅ Good Match"
            color = Fore.YELLOW
        else:
            badge = "📊 Possible"
            color = Fore.WHITE
        
        print(f"  {Fore.CYAN}┌{'─' * 70}┐{Style.RESET_ALL}")
        print(f"  {Fore.CYAN}│{Style.RESET_ALL} {Fore.YELLOW}#{i}. {school.name}{Style.RESET_ALL}" + " " * (68 - len(school.name) - len(str(i)) - 4) + f"{Fore.CYAN}│{Style.RESET_ALL}")
        print(f"  {Fore.CYAN}│{Style.RESET_ALL}    {color}{badge}{Style.RESET_ALL} - Your marks: {student.aggregate_marks}% (Min: {school.min_cutoff}%)" + " " * (10) + f"{Fore.CYAN}│{Style.RESET_ALL}")
        print(f"  {Fore.CYAN}│{Style.RESET_ALL}    📍 {school.district}, {school.province} | 🏠 {school.boarding_type}" + " " * (25) + f"{Fore.CYAN}│{Style.RESET_ALL}")
        
        # Show programs that student qualifies for
        if school.programs:
            qualifying_programs = [p for p in school.programs if student.aggregate_marks >= p.get('cutoff_marks', 0)]
            if qualifying_programs:
                # Sort programs: prioritize student's desired program
                if student.desired_program:
                    desired_lower = student.desired_program.lower()
                    matching_programs = []
                    other_programs = []
                    
                    for prog in qualifying_programs:
                        prog_name = prog.get('program_name', '').lower()
                        if desired_lower in prog_name or prog_name in desired_lower:
                            matching_programs.append(prog)
                        else:
                            other_programs.append(prog)
                    
                    qualifying_programs = matching_programs + other_programs
                
                print(f"  {Fore.CYAN}│{Style.RESET_ALL}" + " " * 70 + f"{Fore.CYAN}│{Style.RESET_ALL}")
                print(f"  {Fore.CYAN}│{Style.RESET_ALL}    {Fore.GREEN}📚 Programs you qualify for:{Style.RESET_ALL}" + " " * 37 + f"{Fore.CYAN}│{Style.RESET_ALL}")
                
                for prog in qualifying_programs[:3]:  # Show top 3 programs
                    prog_name = prog.get('program_name', 'N/A')
                    prog_cutoff = prog.get('cutoff_marks', 0)
                    prog_fees = prog.get('fees_range', 'N/A')
                    prog_duration = prog.get('duration_years', 'N/A')
                    
                    # Check if this is the desired program
                    is_desired = False
                    if student.desired_program:
                        desired_lower = student.desired_program.lower()
                        prog_name_lower = prog_name.lower()
                        if desired_lower in prog_name_lower or prog_name_lower in desired_lower:
                            is_desired = True
                    
                    # Truncate long names
                    display_name = prog_name
                    if len(prog_name) > 35:
                        display_name = prog_name[:32] + "..."
                    
                    # Highlight desired program
                    if is_desired:
                        print(f"  {Fore.CYAN}│{Style.RESET_ALL}       {Fore.YELLOW}⭐ {display_name} (YOUR CHOICE!){Style.RESET_ALL}" + " " * (70 - len(f"       ⭐ {display_name} (YOUR CHOICE!)")) + f"{Fore.CYAN}│{Style.RESET_ALL}")
                    else:
                        print(f"  {Fore.CYAN}│{Style.RESET_ALL}       • {display_name}" + " " * (70 - len(f"       • {display_name}")) + f"{Fore.CYAN}│{Style.RESET_ALL}")
                    
                    print(f"  {Fore.CYAN}│{Style.RESET_ALL}         Cutoff: {prog_cutoff}% | Duration: {prog_duration}yrs | Fees: {prog_fees}" + " " * (5) + f"{Fore.CYAN}│{Style.RESET_ALL}")
                    prog_cutoff = prog.get('cutoff_marks', 0)
                    prog_fees = prog.get('fees_range', 'N/A')
                    prog_duration = prog.get('duration_years', 'N/A')
                    
                    # Truncate long names
                    if len(prog_name) > 35:
                        prog_name = prog_name[:32] + "..."
                    
                    print(f"  {Fore.CYAN}│{Style.RESET_ALL}       • {prog_name}" + " " * (70 - len(f"       • {prog_name}")) + f"{Fore.CYAN}│{Style.RESET_ALL}")
                    print(f"  {Fore.CYAN}│{Style.RESET_ALL}         Cutoff: {prog_cutoff}% | Duration: {prog_duration}yrs | Fees: {prog_fees}" + " " * (5) + f"{Fore.CYAN}│{Style.RESET_ALL}")
        
        print(f"  {Fore.CYAN}└{'─' * 70}┘{Style.RESET_ALL}\n")
    
    print(f"\n  {Fore.GREEN}✨ All schools listed accept your aggregate of {student.aggregate_marks}%!{Style.RESET_ALL}")
    print(f"  {Fore.CYAN}💡 Tip: Programs with higher cutoffs are more competitive{Style.RESET_ALL}\n")


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
        "1": "Signup Student",
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
