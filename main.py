
from cli import student_registration

def main():
    print("\n" + "="*50)
    print("    ISHURI CONNECT - School Matching Platform")
    print("="*50)
    print("\nWelcome! This platform helps students find schools")
    print("that match their academic profile and interests.")
    print("\nPress Ctrl+C at any time to exit.\n")
    print("="*50)
    
    student_registration()
    
    print("\n" + "="*50)
    print("Thank you for using Ishuri Connect!")
    print("="*50 + "\n")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\nGoodbye!\n")