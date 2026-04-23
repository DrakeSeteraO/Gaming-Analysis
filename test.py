import sqlite3

# Do not run this code it is use to delete stuff
with sqlite3.connect("gaming_info.db") as connection:
    cursor = connection.cursor()
    cursor.execute("ALTER TABLE User RENAME COLUMN  firsname TO firstname;")