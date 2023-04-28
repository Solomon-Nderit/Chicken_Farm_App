import sqlite3
with sqlite3.connect('chicken_farm.db') as db:
    cursor=db.cursor()

def creator():
        #View all the tables in the database
        cursor.execute("SELECT * FROM chicken_houses")
        for i in cursor.fetchall():
            print(i)
        cursor.execute("SELECT * FROM eggs_collected")
        for i in cursor.fetchall():
            print(i)
        cursor.execute("SELECT * FROM feeds")
        for i in cursor.fetchall():
            print(i)

        #The function for inserting new records in the chicken table
        def house_table_creator():
            user_in=int(input("How many new records would you  like to enter? "))
            
            #We ask the user how many records they want to create and create a for loop for asking for input that number of times
            for i in range(0,user_in):
                name=input("Enter house name: ")
                population=input("Enter the population: ")
                feeds=float(input("Enter the feeds(in terms of mkebes): "))
                medicine=input("Enter any medication: ")
                cursor.execute("INSERT INTO chicken_houses(name,population,feeds,medicine)VALUES(?,?,?,?)",[name,population,feeds,medicine])
                db.commit()
            #Display the entire table just to see the changes
            cursor.execute("SELECT * FROM chicken_houses")
            for i in cursor.fetchall():
                print(i)
            db.close()

        #Function for inserting new records in eggs table
        #Follows the same outline as the chicken table
        def eggs_table_creator():
            user_in=int(input("How many new records would you  like to enter? "))
            for i in range(0,user_in):
                house=input("Enter house name: ")
                number=int(input("Enter eggs collected: "))
                date = input("Enter today's date: ")
                cursor.execute("INSERT INTO egg_collected(house,number,date)VALUES(?,?,?)",[house,number,date])
            db.commit()
            cursor.execute("SELECT * FROM egg_collected")
            for i in cursor.fetchall():
                print(i)
            db.close()
            
        #Function for inserting new records in the feeds table
        #Follows same layout as the precious two functions
        def feeds_table_creator():
            user_in=eval(input('How many new records would you like to enter? '))
            for i in range(0,user_in):
                  feeds=input('Enter feeds name: ')
                  quantity=input("Enter quantity bought: ")
                  remaining=eval(input("Enter amount left in kilograms: "))
                  cursor.execute("INSERT INTO feeds(name,quantity,remaining)VALUES(?,?,?)",[feeds,quantity,remaining])
            db.commit()
            cursor.execute("SELECT * FROM feeds ")
            for i in cursor.fetchall():
                print(i)
            db.close()

        #Ask the user which table they would like to modify and call the respective function
        table=input("""Which table would you like to modify?
                    
                        1. The Chicken Houses
                        2. Eggs
                        3. Feeds """)
        if table=="1":
            house_table_creator()
        elif table=="2":
                eggs_table_creator()
        elif table=="3":
             feeds_table_creator()
                
              

def main():
    #Give the user three choices between creating new records and the other clearly visible options.
    option=input("""Would you like to :
                    
                    1. Create new records.
                    2. Modify existing information
                    3. Delete existing information? 
                    """)
    if option=="1":
        creator()
        