# COMP3005-A3

# Students Database Application

This application connects to a PostgreSQL database and performs CRUD (Create, Read, Update, Delete) operations on the `students` table.

## Setup

1. Install PostgreSQL and create a new database named "school".
2. Run the SQL commands in `DDL.sql` to create and populate the `students` table.
3. Install the required Python libraries with `pip install -r requirements.txt`.

## Running the Application

Run the application with `python script.py`.

## Functionality

- `getAllStudents()`: Retrieves and displays all records from the students table.
- `addStudent(first_name, last_name, email, enrollment_date)`: Inserts a new student record into the students table.
- `updateStudentEmail(student_id, new_email)`: Updates the email address for a student with the specified student_id.
- `deleteStudent(student_id)`: Deletes the record of the student with the specified student_id.
