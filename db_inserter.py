import sqlite3
with sqlite3.connect('chicken_farm.db') as db:
    cursor=db.cursor()

def insert():
    cursor.execute("SELECT * FROM chicken_houses")
    for i in cursor.fetchall():
        print(i)

    def house_table_inserter():
        user_in=int(input("How many new records would you  like to enter? "))
        for i in range(0,user_in):
            name=input("Enter house name: ")
            population=input("Enter the population: ")
            feeds=float(input("Enter the feeds(in terms of mkebes): "))
            medicine=input("Enter any medication: ")
            cursor.execute("INSERT INTO chicken_houses(name,population,feeds,medicine)VALUES(?,?,?,?)",[name,population,feeds,medicine])
        db.commit()
        cursor.execute("SELECT * FROM chicken_houses")
        for i in cursor.fetchall():
            print(i)
        db.close()
    def eggs_table_inserter():
        user_in=int(input("How many new records would you  like to enter? "))
        for i in range(0,user_in):
            house=input("Enter house name: ")
            number=int(input("Enter eggs collected: "))
            date = input("Enter today's date: ")
            cursor.execute("INSERT INTO egg_collected(house,number,date)VALUES(?,?,?)",[house,number,date])
        db.commit()
        cursor.execute("SELECT * FROM chicken_houses")
        for i in cursor.fetchall():
            print(i)
        db.close()