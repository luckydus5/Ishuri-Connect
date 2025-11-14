"""
Data Models for Ishuri-Connect
Demonstrates: Classes, Objects, __init__, Methods, Encapsulation
"""


class Student:
    """Student class - represents a student in the system"""
    
    def __init__(self, first_name, last_name, email, marks=None, student_id=None,
                 secondary_school=None, aggregate_marks=None, subject_combination=None,
                 location_from=None, preferred_location=None, desired_program=None,
                 preferred_boarding='no_preference'):
        """Initialize a Student object with comprehensive profile"""
        self.student_id = student_id
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.marks = marks if marks else []  # Using list
        self.average_mark = self.calculate_average()
        
        # Previous education
        self.secondary_school = secondary_school
        self.aggregate_marks = aggregate_marks if aggregate_marks else self.average_mark
        self.subject_combination = subject_combination  # PCM, PCB, MEG, etc.
        
        # Location preferences
        self.location_from = location_from
        self.preferred_location = preferred_location
        
        # Program preferences
        self.desired_program = desired_program
        self.preferred_boarding = preferred_boarding
    
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
    
    def matches_program(self, program_name):
        """Check if student's desired program matches given program"""
        if not self.desired_program or not program_name:
            return False
        return self.desired_program.lower() in program_name.lower() or program_name.lower() in self.desired_program.lower()
    
    def matches_location(self, school_district, school_province):
        """Calculate location match score (0-20 points)"""
        if not self.preferred_location:
            return 10  # Neutral score if no preference
        
        pref_lower = self.preferred_location.lower()
        # Exact district match
        if school_district and pref_lower == school_district.lower():
            return 20
        # Province match
        if school_province and pref_lower == school_province.lower():
            return 15
        # Partial match (e.g., "Kigali" in "Kigali City")
        if (school_district and pref_lower in school_district.lower()) or \
           (school_province and pref_lower in school_province.lower()):
            return 10
        return 5  # Different location
    
    def to_dict(self):
        """Convert student object to dictionary - demonstrates dict"""
        return {
            'student_id': self.student_id,
            'first_name': self.first_name,
            'last_name': self.last_name,
            'email': self.email,
            'average_mark': self.average_mark,
            'secondary_school': self.secondary_school,
            'aggregate_marks': self.aggregate_marks,
            'subject_combination': self.subject_combination,
            'location_from': self.location_from,
            'preferred_location': self.preferred_location,
            'desired_program': self.desired_program,
            'preferred_boarding': self.preferred_boarding
        }
    
    def __str__(self):
        """String representation of student"""
        combo = f" | {self.subject_combination}" if self.subject_combination else ""
        program = f" | {self.desired_program}" if self.desired_program else ""
        return f"Student: {self.get_full_name()} - Agg: {self.aggregate_marks}%{combo}{program}"


