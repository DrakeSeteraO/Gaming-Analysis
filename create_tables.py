import sqlite3

with sqlite3.connect("gaming_info.db") as connection:
    cursor = connection.cursor()
    
    # Wallet Table
    command = """
    Create Table If Not Exists Wallet(
        cardNumber Integer(19) Primary Key,
        money Decimal(10,2),
        cardType Text(10),
        bankName Text(50)
        );"""
    cursor.execute(command)

    # User Table
    command = """
    Create Table If Not Exists User(
        steamID Integer Primary Key,
        username Text(50),
        state Text(2),
        firsname Text(50),
        lastname Text(50),
        profileURL Text(50),
        avatar Text(50),
        cardNumber Integer References Wallet(cardNumber)
        );"""
    cursor.execute(command)
    
    # Game Table
    command = """
    Create Table If Not Exists Game(
        gameID Integer Primary Key,
        title Text(40),
        datePublished Text(10)
        );"""
    cursor.execute(command)
    
    
    # Platform Table
    command = """
    Create Table If Not Exists Platform(
        gameID Integer References Game(gameID),
        platformType Text
        );"""
    cursor.execute(command)
    
    
    # UserGame Table
    command = """
    Create Table If Not Exists UserGame(
        steamID Integer References User(SteamID),
        gameID Integer References Game(gameID),
        playTime Integer,
        datePurchased Text(10)
        );"""
    cursor.execute(command)
    
    
    # Genre Table
    command = """
    Create Table If Not Exists Genre(
        genreID Integer Primary Key,
        genreName Text(40)
        );"""
    cursor.execute(command)
    
    
    # GenreGame
    command = """
    Create Table If Not Exists GenreGame(
        genreID Integer References Genre(genreID),
        gameID Integer References Game(gameID),
        isPrimary Text(1)
        );"""
    cursor.execute(command)
    
    
    # Developer Table
    command = """
    Create Table If Not Exists Developer(
        devID Integer Primary Key,
        devName Text(40)
        );"""
    cursor.execute(command)
    
    
    # GameDeveloper Table
    command = """
    Create Table If Not Exists GameDeveloper(
        gameID Integer References Game(gameID),
        devID Integer References Developer(devID),
        percentRevShared Decimal
        );"""
    cursor.execute(command)