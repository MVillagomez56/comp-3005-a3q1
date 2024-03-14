import psycopg2

from db_functions import *

dbname = "a3-q1"
user = "postgres"
password = 'postgres'
host = "localhost"
port = 5433

def connect():
    conn = psycopg2.connect(dbname=dbname, user=user, password=password, host=host, port=port)
    cur = conn.cursor()
    return conn, cur

def disconnect(conn, cur):
    cur.close()
    conn.close()

def main():
    conn, cur = connect()
    print("Welcome to the student database!")
    while True:
        print("1. View all students")
        print("2. Add a student")
        print("3. Update a student's email")
        print("4. Delete a student")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            getAllStudents(cur)
        elif choice == "2":
            first_name = input("Enter student's first name: ")
            last_name = input("Enter student's last name: ")
            email = input("Enter student's email: ")
            enrollment_date = input("Enter student's enrollment date (YYYY-MM-DD): ")
            addStudent(cur, conn, first_name, last_name, email, enrollment_date)
        elif choice == "3":
            student_id = input("Enter student's ID: ")
            new_email = input("Enter student's new email: ")
            updateStudentEmail(cur, conn,student_id, new_email)
        elif choice == "4":
            student_id = input("Enter student's ID: ")
            deleteStudent(cur, conn,student_id)
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")
    # Close the cursor and connection to the database
    disconnect(conn, cur);

main()