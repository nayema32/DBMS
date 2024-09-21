import sqlite3
import threading

def query_db(query, params=()):
    conn = sqlite3.connect('sichuan_university.db')
    cursor = conn.cursor()
    cursor.execute(query, params)
    results = cursor.fetchall()
    conn.close()
    return results

def concurrent_query(student_id):
    query = 'SELECT * FROM Students WHERE student_id = ?'
    results = query_db(query, (student_id,))
    print(f"Result from Thread-{student_id}: {results}")

threads = []

# to create threads for student ID 1 to 5
for i in range(1, 6):
    thread = threading.Thread(target=concurrent_query, args=(i,))
    threads.append(thread)
    thread.start()

# to wait till all the thread completion
for thread in threads:
    thread.join()
