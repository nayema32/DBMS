import sqlite3

def initialize_database():
    conn = sqlite3.connect('sichuan_university.db')
    cursor = conn.cursor()

    # create student table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Students (
                        student_id INTEGER PRIMARY KEY,
                        name TEXT NOT NULL,
                        year_of_enrollment INTEGER NOT NULL,
                        major TEXT NOT NULL,
                        gender TEXT CHECK (gender IN ('Male', 'Female', 'Other')) NOT NULL,
                        email TEXT UNIQUE NOT NULL,
                        phone_number TEXT,
                        address TEXT)''')

    # Create Courses table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Courses (
                        course_id INTEGER PRIMARY KEY,
                        course_name TEXT NOT NULL,
                        description TEXT,
                        credits INTEGER NOT NULL)''')

    # Create Enrollments table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Enrollments (
                        enrollment_id INTEGER PRIMARY KEY,
                        student_id INTEGER NOT NULL,
                        course_id INTEGER NOT NULL,
                        enrollment_date DATE NOT NULL,
                        FOREIGN KEY (student_id) REFERENCES Students(student_id),
                        FOREIGN KEY (course_id) REFERENCES Courses(course_id))''')

    # Create Accommodations table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Accommodations (
                        accommodation_id INTEGER PRIMARY KEY,
                        student_id INTEGER NOT NULL,
                        dorm_number TEXT NOT NULL,
                        room_number TEXT NOT NULL,
                        start_date DATE NOT NULL,
                        end_date DATE,
                        FOREIGN KEY (student_id) REFERENCES Students(student_id))''')

    # Create Books table
    cursor.execute('''CREATE TABLE IF NOT EXISTS Books (
                        book_id INTEGER PRIMARY KEY,
                        title TEXT NOT NULL,
                        author TEXT NOT NULL,
                        isbn TEXT UNIQUE NOT NULL,
                        price REAL NOT NULL)''')

    # Create CourseBooks table
    cursor.execute('''CREATE TABLE IF NOT EXISTS CourseBooks (
                        course_book_id INTEGER PRIMARY KEY,
                        course_id INTEGER NOT NULL,
                        book_id INTEGER NOT NULL,
                        FOREIGN KEY (course_id) REFERENCES Courses(course_id),
                        FOREIGN KEY (book_id) REFERENCES Books(book_id))''')

    # Create BookPurchases table
    cursor.execute('''CREATE TABLE IF NOT EXISTS BookPurchases (
                        purchase_id INTEGER PRIMARY KEY,
                        student_id INTEGER NOT NULL,
                        book_id INTEGER NOT NULL,
                        purchase_date DATE NOT NULL,
                        FOREIGN KEY (student_id) REFERENCES Students(student_id),
                        FOREIGN KEY (book_id) REFERENCES Books(book_id))''')

    # Create StudentAdvisors table
    cursor.execute('''CREATE TABLE IF NOT EXISTS StudentAdvisors (
                        advisor_id INTEGER PRIMARY KEY,
                        student_id INTEGER NOT NULL,
                        advisor_name TEXT NOT NULL,
                        advisor_email TEXT NOT NULL,
                        advisor_phone TEXT,
                        FOREIGN KEY (student_id) REFERENCES Students(student_id))''')

    # Create CourseSchedules table
    cursor.execute('''CREATE TABLE IF NOT EXISTS CourseSchedules (
                        schedule_id INTEGER PRIMARY KEY,
                        course_id INTEGER NOT NULL,
                        day_of_week TEXT NOT NULL,
                        start_time TEXT NOT NULL,
                        end_time TEXT NOT NULL,
                        FOREIGN KEY (course_id) REFERENCES Courses(course_id))''')

    # create indexes tables
    indexes = [
        ('idx_student_id', 'Students(student_id)'),
        ('idx_course_id', 'Courses(course_id)'),
        ('idx_enrollment_id', 'Enrollments(enrollment_id)'),
        ('idx_accommodation_id', 'Accommodations(accommodation_id)'),
        ('idx_book_id', 'Books(book_id)'),
        ('idx_course_book_id', 'CourseBooks(course_book_id)'),
        ('idx_purchase_id', 'BookPurchases(purchase_id)'),
        ('idx_advisor_id', 'StudentAdvisors(advisor_id)'),
        ('idx_schedule_id', 'CourseSchedules(schedule_id)')
    ]

    for index_name, table_column in indexes:
        cursor.execute(f'''CREATE INDEX IF NOT EXISTS {index_name} ON {table_column}''')

    conn.commit()
    conn.close()

initialize_database()
