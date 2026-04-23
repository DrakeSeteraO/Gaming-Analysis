import sqlite3

with sqlite3.connect("gaming_info.db") as connection:
    cursor = connection.cursor()
    
    # 2. 4.
    # Max difference in playtime between users per game
    # Maybe don't include this because of duplicates causing problems
    command = """
    select a.gameID as game_ID, a.steamID as User_A, b.steamID as User_B, max(a.playTime - b.playTime) as max_time_difference from UserGame a, UserGame b where a.gameID = b.gameID group by a.gameID;
    """
    
    cursor.execute(command)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    
    # 2. 4.
    # Average difference in playtime between users per game
    command = """
    select a.gameID as game_ID, avg(a.playTime - b.playTime) as avg_time_difference from UserGame a, UserGame b where a.gameID = b.gameID and a.playtime > b.playtime group by a.gameID;
    """
    
    cursor.execute(command)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    
    # 4. 6.
    # Average difference in playtime between users per game
    command = """
    select c.firsname as first_name, c.lastname as last_name, c.username as username from Game a, UserGame b, User c where b.steamID = c.steamID and a.gameID = b.gameID and a.title = 'Puzzle Dog' and playTime > (select avg(playTime) from UserGame a, Game b where a.gameID = b.gameID and b.title = 'Puzzle Dog');
    """
    
    cursor.execute(command)
    rows = cursor.fetchall()
    for row in rows:
        print(row)