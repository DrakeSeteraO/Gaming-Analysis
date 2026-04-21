import random as rd
import sqlite3
from select_data import *

# Make sure to change these values
start_val = 2
amount = 99

with sqlite3.connect("gaming_info.db") as connection:
    cursor = connection.cursor()
    
    
    for i in range(start_val, start_val + amount):
        fname = rd.choice(FIRST_NAMES)
        cursor.execute("Insert Into User Values (?, ?, ?, ?, ?, ?, ?);", 
                       (i, f"{rd.choice(ADJECTIVES)} {fname}", rd.choice(STATES), fname, rd.choice(LAST_NAMES), f"https:www/{rd.randint(1, 1_000_000)}",  f"https:www/{rd.randint(1, 1_000_000)}"))
        
        cursor.execute("Insert Into Wallet Values (?, ?, ?, ?);", 
                       (rd.randint(1000000000000, 999999999999999), f"{rd.random()*100:.2f}", rd.choice(CARD_TYPES), rd.choice(BANK_NAMES)))
        
        cursor.execute("Insert Into Game Values (?, ?, ?);", 
                       (i, f"{rd.choice(GENRES)} {rd.choice(NOUNS)}", f"{rd.randint(1,12)}-{rd.randint(1,31)}-{rd.randint(1960, 2026)}"))
        
        for j in range(rd.randint(1,len(PLATFORMS))):
            cursor.execute("Insert Into Platform Values (?, ?);", 
                        (i, rd.choice(PLATFORMS)))
        
        for j in range(rd.randint(1,i)):
            cursor.execute("Insert Into UserGame Values (?, ?, ?, ?);", 
                        (i, rd.randint(1, i),rd.randint(0, 100_000), f"{rd.randint(1,12)}-{rd.randint(1,31)}-{rd.randint(1960, 2026)}"))
        
        for j in range(rd.randint(1, len(GENRES))):
            cursor.execute("Insert Into GenreGame Values (?, ?, ?);", 
                           (rd.randint(1, len(GENRES)-1), i, int(j == 0)))
        
        cursor.execute("Insert Into Developer Values (?, ?);",
                        (i, f"{rd.choice(ADJECTIVES)} {rd.choice(NOUNS)} Studio"))
        
        cursor.execute("Insert Into GameDeveloper Values (?, ?, ?);", 
                       (i, i, rd.random() * 100))
        