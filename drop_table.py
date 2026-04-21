import sqlite3

with sqlite3.connect("gaming_info.db") as connection:
    cursor = connection.cursor()
    cursor.execute("Drop Table GameToDeveloper;")