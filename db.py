"""
Database Operations for Ishuri-Connect
Demonstrates: MySQL connections, CRUD operations, Functions, Error handling
"""

import mysql.connector
from mysql.connector import Error
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
        self.connection = None
    
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
    
    def fetch_query(self, query, params=None):
        """
        Fetch data from database
        Demonstrates: function returning lists/tuples
        """
        try:
            cursor = self.connection.cursor(dictionary=True)
            if params:
                cursor.execute(query, params)
            else:
                cursor.execute(query)
            results = cursor.fetchall()  # Returns list of dictionaries
            return results
        except Error as e:
            print(f"Error fetching data: {e}")
            return []
        finally:
            cursor.close()
    
    # ==================== STUDENT OPERATIONS ====================
    
    def insert_student(self, student):
        """
        Insert a new student into database
        Demonstrates: INSERT operation, using object attributes
        """
        query = """
        INSERT INTO students (first_name, last_name, email, average_mark)
        VALUES (%s, %s, %s, %s)
        """
        params = (student.first_name, student.last_name, 
                 student.email, student.average_mark)
        
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
                student_id=data['id']
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
                student_id=data['id']
            )
        return None
    
    def get_all_students(self):
        """
        Get all students - demonstrates fetching multiple records
        Returns: list of Student objects
        """
        query = "SELECT * FROM students ORDER BY average_mark DESC"
        results = self.fetch_query(query)
        
        students = []  # Using list
        for data in results:
            student = Student(
                first_name=data['first_name'],
                last_name=data['last_name'],
                email=data['email'],
                student_id=data['id']
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
        """Insert a new school"""
        query = """
        INSERT INTO schools (name, district, boarding, min_aggregate, contact_email)
        VALUES (%s, %s, %s, %s, %s)
        """
        params = (school.name, school.district, school.boarding_type,
                 school.min_aggregate, school.contact_email)
        
        school_id = self.execute_query(query, params)
        if school_id:
            school.school_id = school_id
            return school_id
        return None
    
    def get_school_by_id(self, school_id):
        """Get school by ID"""
        query = "SELECT * FROM schools WHERE id = %s"
        results = self.fetch_query(query, (school_id,))
        
        if results:
            data = results[0]
            return School(
                name=data['name'],
                district=data['district'],
                courses=["General"],  # Will enhance later
                min_aggregate=float(data['min_aggregate']),
                boarding_type=data['boarding'],
                contact_email=data['contact_email'],
                school_id=data['id']
            )
        return None
    
    def get_all_schools(self):
        """
        Get all schools
        Returns: list of School objects
        """
        query = "SELECT * FROM schools ORDER BY name"
        results = self.fetch_query(query)
        
        schools = []
        for data in results:
            school = School(
                name=data['name'],
                district=data['district'],
                courses=["General"],
                min_aggregate=float(data['min_aggregate']),
                boarding_type=data['boarding'],
                contact_email=data['contact_email'],
                school_id=data['id']
            )
            schools.append(school)
        
        return schools
    
    def get_schools_by_min_mark(self, min_mark):
        """
        Get schools accepting students with specific marks
        Demonstrates: WHERE clause with comparison
        """
        query = "SELECT * FROM schools WHERE min_aggregate <= %s ORDER BY min_aggregate DESC"
        results = self.fetch_query(query, (min_mark,))
        
        schools = []
        for data in results:
            school = School(
                name=data['name'],
                district=data['district'],
                courses=["General"],
                min_aggregate=float(data['min_aggregate']),
                boarding_type=data['boarding'],
                contact_email=data['contact_email'],
                school_id=data['id']
            )
            schools.append(school)
        
        return schools
    
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