import psycopg2

# Function to create a new connection to the database
def create_conn():
    return psycopg2.connect(database="school", user="postgres", password="admin", host="127.0.0.1", port="5432")

# Function to retrieve and display all records from the students table
def getAllStudents():
    try:
        conn = create_conn()
        cur = conn.cursor()
        cur.execute("SELECT * FROM students")
        rows = cur.fetchall()
        for row in rows:
            print(row)
        conn.close()
    except Exception as e:
        print("An error occurred while retrieving students:", e)

# Function to insert a new student record into the students table
def addStudent(first_name, last_name, email, enrollment_date):
    try:
        conn = create_conn()
        cur = conn.cursor()
        cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
        conn.commit()
        conn.close()
    except Exception as e:
        print("An error occurred while adding a student:", e)

# Function to update the email address for a student with the specified student_id
def updateStudentEmail(student_id, new_email):
    try:
        conn = create_conn()
        cur = conn.cursor()
        cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
        conn.commit()
        conn.close()
    except Exception as e:
        print("An error occurred while updating a student's email:", e)

# Function to delete the record of the student with the specified student_id
def deleteStudent(student_id):
    try:
        conn = create_conn()
        cur = conn.cursor()
        cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
        conn.commit()
        conn.close()
    except Exception as e:
        print("An error occurred while deleting a student:", e)

# Call the function to test
print("Initial students:")
getAllStudents()

print("Adding a student:")
addStudent('Mike', 'Tyson', 'mike.tyson@example.com', '2023-09-03')
getAllStudents()

print("Updating a student's email:")
updateStudentEmail(1, 'new.john.doe@example.com')
getAllStudents()

print("Deleting a student:")
deleteStudent(2)
getAllStudents()