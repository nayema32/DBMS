## code to add new student

import sqlite3

def add_student(student_id, name, year_of_enrollment, major, gender, email, phone_number, address):
    conn = sqlite3.connect('sichuan_university.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Students 
                      (student_id, name, year_of_enrollment, major, gender, email, phone_number, address) 
                      VALUES (?, ?, ?, ?, ?, ?, ?, ?)''',
                   (student_id, name, year_of_enrollment, major, gender, email, phone_number, address))
    conn.commit()
    conn.close()
    print("Student added successfully.")

# add demo students to the database
add_student(1, "Nayema Akter", 2021, "Software Engineering", "Female", "nayema.akter@example.com", "1234567890", "sichuan")
add_student(2, "Jane Smith", 2022, "Electrical Engineering", "Female", "jane.smith@example.com", "0987654321", "456 Elm St")
add_student(3, "Alice Johnson", 2024, "Mechanical Engineering", "Female", "alice.johnson@example.com", "1122334455", "789 Oak St")
add_student(4, "Bob Brown", 2023, "Mathematics", "Male", "bob.brown@example.com", "2233445566", "101 Pine St")
add_student(5, "Charlie Davis", 2021, "Physics", "Non-binary", "charlie.davis@example.com", "3344556677", "202 Birch St")
add_student(6, "Diana Evans", 2023, "Chemical Engineering", "Female", "diana.evans@example.com", "4455667788", "303 Cedar St")
add_student(7, "Ethan Wilson", 2022, "Civil Engineering", "Male", "ethan.wilson@example.com", "5566778899", "404 Maple St")
add_student(8, "Fiona Thomas", 2024, "Biology", "Female", "fiona.thomas@example.com", "6677889900", "505 Walnut St")
add_student(9, "George White", 2021, "History", "Male", "george.white@example.com", "7788990011", "606 Willow St")
add_student(10, "Hannah Martin", 2023, "Philosophy", "Female", "hannah.martin@example.com", "8899001122", "707 Cherry St")
add_student(11, "Yuki Tanaka", 2023, "Computer Science", "Female", "yuki.tanaka@example.com", "9988776655", "808 Sakura Ave")
add_student(12, "Wei Chen", 2022, "Electrical Engineering", "Male", "wei.chen@example.com", "8877665544", "909 Bamboo St")
add_student(13, "Ji-hyun Park", 2024, "Business Administration", "Female", "jihyun.park@example.com", "7766554433", "1010 Lotus St")
add_student(14, "Ravi Patel", 2023, "Chemical Engineering", "Male", "ravi.patel@example.com", "6655443322", "1111 Jade St")
add_student(15, "Mei Li", 2021, "Economics", "Female", "mei.li@example.com", "5544332211", "1212 Bamboo Ave")
add_student(16, "Hiroshi Yamamoto", 2023, "Mechanical Engineering", "Male", "hiroshi.yamamoto@example.com", "4433221100", "1313 Pine St")
add_student(17, "Priya Gupta", 2022, "Computer Science", "Female", "priya.gupta@example.com", "3322110099", "1414 Orchid St")
add_student(18, "Jung-sik Kim", 2024, "Chemistry", "Male", "jungsik.kim@example.com", "2211009988", "1515 Magnolia Ave")
add_student(19, "Sakura Tanaka", 2021, "Art History", "Female", "sakura.tanaka@example.com", "1100998877", "1616 Sakura Ave")
add_student(20, "Linh Nguyen", 2023, "Environmental Science", "Female", "linh.nguyen@example.com", "0099887766", "1717 Lotus St")


##Update student informations
def update_student(student_id, name=None, year_of_enrollment=None, major=None, gender=None, email=None,
                   phone_number=None, address=None):
    conn = sqlite3.connect('sichuan_university.db')
    cursor = conn.cursor()
    query = "UPDATE Students SET "
    params = []
    if name:
        query += "name = ?, "
        params.append(name)
    if year_of_enrollment:
        query += "year_of_enrollment = ?, "
        params.append(year_of_enrollment)
    if major:
        query += "major = ?, "
        params.append(major)
    if gender:
        query += "gender = ?, "
        params.append(gender)
    if email:
        query += "email = ?, "
        params.append(email)
    if phone_number:
        query += "phone_number = ?, "
        params.append(phone_number)
    if address:
        query += "address = ?, "
        params.append(address)

    query = query.rstrip(', ')
    query += " WHERE student_id = ?"
    params.append(student_id)

    cursor.execute(query, params)
    conn.commit()
    conn.close()
    print("Student updated successfully.")


# Example usage
update_student(1, name="Jane Doel")
update_student(2, name="Johon Smith")
update_student(3, name="Alicia Jonson")
update_student(4, email="bobby.brown1@example.com")
update_student(5, major="physics")
update_student(6, phone="5542432211")
update_student(7, address="505 Maple Street")

##delete student record

def delete_student(student_id):
    conn = sqlite3.connect('sichuan_university.db')
    cursor = conn.cursor()
    cursor.execute('''DELETE FROM Students WHERE student_id = ?''', (student_id,))
    conn.commit()
    conn.close()
    print("Student deleted successfully.")

# Example usage
delete_student(6)

##Query operations

def query_student(student_id):
    conn = sqlite3.connect('sichuan_university.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM Students WHERE student_id = ?''', (student_id,))
    student = cursor.fetchone()
    conn.close()
    return student

# Example usage
student = query_student(1)
if student:
    print(student)
else:
    print("Student not found.")

def query_student_by_email(email):
    conn = sqlite3.connect('sichuan_university.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM Students WHERE email = ?''', (email,))
    student = cursor.fetchone()
    conn.close()
    return student

# Example usage 2 - retrive student by email
student = query_student_by_email('john.doe@example.com')
if student:
    print(student)
else:
    print("Student with this email not found.")

def query_students_by_gender(gender):
    conn = sqlite3.connect('sichuan_university.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM Students WHERE gender = ?''', (gender,))
    students = cursor.fetchall()
    conn.close()
    return students

# Example usage 3 - retrieve student by gender
students = query_students_by_gender('Female')
if students:
    for student in students:
        print(student)
else:
    print("No students found with this gender.")

def query_students_by_major(major):
    conn = sqlite3.connect('sichuan_university.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM Students WHERE major = ?''', (major,))
    students = cursor.fetchall()
    conn.close()
    return students

# Example usage 4 - Retrieve student by major
students = query_students_by_major('Computer Science')
if students:
    for student in students:
        print(student)
else:
    print("No students found in this major.")

def query_students_by_graduation_year(year):
    conn = sqlite3.connect('sichuan_university.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM Students WHERE graduation_year = ?''', (year,))
    students = cursor.fetchall()
    conn.close()
    return students

# Example usage 5- Retrieve students graduating in a specific year
students = query_students_by_graduation_year(2023)
if students:
    for student in students:
        print(student)
else:
    print("No students graduating in this year.")


def query_all_students():
    conn = sqlite3.connect('sichuan_university.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM Students''')
    students = cursor.fetchall()
    conn.close()
    return students

# Example usage 6 - Retrieve all students
students = query_all_students()
if students:
    for student in students:
        print(student)
else:
    print("No students found.")






