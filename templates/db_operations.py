import sqlite3

def connect_db():
    return sqlite3.connect('sichuan_university.db')

def add_student_db(name, year_of_enrollment, major, gender, birth_year, region):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("INSERT INTO Students (name, year_of_enrollment, major, gender, birth_year, region) VALUES (?, ?, ?, ?, ?, ?)",
                   (name, year_of_enrollment, major, gender, birth_year, region))
    conn.commit()
    conn.close()

def update_student_db(student_id, name, year_of_enrollment, major, gender, birth_year, region):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("UPDATE Students SET name=?, year_of_enrollment=?, major=?, gender=?, birth_year=?, region=? WHERE student_id=?",
                   (name, year_of_enrollment, major, gender, birth_year, region, student_id))
    conn.commit()
    conn.close()

def delete_student_db(student_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Students WHERE student_id=?", (student_id,))
    conn.commit()
    conn.close()

def query_student_db(student_id):
    conn = connect_db()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Students WHERE student_id=?", (student_id,))
    student = cursor.fetchone()
    conn.close()
    return student
