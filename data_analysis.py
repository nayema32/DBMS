import sys
print("Using Python interpreter at:", sys.executable)

import sqlite3
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Step 1: Create necessary tables and add fields
def create_test_scores_table():
    conn = sqlite3.connect('sichuan_university.db')
    cursor = conn.cursor()
    cursor.execute('''
    CREATE TABLE IF NOT EXISTS TestScores (
        student_id INTEGER,
        course_id INTEGER,
        score INTEGER,
        PRIMARY KEY (student_id, course_id),
        FOREIGN KEY (student_id) REFERENCES Students(student_id),
        FOREIGN KEY (course_id) REFERENCES Courses(course_id)
    )
    ''')
    conn.commit()
    conn.close()
    print("TestScores table created successfully.")

def add_columns_to_students():
    conn = sqlite3.connect('sichuan_university.db')
    cursor = conn.cursor()
    cursor.execute('ALTER TABLE Students ADD COLUMN birth_year INTEGER')
    cursor.execute('ALTER TABLE Students ADD COLUMN region TEXT')
    conn.commit()
    conn.close()
    print("Columns birth_year and region added to Students table successfully.")

def populate_test_scores():
    conn = sqlite3.connect('sichuan_university.db')
    cursor = conn.cursor()
    test_scores = [
        (1, 101, 85),
        (2, 102, 90),
        (3, 103, 75),
        # Add more sample test scores
    ]
    cursor.executemany('''INSERT INTO TestScores (student_id, course_id, score) VALUES (?, ?, ?)''', test_scores)
    conn.commit()
    conn.close()
    print("Sample test scores inserted successfully.")

def update_students_with_new_data():
    conn = sqlite3.connect('sichuan_university.db')
    cursor = conn.cursor()
    cursor.execute('''UPDATE Students SET birth_year = 2000, region = 'North' WHERE student_id = 1''')
    cursor.execute('''UPDATE Students SET birth_year = 2001, region = 'South' WHERE student_id = 2''')
    cursor.execute('''UPDATE Students SET birth_year = 2002, region = 'East' WHERE student_id = 3''')
    # Add more updates as needed
    conn.commit()
    conn.close()
    print("Students table updated with birth_year and region data successfully.")

create_test_scores_table()
add_columns_to_students()
populate_test_scores()
update_students_with_new_data()

# Step 2: Data analysis and reporting

# Load data into Pandas DataFrame
conn = sqlite3.connect('sichuan_university.db')

students_df = pd.read_sql_query("SELECT * FROM Students", conn)
enrollments_df = pd.read_sql_query("SELECT * FROM Enrollments", conn)
courses_df = pd.read_sql_query("SELECT * FROM Courses", conn)
accommodations_df = pd.read_sql_query("SELECT * FROM Accommodations", conn)
book_purchases_df = pd.read_sql_query("SELECT * FROM BookPurchases", conn)
test_scores_df = pd.read_sql_query("SELECT * FROM TestScores", conn)

conn.close()

# Analysis 1: Number of students and gender ratio for each major
gender_ratio = students_df.groupby(['major', 'gender']).size().unstack(fill_value=0)
print(gender_ratio)
gender_ratio.plot(kind='bar', stacked=True)
plt.title('Gender Ratio per Major')
plt.xlabel('Major')
plt.ylabel('Number of Students')
plt.show()

# Analysis 2: Comparison of results in different majors
average_scores = test_scores_df.groupby('course_id')['score'].mean()
average_scores.plot(kind='bar')
plt.title('Average Test Scores per Course')
plt.xlabel('Course ID')
plt.ylabel('Average Score')
plt.show()

# Analysis 3: Relationship between student age and test scores
students_df['age'] = 2024 - students_df['birth_year']
age_scores_df = pd.merge(students_df[['student_id', 'age']], test_scores_df[['student_id', 'score']], on='student_id')
sns.scatterplot(data=age_scores_df, x='age', y='score')
plt.title('Relationship between Age and Test Scores')
plt.xlabel('Age')
plt.ylabel('Test Score')
plt.show()

# Analysis 4: Relationship between students' regional distribution and test scores
region_scores_df = pd.merge(students_df[['student_id', 'region']], test_scores_df[['student_id', 'score']], on='student_id')
region_avg_scores = region_scores_df.groupby('region')['score'].mean()
region_avg_scores.plot(kind='bar')
plt.title('Average Test Scores by Region')
plt.xlabel('Region')
plt.ylabel('Average Score')
plt.show()

# Analysis 5: Other analysis (Example: Distribution of test scores)
sns.histplot(test_scores_df['score'], bins=10, kde=True)
plt.title('Distribution of Test Scores')
plt.xlabel('Test Score')
plt.ylabel('Frequency')
plt.show()
