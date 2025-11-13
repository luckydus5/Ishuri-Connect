from utils import get_marks, calculate_average, validate_email, recommend_universities

def student_registration():
    try:
        print("\n === Student Registration Process Initiated. =======\n")

        first_name = input("Enter your first name: ").strip()
        if not first_name:
            print("First name cannot be empty.")
            return
        
        last_name = input("Enter your last name: ").strip()
        if not last_name:
            print("Last name cannot be empty.")
            return
        
        email = input("Enter your email address: ").strip()
        if not validate_email(email):
            print("Invalid email format. Please provide a valid email address.")
            return
        
        course = input("Which course are you interested in? ").strip()
        if not course:
            print("Course cannot be empty.")
            return

        print(f"\nThank you {first_name} {last_name} for registering with email: {email}")
        print("Now enter your marks (press Enter without typing to finish):\n")
        marks = get_marks()

        if not marks:
            print("\nNo marks were entered. Registration cannot proceed.")
            return
        
        average = calculate_average(marks)
        print("\n" + "="*50)
        print("Registration Successful!")
        print(f"Welcome to Ishuri Connect, {first_name} {last_name}!")
        print(f"Your average marks: {average:.2f}")
        print("="*50)
        
        # Show recommendations
        print(f"\nSearching for schools offering {course}...\n")
        recommendations = recommend_universities(course, average)
        
        if recommendations:
            print(f"Found {len(recommendations)} school(s) that match your profile:\n")
            for idx, school in enumerate(recommendations, 1):
                print(f"{idx}. {school['name']}")
                print(f"   Required minimum: {school['min_mark']}%")
                print(f"   Your average: {average:.2f}%")
                print()
        else:
            print(f"Unfortunately, no schools were found for '{course}' with your average mark.")
            print("You may want to explore other courses or improve your marks.\n")
    
    except KeyboardInterrupt:
        print("\n\nRegistration cancelled by user. Goodbye!")
    except Exception as e:
        print(f"\nAn error occurred: {e}")
        print("Please try again or contact support.")