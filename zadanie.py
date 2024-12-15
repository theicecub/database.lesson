import sqlite3

connection = sqlite3.connect("books.db")

cur = connection.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS books(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT,
        author TEXT
    );
""")

# cur.execute("INSERT INTO books (title, author) VALUES ('Test', 'Test Testovich');")
# cur.execute("INSERT INTO books (title, author) VALUES ('Test1', 'Test Testovich Junior');")
# cur.execute("INSERT INTO books (title, author) VALUES ('Test2', 'Test Testovich Mini');")

cur.execute("SELECT * FROM books;")

books = cur.fetchall()

for i in books:
    print(i)

connection.commit()
connection.close()