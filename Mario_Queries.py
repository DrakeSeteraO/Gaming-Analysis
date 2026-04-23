import sqlite3

with sqlite3.connect("gaming_info.db") as connection:
    cursor = connection.cursor()
    
    # 1. 4-table join
    # Find each user's name, the games they own, the genre of each game, and the developer who made it
    command = """
    select u.firstname, u.lastname, g.title, gr.genreName, d.devName
    from User u 
    join UserGame ug on u.steamID = ug.steamID
    join Game g on ug.gameID = g.gameID
    join GenreGame gg on g.gameID = gg.gameID
    join Genre gr on gg.genreID = gr.genreID
    join GameDeveloper gd on g.gameID = gd.gameID
    join Developer d on gd.devID = d.devID
    where gg.isPrimary = 'Y'
    order by u.lastname, g.title
    limit 10;
    """
    cursor.execute(command)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # 5. Union
    # Find users with over 2k hours of playtime combined with devs who have a less than average revenue share
    command = """
    select u.username, 'High Playtime User' as catergory
    from User u
    join UserGame ug on u.steamID = ug.steamID
    where ug.playTime > 2000
    union
    select d.devName, 'Low Revenue Share Dev'
    from Developer d
    join GameDeveloper gd on d.devID = gd.devID
    where gd.percentRevShared < (select avg(percentRevShared) from GameDeveloper)
    limit 10;
    """
    cursor.execute(command)
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    # 6. Group by, having, order by
    # Find developers who have an average revenue share above 50%, ordered from highest to lowest
    command = """
    select d.devName, round(avg(gd.percentRevShared), 2) as avgRevShare
    from Developer d
    join GameDeveloper gd on d.devID = gd.devID
    group by d.devName
    having avg(gd.percentRevShared) > 50
    order by avgRevShare desc
    limit 10;
    """
    
    cursor.execute(command)
    rows = cursor.fetchall()
    for row in rows:
        print(row)