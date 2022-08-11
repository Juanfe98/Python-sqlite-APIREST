import sqlite3

connection = sqlite3.connect('data.db')

cursor = connection.cursor()

create_table = "CREATE TABLE users (id int, username text, password text)"
cursor.execute(create_table)


user = (1, "Jose", "Pass")
insert_query = "INSERT INTO users (id, username, password) VALUES (?,?,?)"
cursor.execute(insert_query, user)


users = [
    (2, "Pedro", "Pass"),
    (3, "Carlos", "Pass")
]
cursor.executemany(insert_query, users)


getAllUsers = "SELECT * FROM users"

for row in cursor.execute(getAllUsers):
    print(row)


connection.commit()
connection.close()