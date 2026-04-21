import sqlite3

with sqlite3.connect("gaming_info.db") as connection:
    cursor = connection.cursor()
    
    table_names = ["User",
                   "Wallet",
                   "Game",
                   "Platform",
                   "UserGame",
                   "Genre",
                   "GenreGame",
                   "Developer",
                   "GameDeveloper"]
    
    for table_name in table_names:
        
        cursor.execute(f"select * from {table_name};" )
        rows = cursor.fetchall()
        
        print(f"\n{table_name}: ")
        for row in rows:
            print(row)