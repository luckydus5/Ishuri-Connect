"""
Database Operations for Ishuri-Connect
Demonstrates: MySQL connections, CRUD operations, Functions, Error handling
"""

import mysql.connector
from mysql.connector import Error
from typing import Optional, List, Dict, Any
import os
from dotenv import load_dotenv
from models import Student, School, Application

# Load environment variables
load_dotenv()


class Database:
    """Database class - handles all MySQL operations"""
    
    def __init__(self):
        """Initialize database connection parameters"""
        self.host = os.getenv('DB_HOST', 'localhost')
        self.user = os.getenv('DB_USER', 'root')
        self.password = os.getenv('DB_PASSWORD', '')
        self.database = os.getenv('DB_NAME', 'ishuri_connect')
        self.connection: Optional[Any] = None
    
    def connect(self):
        """Establish database connection - demonstrates function"""
        try:
            self.connection = mysql.connector.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                database=self.database
            )
            if self.connection.is_connected():
                return True
        except Error as e:
            print(f"Error connecting to MySQL: {e}")
            return False
    
    def disconnect(self):
        """Close database connection"""
        if self.connection and self.connection.is_connected():
            self.connection.close()
    
    def execute_query(self, query, params=None):
        """
        Execute a query (INSERT, UPDATE, DELETE)
        Demonstrates: function with parameters, tuple usage
        """
        try:
            cursor = self.connection.cursor()
            if params:
                cursor.execute(query, params)  # Using tuple for params
            else:
                cursor.execute(query)
            self.connection.commit()
            return cursor.lastrowid if cursor.lastrowid else True
        except Error as e:
            print(f"Error executing query: {e}")
            return None
        finally:
            cursor.close()
    
    def fetch_query(self, query, params=None) -> List[Dict[str, Any]]:
        """
        Fetch data from database
        Demonstrates: function returning lists/tuples
        """
        try:
            if self.connection is None:
                return []
            cursor = self.connection.cursor(dictionary=True)
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            results = cursor.fetchall()  # Returns list of dictionaries
            return results  # type: ignore
        except Error as e:
            print(f"Error fetching data: {e}")
            return []
        finally:
            if 'cursor' in locals():
                cursor.close()
    
    # ==================== STUDENT OPERATIONS ====================
    
    def insert_student(self, student):
        """
        Insert a new student into database with comprehensive profile
        Demonstrates: INSERT operation, using object attributes
        """
        query = """
        INSERT INTO students (first_name, last_name, email, average_mark, aggregate_marks,
                             secondary_school, subject_combination, location_from, 
                             preferred_location, desired_program, preferred_boarding)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            student.first_name, student.last_name, student.email, 
            student.average_mark, student.aggregate_marks,
            student.secondary_school, student.subject_combination,
            student.location_from, student.preferred_location,
            student.desired_program, student.preferred_boarding
        )
        
        student_id = self.execute_query(query, params)
        if student_id:
            student.student_id = student_id
            return student_id
        return None
    
    def get_student_by_id(self, student_id):
        """
        Get student by ID - demonstrates SELECT operation
        Returns: Student object or None
        """
        query = "SELECT * FROM students WHERE id = %s"
        results = self.fetch_query(query, (student_id,))
        
        if results:
            data = results[0]  # Getting first element from list
            return Student(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                student_id=data['id'],
                secondary_school=data.get('secondary_school'),
                aggregate_marks=float(data.get('aggregate_marks', 0)),
                subject_combination=data.get('subject_combination'),
                location_from=data.get('location_from'),
                preferred_location=data.get('preferred_location'),
                desired_program=data.get('desired_program'),
                preferred_boarding=data.get('preferred_boarding', 'no_preference')
            )
        return None
    
    def get_student_by_email(self, email):
        """Get student by email"""
        query = "SELECT * FROM students WHERE email = %s"
        results = self.fetch_query(query, (email,))
        
        if results:
            data = results[0]
            return Student(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                student_id=data['id'],
                secondary_school=data.get('secondary_school'),
                aggregate_marks=float(data.get('aggregate_marks', 0)),
                subject_combination=data.get('subject_combination'),
                location_from=data.get('location_from'),
                preferred_location=data.get('preferred_location'),
                desired_program=data.get('desired_program'),
                preferred_boarding=data.get('preferred_boarding', 'no_preference')
            )
        return None
    
    def get_all_students(self):
        """
        Get all students - demonstrates fetching multiple records
        Returns: list of Student objects
        """
        query = "SELECT * FROM students ORDER BY aggregate_marks DESC"
        results = self.fetch_query(query)
        
        students = []  # Using list
        for data in results:
            student = Student(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                student_id=data['id'],
                secondary_school=data.get('secondary_school'),
                aggregate_marks=float(data.get('aggregate_marks', 0)),
                subject_combination=data.get('subject_combination'),
                location_from=data.get('location_from'),
                preferred_location=data.get('preferred_location'),
                desired_program=data.get('desired_program'),
                preferred_boarding=data.get('preferred_boarding', 'no_preference')
            )
            students.append(student)
        
        return students
    
    def update_student(self, student):
        """Update student information - demonstrates UPDATE operation"""
        query = """
        UPDATE students 
        SET first_name = %s, last_name = %s, email = %s, average_mark = %s
        WHERE id = %s
        """
        params = (student.first_name, student.last_name, student.email,
                 student.average_mark, student.student_id)
        return self.execute_query(query, params)
    
    def delete_student(self, student_id):
        """Delete student - demonstrates DELETE operation"""
        query = "DELETE FROM students WHERE id = %s"
        return self.execute_query(query, (student_id,))
    
    # ==================== SCHOOL OPERATIONS ====================
    
    def insert_school(self, school):
        """Insert a new school with comprehensive data"""
        query = """
        INSERT INTO schools (name, district, province, school_type, boarding, 
                           min_aggregate, min_cutoff, max_cutoff, required_subjects,
                           competencies_needed, contact_email, website)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
        """
        
        # Convert lists to comma-separated strings
        required_subj = ','.join(school.required_subjects) if school.required_subjects else None
        competencies = ','.join(school.competencies_needed) if school.competencies_needed else None
        
        params = (
            school.name, school.district, school.province, school.school_type,
            school.boarding_type, school.min_aggregate, school.min_cutoff, 
            school.max_cutoff, required_subj, competencies,
            school.contact_email, school.website
        )
        
        school_id = self.execute_query(query, params)
        if school_id:
            school.school_id = school_id
            return school_id
        return None
    
    def get_school_by_id(self, school_id):
        """Get school by ID with all details"""
        query = "SELECT * FROM schools WHERE id = %s"
        results = self.fetch_query(query, (school_id,))
        
        if results:
            data = results[0]
            
            # Parse comma-separated strings to lists
            required_subj = data.get('required_subjects', '').split(',') if data.get('required_subjects') else []
            competencies = data.get('competencies_needed', '').split(',') if data.get('competencies_needed') else []
            
            school = School(
                name=data['name'],
                district=data.get('district'),
                province=data.get('province'),
                school_type=data.get('school_type', 'private'),
                min_aggregate=float(data['min_aggregate']),
                min_cutoff=float(data.get('min_cutoff', data['min_aggregate'])),
                max_cutoff=float(data.get('max_cutoff', data['min_aggregate'])),
                boarding_type=data.get('boarding', 'day'),
                required_subjects=required_subj,
                competencies_needed=competencies,
                contact_email=data.get('contact_email'),
                website=data.get('website'),
                school_id=data['id']
            )
            
            # Load programs for this school
            school.programs = self.get_programs_by_school(school_id)
            
            return school
        return None
    
    def get_all_schools(self):
        """
        Get all schools with comprehensive data
        Returns: list of School objects
        """
        query = "SELECT * FROM schools ORDER BY name"
        results = self.fetch_query(query)
        
        schools = []
        for data in results:
            # Parse comma-separated strings to lists
            required_subj = data.get('required_subjects', '').split(',') if data.get('required_subjects') else []
            competencies = data.get('competencies_needed', '').split(',') if data.get('competencies_needed') else []
            
            school = School(
                name=data['name'],
                district=data.get('district'),
                province=data.get('province'),
                school_type=data.get('school_type', 'private'),
                min_aggregate=float(data['min_aggregate']),
                min_cutoff=float(data.get('min_cutoff', data['min_aggregate'])),
                max_cutoff=float(data.get('max_cutoff', data['min_aggregate'])),
                boarding_type=data.get('boarding', 'day'),
                required_subjects=required_subj,
                competencies_needed=competencies,
                contact_email=data.get('contact_email'),
                website=data.get('website'),
                school_id=data['id']
            )
            
            # Load programs for this school
            school.programs = self.get_programs_by_school(data['id'])
            
            schools.append(school)
        
        return schools
    
    def get_schools_by_min_mark(self, min_mark):
        """
        Get schools accepting students with specific aggregate marks
        Demonstrates: WHERE clause with comparison
        """
        query = "SELECT * FROM schools WHERE min_cutoff <= %s ORDER BY min_cutoff DESC"
        results = self.fetch_query(query, (min_mark,))
        
        schools = []
        for data in results:
            required_subj = data.get('required_subjects', '').split(',') if data.get('required_subjects') else []
            competencies = data.get('competencies_needed', '').split(',') if data.get('competencies_needed') else []
            
            school = School(
                name=data['name'],
                district=data.get('district'),
                province=data.get('province'),
                school_type=data.get('school_type', 'private'),
                min_aggregate=float(data['min_aggregate']),
                min_cutoff=float(data.get('min_cutoff', data['min_aggregate'])),
                max_cutoff=float(data.get('max_cutoff', data['min_aggregate'])),
                boarding_type=data.get('boarding', 'day'),
                required_subjects=required_subj,
                competencies_needed=competencies,
                contact_email=data.get('contact_email'),
                website=data.get('website'),
                school_id=data['id']
            )
            school.programs = self.get_programs_by_school(data['id'])
            schools.append(school)
        
        return schools
    
    # ==================== PROGRAM OPERATIONS ====================
    
    def insert_program(self, program_data):
        """Insert a new program for a school"""
        query = """
        INSERT INTO programs (school_id, program_name, program_code, cutoff_marks,
                            required_combination, duration_years, fees_range, description)
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        params = (
            program_data.get('school_id'),
            program_data.get('program_name'),
            program_data.get('program_code'),
            program_data.get('cutoff_marks'),
            program_data.get('required_combination'),
            program_data.get('duration_years', 4),
            program_data.get('fees_range'),
            program_data.get('description')
        )
        return self.execute_query(query, params)
    
    def get_programs_by_school(self, school_id):
        """Get all programs offered by a specific school"""
        query = "SELECT * FROM programs WHERE school_id = %s ORDER BY cutoff_marks DESC"
        results = self.fetch_query(query, (school_id,))
        return results if results else []
    
    def get_program_by_id(self, program_id):
        """Get a specific program by ID"""
        query = "SELECT * FROM programs WHERE id = %s"
        results = self.fetch_query(query, (program_id,))
        return results[0] if results else None
    
    def search_programs_by_name(self, program_name):
        """Search programs by name across all schools"""
        query = """
        SELECT p.*, s.name as school_name 
        FROM programs p
        JOIN schools s ON p.school_id = s.id
        WHERE p.program_name LIKE %s
        ORDER BY p.cutoff_marks
        """
        search_term = f"%{program_name}%"
        return self.fetch_query(query, (search_term,))
    
    # ==================== APPLICATION OPERATIONS ====================
    
    def insert_application(self, application):
        """Insert a new application"""
        query = """
        INSERT INTO applications (student_id, school_id, status)
        VALUES (%s, %s, %s)
        """
        params = (application.student_id, application.school_id, application.status)
        
        app_id = self.execute_query(query, params)
        if app_id:
            application.application_id = app_id
            return app_id
        return None
    
    def get_applications_by_student(self, student_id):
        """
        Get all applications for a student
        Demonstrates: JOIN operation, list of objects
        """
        query = """
        SELECT a.*, s.name as school_name
        FROM applications a
        JOIN schools s ON a.school_id = s.id
        WHERE a.student_id = %s
        ORDER BY a.applied_at DESC
        """
        results = self.fetch_query(query, (student_id,))
        
        applications = []
        for data in results:
            app = Application(
                student_id=data['student_id'],
                school_id=data['school_id'],
                application_id=data['id'],
                status=data['status'],
                applied_date=data['applied_at']
            )
            applications.append(app)
        
        return applications
    
    def get_applications_by_school(self, school_id):
        """Get all applications for a school"""
        query = """
        SELECT a.*, st.first_name, st.last_name, st.email, st.average_mark
        FROM applications a
        JOIN students st ON a.student_id = st.id
        WHERE a.school_id = %s
        ORDER BY a.applied_at DESC
        """
        results = self.fetch_query(query, (school_id,))
        
        applications = []
        for data in results:
            app = Application(
                student_id=data['student_id'],
                school_id=school_id,
                application_id=data['id'],
                status=data['status'],
                applied_date=data['applied_at']
            )
            applications.append(app)
        
        return applications
    
    def update_application_status(self, application_id, new_status):
        """Update application status - demonstrates UPDATE"""
        query = "UPDATE applications SET status = %s WHERE id = %s"
        return self.execute_query(query, (new_status, application_id))
    
    def check_existing_application(self, student_id, school_id):
        """
        Check if student already applied to school
        Demonstrates: complex WHERE clause
        """
        query = """
        SELECT * FROM applications 
        WHERE student_id = %s AND school_id = %s
        """
        results = self.fetch_query(query, (student_id, school_id))
        return len(results) > 0
    
    # ==================== STATISTICS & REPORTS ====================
    
    def get_statistics(self):
        """
        Get system statistics
        Demonstrates: COUNT, multiple queries, dictionary return
        """
        stats = {}  # Using dictionary
        
        # Total students
        result = self.fetch_query("SELECT COUNT(*) as count FROM students")
        stats['total_students'] = result[0]['count'] if result else 0
        
        # Total schools
        result = self.fetch_query("SELECT COUNT(*) as count FROM schools")
        stats['total_schools'] = result[0]['count'] if result else 0
        
        # Total applications
        result = self.fetch_query("SELECT COUNT(*) as count FROM applications")
        stats['total_applications'] = result[0]['count'] if result else 0
        
        # Pending applications
        result = self.fetch_query(
            "SELECT COUNT(*) as count FROM applications WHERE status = 'pending'"
        )
        stats['pending_applications'] = result[0]['count'] if result else 0
        
        return stats
    
    def advanced_match_search(self, student):
        """
        Advanced school search based on multiple criteria
        Demonstrates: Complex WHERE clauses, multiple conditions, JOIN
        Returns: list of matching schools
        """
        query = """
        SELECT DISTINCT s.* 
        FROM schools s
        WHERE s.min_cutoff <= %s
        AND (
            s.required_subjects IS NULL 
            OR s.required_subjects = '' 
            OR FIND_IN_SET(%s, s.required_subjects) > 0
        )
        ORDER BY s.min_cutoff DESC
        """
        
        params = (student.aggregate_marks, student.subject_combination)
        results = self.fetch_query(query, params)
        
        schools = []
        for data in results:
            required_subj = data.get('required_subjects', '').split(',') if data.get('required_subjects') else []
            competencies = data.get('competencies_needed', '').split(',') if data.get('competencies_needed') else []
            
            school = School(
                name=data['name'],
                district=data.get('district'),
                province=data.get('province'),
                school_type=data.get('school_type', 'private'),
                min_aggregate=float(data['min_aggregate']),
                min_cutoff=float(data.get('min_cutoff', data['min_aggregate'])),
                max_cutoff=float(data.get('max_cutoff', data['min_aggregate'])),
                boarding_type=data.get('boarding', 'day'),
                required_subjects=required_subj,
                competencies_needed=competencies,
                contact_email=data.get('contact_email'),
                website=data.get('website'),
                school_id=data['id']
            )
            school.programs = self.get_programs_by_school(data['id'])
            schools.append(school)
        
        return schools


# Standalone utility functions
def test_connection():
    """Test database connection - demonstrates function"""
    db = Database()
    if db.connect():
        print("✅ Database connection successful!")
        db.disconnect()
        return True
    else:
        print("❌ Database connection failed!")
        return False


def initialize_sample_data():
    """
    Initialize database with sample schools
    Demonstrates: function with multiple operations
    """
    db = Database()
    if not db.connect():
        return False
    
    # Sample schools as list of tuples
    sample_schools = [
        ("University of Rwanda", "Kigali", "boarding", 65.00, "admissions@ur.ac.rw"),
        ("Kigali Independent University", "Kigali", "day", 55.00, "info@kiu.ac.rw"),
        ("Mount Kenya University Rwanda", "Kigali", "boarding", 50.00, "apply@mku.rw"),
        ("African Leadership University", "Kigali", "boarding", 75.00, "admissions@alu.edu")
    ]
    
    for school_data in sample_schools:
        school = School(
            name=school_data[0],
            district=school_data[1],
            courses=["General"],
            min_aggregate=school_data[3],
            boarding_type=school_data[2],
            contact_email=school_data[4]
        )
        db.insert_school(school)
    
    db.disconnect()
    return True