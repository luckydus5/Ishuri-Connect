"""
Data Models for Ishuri-Connect
Demonstrates: Classes, Objects, __init__, Methods, Encapsulation
"""


class Student:
    """Student class - represents a student in the system"""
    
    def __init__(self, first_name, last_name, email, marks=None, student_id=None):
        """Initialize a Student object"""
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.marks = marks if marks else []  # Using list
        self.average_mark = self.calculate_average()
    
    def calculate_average(self):
        """Calculate and return average marks - demonstrates function"""
        if not self.marks:
            return 0.0
        return round(sum(self.marks) / len(self.marks), 2)
    
    def get_full_name(self):
        """Return full name - demonstrates method"""
        return f"{self.first_name} {self.last_name}"
    
    def add_mark(self, mark):
        """Add a mark to the student's marks list"""
        if 0 <= mark <= 100:
            self.marks.append(mark)
            self.average_mark = self.calculate_average()
            return True
        return False
    
    def to_dict(self):
        """Convert student object to dictionary - demonstrates dict"""
        return {
            'student_id': self.student_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'average_mark': self.average_mark
        }
    
    def __str__(self):
        """String representation of student"""
        return f"Student: {self.get_full_name()} ({self.email}) - Avg: {self.average_mark}%"


class School:
    """School class - represents a school/university"""
    
    def __init__(self, name, district, courses, min_aggregate, 
                 boarding_type="day", contact_email=None, school_id=None):
        """Initialize a School object"""
        self.school_id = school_id
        self.name = name
        self.district = district
        self.courses = courses  # Using list of courses
        self.min_aggregate = min_aggregate
        self.boarding_type = boarding_type
        self.contact_email = contact_email
        self.capacity = 100  # Maximum students
        self.current_students = 0
    
    def accepts_student(self, average_mark):
        """Check if school accepts student based on marks"""
        return average_mark >= self.min_aggregate
    
    def has_capacity(self):
        """Check if school has available capacity"""
        return self.current_students < self.capacity
    
    def offers_course(self, course_name):
        """Check if school offers a specific course"""
        return course_name.lower() in [c.lower() for c in self.courses]
    
    def get_info(self):
        """Return school information as tuple"""
        return (self.name, self.district, self.min_aggregate, 
                self.boarding_type, self.capacity - self.current_students)
    
    def to_dict(self):
        """Convert school to dictionary"""
        return {
            'school_id': self.school_id,
            'name': self.name,
            'district': self.district,
            'courses': ', '.join(self.courses),
            'min_aggregate': self.min_aggregate,
            'boarding_type': self.boarding_type,
            'contact_email': self.contact_email,
            'available_slots': self.capacity - self.current_students
        }
    
    def __str__(self):
        """String representation of school"""
        return f"{self.name} ({self.district}) - Min: {self.min_aggregate}%"


class Application:
    """Application class - represents a student's application to a school"""
    
    # Class variable - demonstrates class attributes
    STATUS_PENDING = "Pending"
    STATUS_ACCEPTED = "Accepted"
    STATUS_REJECTED = "Rejected"
    STATUS_WITHDRAWN = "Withdrawn"
    
    def __init__(self, student_id, school_id, application_id=None, 
                 status=None, applied_date=None):
        """Initialize an Application object"""
        self.application_id = application_id
        self.student_id = student_id
        self.school_id = school_id
        self.status = status if status else self.STATUS_PENDING
        self.applied_date = applied_date
    
    def is_pending(self):
        """Check if application is pending"""
        return self.status == self.STATUS_PENDING
    
    def accept(self):
        """Accept the application"""
        self.status = self.STATUS_ACCEPTED
    
    def reject(self):
        """Reject the application"""
        self.status = self.STATUS_REJECTED
    
    def withdraw(self):
        """Withdraw the application"""
        self.status = self.STATUS_WITHDRAWN
    
    def get_status_info(self):
        """Return application status as tuple"""
        return (self.application_id, self.status, self.applied_date)
    
    def to_dict(self):
        """Convert application to dictionary"""
        return {
            'application_id': self.application_id,
            'student_id': self.student_id,
            'school_id': self.school_id,
            'status': self.status,
            'applied_date': self.applied_date
        }
    
    def __str__(self):
        """String representation of application"""
        return f"Application #{self.application_id} - Status: {self.status}"


# Utility functions demonstrating function concepts
def validate_email(email):
    """Validate email format - demonstrates function with return value"""
    if '@' in email and '.' in email.split('@')[1]:
        return True
    return False


def calculate_match_score(student_average, school_min, course_match):
    """
    Calculate matching score between student and school
    Demonstrates: function with multiple parameters and calculations
    """
    if student_average < school_min:
        return 0
    
    score = 0
    # Base score from marks difference
    score += min((student_average - school_min) * 2, 50)
    # Course match bonus
    if course_match:
        score += 30
    # Excellence bonus
    if student_average >= 90:
        score += 20
    
    return min(score, 100)  # Cap at 100


def sort_schools_by_match(schools_list, student_average, interested_course):
    """
    Sort schools by match score - demonstrates list operations
    Returns list of tuples (school, score)
    """
    matches = []  # Using list
    
    for school in schools_list:
        if school.accepts_student(student_average):
            course_match = school.offers_course(interested_course)
            score = calculate_match_score(student_average, school.min_aggregate, course_match)
            matches.append((school, score))  # Using tuple
    
    # Sort by score (descending) - demonstrates sorting
    matches.sort(key=lambda x: x[1], reverse=True)
    
    return matches