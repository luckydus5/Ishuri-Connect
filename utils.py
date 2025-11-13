import re


def validate_email(email):
    """Validate email format using simple regex."""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None


def get_marks():
    marks = []
    i = 1
    while True:
        user_input = input(f"Enter marks {i}: ").strip()
        if user_input == "":
            break
        try:
            mark = float(user_input)
            if 0 <= mark <= 100:
                marks.append(mark)
                i += 1
            else:
                print("Please enter a valid mark between 0 and 100.")
        except ValueError:
            print("Invalid input. Please enter a numeric value.")
    return marks


def calculate_average(marks):
    if not marks:
        return 0.0
    total = sum(marks)
    count = len(marks)
    average = total / count
    return round(average, 2)


# "Fake database" of universities
universities = [
    {"name": "University of Rwanda", "course": "Computer Science", "min_mark": 70},
    {"name": "Mount Kenya University", "course": "Business", "min_mark": 55},
    {"name": "AUCA", "course": "Nursing", "min_mark": 60},
    {"name": "ULK", "course": "Law", "min_mark": 65}
]


def recommend_universities(course, average, schools=None):
    """Return universities that offer the given course and accept the student's average mark."""
    if schools is None:
        schools = universities
    
    matched = []
    for uni in schools:
        if uni["course"].lower() == course.lower() and average >= uni["min_mark"]:
            matched.append(uni)
    return matched
