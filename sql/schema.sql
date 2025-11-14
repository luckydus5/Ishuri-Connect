-- sql/schema.sql
-- Enhanced schema for comprehensive student-school matching

CREATE TABLE IF NOT EXISTS students (
  id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(150) NOT NULL,
  -- Previous education
  secondary_school VARCHAR(200),
  aggregate_marks DECIMAL(5,2) NOT NULL,
  average_mark DECIMAL(5,2) NOT NULL,
  subject_combination VARCHAR(50), -- PCM, PCB, MEG, HEG, LKE, etc.
  -- Location preferences
  location_from VARCHAR(100), -- District/Province they're from
  preferred_location VARCHAR(100), -- Where they want to study
  -- Program preferences
  desired_program VARCHAR(200), -- What they want to study
  preferred_boarding ENUM('boarding','day','no_preference') DEFAULT 'no_preference',
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS schools (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(200) NOT NULL,
  district VARCHAR(100),
  province VARCHAR(50), -- Northern, Southern, Eastern, Western, Kigali
  school_type ENUM('public','private') DEFAULT 'private',
  boarding ENUM('boarding','day','both') DEFAULT 'day',
  -- Admission requirements
  min_aggregate DECIMAL(5,2) NOT NULL,
  min_cutoff DECIMAL(5,2) NOT NULL, -- Minimum cutoff across all programs
  max_cutoff DECIMAL(5,2) NOT NULL, -- Maximum cutoff (most competitive program)
  required_subjects TEXT, -- Comma-separated acceptable combinations: PCM,PCB,MEG
  competencies_needed TEXT, -- Skills/competencies required
  contact_email VARCHAR(150),
  website VARCHAR(200)
);

CREATE TABLE IF NOT EXISTS applications (
  id INT AUTO_INCREMENT PRIMARY KEY,
  student_id INT NOT NULL,
  school_id INT NOT NULL,
  program_id INT, -- Can be NULL if applying to school without specific program
  applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  status ENUM('pending','accepted','rejected','withdrawn') DEFAULT 'pending',
  FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
  FOREIGN KEY (school_id) REFERENCES schools(id) ON DELETE CASCADE,
  FOREIGN KEY (program_id) REFERENCES programs(id) ON DELETE SET NULL
);

-- Programs table - stores programs offered by each school
CREATE TABLE IF NOT EXISTS programs (
  id INT AUTO_INCREMENT PRIMARY KEY,
  school_id INT NOT NULL,
  program_name VARCHAR(200) NOT NULL,
  program_code VARCHAR(50), -- e.g., BSC-CS, BA-ECON
  cutoff_marks DECIMAL(5,2) NOT NULL,
  required_combination VARCHAR(100), -- e.g., "PCM,PCB" - acceptable combinations
  duration_years INT DEFAULT 4,
  fees_range VARCHAR(100), -- e.g., "500,000 - 1,200,000 RWF"
  description TEXT,
  FOREIGN KEY (school_id) REFERENCES schools(id) ON DELETE CASCADE
);

-- Sample schools with comprehensive data
INSERT INTO schools (name, district, province, school_type, boarding, min_aggregate, min_cutoff, max_cutoff, required_subjects, competencies_needed, contact_email, website)
VALUES
('University of Rwanda', 'Kigali', 'Kigali', 'public', 'both', 60.00, 60.00, 85.00, 'PCM,PCB,MEG,HEG,LKE', 'Critical thinking, Research, Communication', 'admissions@ur.ac.rw', 'www.ur.ac.rw'),
('African Leadership University', 'Kigali', 'Kigali', 'private', 'boarding', 65.00, 65.00, 80.00, 'PCM,PCB,MEG,HEG', 'Leadership, Entrepreneurship, Innovation', 'admissions@alueducation.com', 'www.alueducation.com'),
('Kigali Independent University', 'Kigali', 'Kigali', 'private', 'day', 50.00, 50.00, 70.00, 'PCM,PCB,MEG,HEG,LKE', 'Problem solving, Teamwork', 'info@kiu.ac.rw', 'www.kiu.ac.rw'),
('Adventist University of Central Africa', 'Kigali', 'Kigali', 'private', 'boarding', 55.00, 55.00, 72.00, 'PCM,PCB,MEG,HEG,LKE', 'Ethics, Service, Excellence', 'info@auca.ac.rw', 'www.auca.ac.rw'),
('Mount Kenya University Rwanda', 'Kigali', 'Kigali', 'private', 'both', 48.00, 48.00, 68.00, 'PCM,PCB,MEG,HEG,LKE,MCB', 'Practical skills, Innovation', 'info@mku.ac.rw', 'www.mku.ac.rw'),
('University of Kigali', 'Kigali', 'Kigali', 'private', 'day', 50.00, 50.00, 70.00, 'PCM,PCB,MEG,HEG,LKE', 'Technology, Business acumen', 'info@uok.ac.rw', 'www.uok.ac.rw'),
('University of Lay Adventists of Kigali', 'Kigali', 'Kigali', 'private', 'day', 48.00, 48.00, 65.00, 'PCM,PCB,MEG,HEG,LKE,MCB', 'Community service, Integrity', 'info@unilak.ac.rw', 'www.unilak.ac.rw'),
('INES - Ruhengeri', 'Musanze', 'Northern', 'private', 'boarding', 52.00, 52.00, 70.00, 'PCM,PCB,MEG,HEG', 'Engineering skills, Research', 'info@ines.ac.rw', 'www.ines.ac.rw'),
('Catholic University of Rwanda', 'Huye', 'Southern', 'private', 'boarding', 53.00, 53.00, 72.00, 'PCM,PCB,MEG,HEG,LKE', 'Social responsibility, Ethics', 'info@catho.ac.rw', 'www.catho.ac.rw'),
('University of Tourism Technology and Business Studies', 'Kigali', 'Kigali', 'private', 'both', 45.00, 45.00, 62.00, 'MEG,HEG,LKE,MCB', 'Hospitality, Business management', 'info@uttbs.ac.rw', 'www.uttbs.ac.rw');

-- Sample programs for different universities
INSERT INTO programs (school_id, program_name, program_code, cutoff_marks, required_combination, duration_years, fees_range, description)
VALUES
-- University of Rwanda programs
(1, 'Bachelor of Science in Computer Science', 'BSC-CS', 75.00, 'PCM', 4, '500,000 - 800,000 RWF', 'Software development, algorithms, AI'),
(1, 'Bachelor of Medicine and Surgery', 'MBBS', 85.00, 'PCB', 6, '1,500,000 - 2,000,000 RWF', 'Medical training and clinical practice'),
(1, 'Bachelor of Engineering in Civil Engineering', 'BE-CE', 72.00, 'PCM', 5, '600,000 - 900,000 RWF', 'Infrastructure design and construction'),
(1, 'Bachelor of Economics', 'BA-ECON', 68.00, 'MEG,HEG', 3, '400,000 - 700,000 RWF', 'Economic theory and analysis'),
(1, 'Bachelor of Education', 'BED', 60.00, 'PCM,PCB,MEG,HEG,LKE', 3, '350,000 - 600,000 RWF', 'Teacher training program'),

-- ALU programs
(2, 'Bachelor of Science in Global Challenges', 'BSC-GC', 70.00, 'PCM,PCB,MEG', 3, '15,000 - 20,000 USD', 'Entrepreneurial leadership and innovation'),
(2, 'Bachelor of Science in Software Engineering', 'BSC-SE', 75.00, 'PCM', 4, '15,000 - 20,000 USD', 'Full-stack development and systems'),

-- KIU programs
(3, 'Bachelor of Business Administration', 'BBA', 55.00, 'MEG,HEG', 3, '800,000 - 1,200,000 RWF', 'Business management and entrepreneurship'),
(3, 'Bachelor of Science in Nursing', 'BSC-NURS', 60.00, 'PCB', 4, '700,000 - 1,000,000 RWF', 'Healthcare and nursing practice'),
(3, 'Bachelor of Laws', 'LLB', 65.00, 'HEG,LKE', 4, '900,000 - 1,300,000 RWF', 'Legal studies and jurisprudence'),

-- AUCA programs
(4, 'Bachelor of Arts in Theology', 'BA-THEO', 55.00, 'LKE,HEG', 4, '600,000 - 900,000 RWF', 'Religious studies and ministry'),
(4, 'Bachelor of Business Administration', 'BBA', 58.00, 'MEG,HEG', 3, '700,000 - 1,000,000 RWF', 'Business and management'),
(4, 'Bachelor of Science in Information Technology', 'BSC-IT', 65.00, 'PCM,MEG', 4, '800,000 - 1,200,000 RWF', 'IT systems and networking'),

-- MKU programs
(5, 'Bachelor of Commerce', 'BCOM', 50.00, 'MEG,HEG', 3, '700,000 - 1,000,000 RWF', 'Accounting and finance'),
(5, 'Bachelor of Science in Public Health', 'BSC-PH', 58.00, 'PCB,MEG', 4, '650,000 - 950,000 RWF', 'Community health and epidemiology'),
(5, 'Bachelor of Education Arts', 'BED-ARTS', 48.00, 'LKE,HEG', 3, '500,000 - 800,000 RWF', 'Arts and humanities teaching'),

-- UoK programs
(6, 'Bachelor of Science in Computer Engineering', 'BSC-CE', 62.00, 'PCM', 4, '800,000 - 1,200,000 RWF', 'Hardware and software systems'),
(6, 'Bachelor of Architecture', 'B-ARCH', 65.00, 'PCM', 5, '900,000 - 1,400,000 RWF', 'Building design and urban planning'),

-- UNILAK programs
(7, 'Bachelor of Science in Agriculture', 'BSC-AGR', 50.00, 'PCB,PCM', 4, '500,000 - 800,000 RWF', 'Crop science and agribusiness'),
(7, 'Bachelor of Social Work', 'BSW', 48.00, 'HEG,LKE', 3, '450,000 - 700,000 RWF', 'Community development and counseling'),

-- INES programs
(8, 'Bachelor of Engineering in Electronics', 'BE-ELEC', 65.00, 'PCM', 5, '700,000 - 1,100,000 RWF', 'Electronics and telecommunications'),
(8, 'Bachelor of Science in Applied Mathematics', 'BSC-MATH', 68.00, 'PCM', 4, '600,000 - 900,000 RWF', 'Mathematical modeling and statistics'),

-- Catholic University programs
(9, 'Bachelor of Science in Biotechnology', 'BSC-BIOTECH', 70.00, 'PCB', 4, '750,000 - 1,100,000 RWF', 'Genetic engineering and microbiology'),
(9, 'Bachelor of Development Studies', 'BDS', 58.00, 'MEG,HEG', 3, '550,000 - 850,000 RWF', 'Community development and policy'),

-- UTTBS programs
(10, 'Bachelor of Tourism Management', 'BTM', 48.00, 'MEG,HEG,LKE', 3, '600,000 - 900,000 RWF', 'Hospitality and tourism industry'),
(10, 'Bachelor of Culinary Arts', 'BCA', 45.00, 'MEG,LKE,MCB', 3, '700,000 - 1,000,000 RWF', 'Professional cooking and restaurant management');