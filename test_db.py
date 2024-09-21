import sqlite3

def add_student(name, year_of_enrollment, major, gender, email, phone_number, address):
    conn = sqlite3.connect('sichuan_university.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Students (name, year_of_enrollment, major, gender, email, phone_number, address)
                      VALUES (?, ?, ?, ?, ?, ?, ?)''',
                   (name, year_of_enrollment, major, gender, email, phone_number, address))
    conn.commit()
    conn.close()

def test_db():
    # adding some sample data
    add_student('Alice', 2023, 'Computer Science', 'Female', 'alice@example.com', '1234567890', '123 Main St')
    add_student('Bob', 2022, 'Mathematics', 'Male', 'bob@example.com', '0987654321', '456 Elm St')

    conn = sqlite3.connect('sichuan_university.db')
    cursor = conn.cursor()

    # Retrieve information and print information for all students
    cursor.execute('SELECT * FROM Students')
    students = cursor.fetchall()
    for student in students:
        print(student)

    conn.close()

# apply test function
test_db()
