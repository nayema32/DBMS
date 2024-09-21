import sqlite3

##f1: Student to choose course
def enroll_student_in_course(student_id, course_id, enrollment_date):
    conn = sqlite3.connect('sichuan_university.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Enrollments (student_id, course_id, enrollment_date) VALUES (?, ?, ?)''',
                   (student_id, course_id, enrollment_date))
    conn.commit()
    conn.close()
    print("Student enrolled in course successfully.")

# Example usage
enroll_student_in_course(1, 101, '2024-01-10')
# Example 1: Enroll a student in another course
enroll_student_in_course(2, 102, '2024-02-15')

# Example 2: Enroll a different student in a course
enroll_student_in_course(3, 103, '2023-12-20')

# Example 3: Enroll a student in a course with a different enrollment date
enroll_student_in_course(4, 101, '2024-03-05')

# Example 4: Enroll a student in multiple courses
enroll_student_in_course(5, 104, '2024-04-01')
enroll_student_in_course(5, 105, '2024-04-01')

# Example 5: Enroll a student in a course with a different course ID
enroll_student_in_course(6, 106, '2024-02-28')

# Example 6: Enroll a student in a course with a different student ID and enrollment date
enroll_student_in_course(7, 107, '2024-03-15')

# Example 7: Enroll a student in a course with a different course ID and enrollment date
enroll_student_in_course(8, 108, '2024-04-20')

##f2: Student accommodation related information management
def assign_accommodation(student_id, dorm_number, room_number, start_date, end_date):
    conn = sqlite3.connect('sichuan_university.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO Accommodations (student_id, dorm_number, room_number, start_date, end_date) VALUES (?, ?, ?, ?, ?)''',
                   (student_id, dorm_number, room_number, start_date, end_date))
    conn.commit()
    conn.close()
    print("Accommodation assigned successfully.")

# Example usage
# Example 1: Assign accommodation to another student in a different dorm and room
assign_accommodation(2, "Dorm B", "201", '2024-02-01', '2024-12-31')

# Example 2: Assign accommodation to a different student with a different room number and dates
assign_accommodation(3, "Dorm A", "102", '2024-03-01', '2024-12-31')

# Example 3: Assign accommodation to a student in a different dorm, room, and dates
assign_accommodation(4, "Dorm C", "301", '2024-04-01', '2024-12-31')

# Example 4: Assign accommodation to a student with a different start date and end date
assign_accommodation(5, "Dorm A", "103", '2024-05-01', '2024-08-31')

# Example 5: Assign accommodation to another student with different dorm, room, and dates
assign_accommodation(6, "Dorm B", "202", '2024-06-01', '2024-12-31')

# Example 6: Assign accommodation to a student with a different room number and end date
assign_accommodation(7, "Dorm A", "104", '2024-07-01', '2024-11-30')

# Example 7: Assign accommodation to another student in a different dorm and room with different dates
assign_accommodation(8, "Dorm C", "302", '2024-08-01', '2024-10-31')

##f3: Students buy books for the related course
def purchase_book(student_id, book_id, purchase_date):
    conn = sqlite3.connect('sichuan_university.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO BookPurchases (student_id, book_id, purchase_date) VALUES (?, ?, ?)''',
                   (student_id, book_id, purchase_date))
    conn.commit()
    conn.close()
    print("Book purchased successfully.")

# Example usage
purchase_book(1, 1001, '2024-01-15')

# Book Return
def return_book(student_id, book_id, return_date):
    conn = sqlite3.connect('sichuan_university.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO BookReturns (student_id, book_id, return_date) VALUES (?, ?, ?)''',
                   (student_id, book_id, return_date))
    conn.commit()
    conn.close()
    print("Book returned successfully.")

# Example usage
return_book(1, 1001, '2024-02-15')

# Book Borrow
def borrow_book(student_id, book_id, borrow_date, due_date):
    conn = sqlite3.connect('sichuan_university.db')
    cursor = conn.cursor()
    cursor.execute('''INSERT INTO BookBorrows (student_id, book_id, borrow_date, due_date) VALUES (?, ?, ?, ?)''',
                   (student_id, book_id, borrow_date, due_date))
    conn.commit()
    conn.close()
    print("Book borrowed successfully.")

# Example usage
borrow_book(2, 1002, '2024-03-01', '2024-04-01')

# Functions to view the changes in the database

def view_enrollments():
    conn = sqlite3.connect('sichuan_university.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM Enrollments''')
    enrollments = cursor.fetchall()
    conn.close()
    return enrollments

def view_accommodations():
    conn = sqlite3.connect('sichuan_university.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM Accommodations''')
    accommodations = cursor.fetchall()
    conn.close()
    return accommodations

def view_book_purchases():
    conn = sqlite3.connect('sichuan_university.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM BookPurchases''')
    book_purchases = cursor.fetchall()
    conn.close()
    return book_purchases

def view_book_returns():
    conn = sqlite3.connect('sichuan_university.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM BookReturns''')
    book_returns = cursor.fetchall()
    conn.close()
    return book_returns

def view_book_borrows():
    conn = sqlite3.connect('sichuan_university.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM BookBorrows''')
    book_borrows = cursor.fetchall()
    conn.close()
    return book_borrows

# View changes
print("Enrollments:")
enrollments = view_enrollments()
for enrollment in enrollments:
    print(enrollment)

print("\nAccommodations:")
accommodations = view_accommodations()
for accommodation in accommodations:
    print(accommodation)

print("\nBook Purchases:")
book_purchases = view_book_purchases()
for purchase in book_purchases:
    print(purchase)

print("\nBook Returns:")
book_returns = view_book_returns()
for book_return in book_returns:
    print(book_return)

print("\nBook Borrows:")
book_borrows = view_book_borrows()
for borrow in book_borrows:
    print(borrow)
