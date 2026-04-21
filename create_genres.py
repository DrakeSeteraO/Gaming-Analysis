from select_data import *
import sqlite3

with sqlite3.connect("gaming_info.db") as connection:
    cursor = connection.cursor()
    for i in range(len(GENRES)):
        cursor.execute("Insert Into Genre Values (?, ?);",
                       (i+1, GENRES[i]))