class School:
    """School class - represents a school/university"""
    
    def __init__(self, name, district, courses=None, min_aggregate=0, 
                 boarding_type="day", contact_email=None, school_id=None,
                 province=None, school_type="private", min_cutoff=None, max_cutoff=None,
                 required_subjects=None, competencies_needed=None, website=None):
        """Initialize a School object with comprehensive data"""
        self.school_id = school_id
        self.name = name
        self.district = district
        self.province = province
        self.school_type = school_type
        self.courses = courses if courses else []  # Using list of courses
        self.min_aggregate = min_aggregate
        self.min_cutoff = min_cutoff if min_cutoff else min_aggregate
        self.max_cutoff = max_cutoff if max_cutoff else min_aggregate
        self.boarding_type = boarding_type
        self.contact_email = contact_email
        self.website = website
        
        # Admission requirements
        self.required_subjects = required_subjects if required_subjects else []  # List of acceptable combinations
        self.competencies_needed = competencies_needed if competencies_needed else []
        
        # Capacity
        self.capacity = 100  # Maximum students
        self.current_students = 0
        
        # Programs (list of Program objects or dicts)
        self.programs = []  # Will be populated from database
    
    def accepts_student(self, aggregate_mark):
        """Check if school accepts student based on aggregate marks"""
        return aggregate_mark >= self.min_aggregate
    
    def accepts_combination(self, student_combination):
        """Check if school accepts student's subject combination"""
        if not self.required_subjects or not student_combination:
            return True  # No restriction or no student combination
        
        # Check if student combination is in list of accepted combinations
        return student_combination.upper() in [subj.strip().upper() for subj in self.required_subjects]
    
    def has_program(self, program_name):
        """Check if school offers a specific program"""
        if not program_name:
            return False
        
        program_lower = program_name.lower()
        # Check in programs list
        for program in self.programs:
            if isinstance(program, dict):
                if program_lower in program.get('program_name', '').lower():
                    return True
            else:
                if program_lower in str(program).lower():
                    return True
        
        # Fallback: check in courses list
        return any(program_lower in course.lower() for course in self.courses)
    
    def has_capacity(self):
        """Check if school has available capacity"""
        return self.current_students < self.capacity
    
    def offers_course(self, course_name):
        """Check if school offers a specific course"""
        return course_name.lower() in [c.lower() for c in self.courses]
    
    def get_info(self):
        """Return school information as tuple"""
        return (self.name, self.district, self.province, self.min_aggregate, 
                self.max_cutoff, self.boarding_type)
    
    def get_cutoff_range(self):
        """Return cutoff range as tuple"""
        return (self.min_cutoff, self.max_cutoff)
    
    def to_dict(self):
        """Convert school to dictionary"""
        return {
            'school_id': self.school_id,
            'name': self.name,
            'district': self.district,
            'province': self.province,
            'school_type': self.school_type,
            'min_aggregate': self.min_aggregate,
            'min_cutoff': self.min_cutoff,
            'max_cutoff': self.max_cutoff,
            'boarding_type': self.boarding_type,
            'required_subjects': ', '.join(self.required_subjects) if self.required_subjects else 'Any',
            'competencies': ', '.join(self.competencies_needed) if self.competencies_needed else 'None',
            'contact_email': self.contact_email,
            'website': self.website,
            'programs_count': len(self.programs)
        }
    
    def __str__(self):
        """String representation of school"""
        return f"{self.name} ({self.province}) - Cutoff: {self.min_cutoff}-{self.max_cutoff}%"


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


def calculate_match_score(student, school, program=None):
    """
    Calculate comprehensive matching score between student and school
    Demonstrates: function with multiple parameters and calculations
    
    Scoring breakdown:
    - Marks match: 30 points (student aggregate vs cutoff)
    - Program match: 30 points (desired program offered)
    - Location match: 20 points (preferred location)
    - Subject compatibility: 20 points (combination accepted)
    
    Returns: score (0-100)
    """
    score = 0
    
    # 1. Marks Match (30 points max)
    if student.aggregate_marks >= school.min_cutoff:
        marks_diff = student.aggregate_marks - school.min_cutoff
        # More marks = higher score, cap at 30
        marks_score = min(marks_diff * 1.5, 30)
        score += marks_score
    else:
        return 0  # Doesn't meet minimum requirements
    
    # 2. Program Match (30 points max)
    if student.desired_program:
        if program and student.matches_program(program.get('program_name', '')):
            score += 30  # Exact program match
        elif school.has_program(student.desired_program):
            score += 25  # School offers related program
    else:
        score += 15  # No preference = neutral score
    
    # 3. Location Match (20 points max)
    location_score = student.matches_location(school.district, school.province)
    score += location_score
    
    # 4. Subject Compatibility (20 points max)
    if school.accepts_combination(student.subject_combination):
        score += 20
    else:
        score += 5  # Some partial credit
    
    # Bonus points
    if student.aggregate_marks >= 80:
        score += 5  # Excellence bonus
    
    if student.preferred_boarding != 'no_preference':
        if student.preferred_boarding == school.boarding_type or school.boarding_type == 'both':
            score += 3  # Boarding preference match
    
    return min(score, 100)  # Cap at 100


def sort_schools_by_match(schools_list, student):
    """
    Sort schools by comprehensive match score
    Demonstrates: list operations, sorting, tuple usage
    Returns list of tuples: [(school, score, match_details), ...]
    """
    matches = []  # Using list
    
    for school in schools_list:
        # Basic eligibility check
        if not school.accepts_student(student.aggregate_marks):
            continue  # Skip schools student doesn't qualify for
        
        if not school.accepts_combination(student.subject_combination):
            continue  # Skip if combination not accepted
        
        # Calculate match score
        score = calculate_match_score(student, school)
        
        # Create match details dictionary
        match_details = {
            'marks_qualified': student.aggregate_marks >= school.min_cutoff,
            'program_offered': school.has_program(student.desired_program) if student.desired_program else True,
            'combination_accepted': school.accepts_combination(student.subject_combination),
            'location': school.district
        }
        
        matches.append((school, score, match_details))  # Using tuple
    
    # Sort by score (descending) - demonstrates sorting with lambda
    matches.sort(key=lambda x: x[1], reverse=True)
    
    return matches