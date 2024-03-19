from psycopg2 import OperationalError, IntegrityError, DataError


def getAllStudents(cur):
    try:
        cur.execute("SELECT * FROM students")
        rows = cur.fetchall()
        for row in rows:
            print(row)
    except (OperationalError, DataError) as e:
        print(f"Error fetching students: {e}")

def addStudent(cur, conn, first_name, last_name, email, enrollment_date):
    try:
        cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)",
                    (first_name, last_name, email, enrollment_date))
        conn.commit()
        print("Student added:", first_name, last_name)
    except (IntegrityError, DataError) as e:
        print(f"Error adding student: {e}")
        conn.rollback()

def updateStudentEmail(cur, conn, student_id, new_email):
    try:
        cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
        conn.commit()
        if cur.rowcount == 0:
            print("Student not found:", student_id)
        else:
            print("Student email updated:", student_id)
    except (OperationalError, DataError) as e:
        print(f"Error updating student email: {e}")
        conn.rollback()

def deleteStudent(cur, conn, student_id):
    try:
        cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
        conn.commit()
        if cur.rowcount == 0:
            print("Student not found:", student_id)
        else:
            print("Student deleted:", student_id)
    except (OperationalError, DataError) as e:
        print(f"Error deleting student: {e}")
        conn.rollback()

