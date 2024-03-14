def getAllStudents(cur):
    cur.execute("SELECT * FROM students")
    rows = cur.fetchall()
    for row in rows:
        print(row)

def addStudent(cur,conn,first_name, last_name, email, enrollment_date):
    cur.execute("INSERT INTO students (first_name, last_name, email, enrollment_date) VALUES (%s, %s, %s, %s)", (first_name, last_name, email, enrollment_date))
    conn.commit()
    print("Student added:", first_name, last_name)

def updateStudentEmail(cur, conn, student_id, new_email):
    cur.execute("UPDATE students SET email = %s WHERE student_id = %s", (new_email, student_id))
    conn.commit()
    print("Student email updated:", student_id)

def deleteStudent(cur, conn, student_id):
    cur.execute("DELETE FROM students WHERE student_id = %s", (student_id,))
    conn.commit()
    print("Student deleted:", student_id)

    
