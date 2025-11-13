-- sql/schema.sql
CREATE DATABASE IF NOT EXISTS ishuri_connect;
USE ishuri_connect;

CREATE TABLE IF NOT EXISTS students (
  id INT AUTO_INCREMENT PRIMARY KEY,
  first_name VARCHAR(100) NOT NULL,
  last_name VARCHAR(100) NOT NULL,
  email VARCHAR(150) NOT NULL,
  average_mark DECIMAL(5,2) NOT NULL,
  created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);

CREATE TABLE IF NOT EXISTS schools (
  id INT AUTO_INCREMENT PRIMARY KEY,
  name VARCHAR(200) NOT NULL,
  district VARCHAR(100),
  boarding ENUM('boarding','day') DEFAULT 'day',
  min_aggregate DECIMAL(5,2) NOT NULL,
  contact_email VARCHAR(150)
);

CREATE TABLE IF NOT EXISTS applications (
  id INT AUTO_INCREMENT PRIMARY KEY,
  student_id INT NOT NULL,
  school_id INT NOT NULL,
  applied_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
  status ENUM('pending','accepted','rejected') DEFAULT 'pending',
  FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE,
  FOREIGN KEY (school_id) REFERENCES schools(id) ON DELETE CASCADE
);

-- sample schools (optional)
INSERT INTO schools (name, district, boarding, min_aggregate, contact_email)
VALUES
('University of Rwanda', 'Kigali', 'boarding', 65.00, 'admissions@ur.ac.rw'),
('Kigali Independent University', 'Kigali', 'day', 55.00, 'info@kinyu.ac.rw'),
('Mount Kenya University Rwanda', 'Kigali', 'boarding', 50.00, 'apply@mku.rw');
('African Leadership University', 'Kigali', 'day', 60.00, 'https://www.alueducation.com/apply-now/')