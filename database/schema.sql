create database school_management;

use school_management;

CREATE TABLE students (
    id int primary key auto_increment,
    student_id varchar(50) UNIQUE NOT null,
    first_name varchar(50) NOT null,
    last_name varchar(50) NOT null,
    email varchar(100) UNIQUE not null,
    phone varchar(15),
    date_of_birth DATE,
    gender ENUM("MALE", "FEMALE", "OTHERS"),
    address TEXT,
    enrollment_date DATE DEFAULT(CURRENT_DATE),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
)


CREATE TABLE teachers(
id int PRIMARY KEY AUTO_INCREMENT,
    teacher_id varchar(50) UNIQUE NOT null,
    first_name varchar(50) NOT null,
    last_name varchar(50) NOT null,
    email varchar(100) UNIQUE not null,
    phone varchar(15),
    subject varchar(100),
    qualification varchar(100),
    experience_years int,
    salary decimal(10, 2),
    hire_date date DEFAULT (CURRENT_DATE),
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP 
)

CREATE TABLE courses ( id int PRIMARY KEY AUTO_INCREMENT, course_code varchar(20) UNIQUE not null, course_name varchar(100) not null, description TEXT, credits INT, teacher_id INT, capacity int DEFAULT 30, semester varchar(20), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY(teacher_id) REFERENCES teachers(id) on DELETE set null);


CREATE TABLE enrollments( id int PRIMARY KEY AUTO_INCREMENT, student_id INT NOT NULL, course_id INT NOT NULL, enrollment_date DATE DEFAULT(CURRENT_DATE), grade varchar(15), status ENUM("Active", "Completed", "Dropped") DEFAULT "Active", created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP, FOREIGN KEY (student_id) REFERENCES students(id) ON DELETE CASCADE, FOREIGN KEY (course_id) REFERENCES courses(id) ON DELETE CASCADE, UNIQUE KEY unique_enrollment(student_id, course_id) );