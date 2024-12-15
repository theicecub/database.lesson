# import sqlite3

# #Connecting to data base
# connection = sqlite3.connect("student.db")

# print("Соединение с базой данных установлено")

# cut = connection.cursor()
# cut.execute("""
#     CREATE TABLE IF NOT EXISTS student(
#         id INTEGER PRIMARY KEY AUTOINCREMENT,
#         name TEXT,
#         age INTEGER
#     );
# """) #"PRIMARY KEY" делает поле уникальным

# # cut.execute("INSERT INTO student (name, age) VALUES ('Bob',14);")
# # cut.execute("INSERT INTO student (name, age) VALUES ('Obb',13);")
# # cut.execute("INSERT INTO student (name, age) VALUES ('Bbo',12);")

# #Читаем данные

# cut.execute("SELECT * FROM student;")

# student = cut.fetchall()

# cut.execute("UPDATE student SET age = 16 WHERE name = 'Bob';") #Меняет возраст боба

# for i in student:
#     print(i)


# #CRUD. Create. Read. Update. Delete.

# connection.commit()
# connection.close()