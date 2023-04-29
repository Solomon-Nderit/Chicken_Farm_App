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
                

def deleter():
    def house_table_deleter():
        print("Here is the entire Chicken Table:\n")
        cursor.execute("SELECT * FROM chicken_houses WHERE id>0")
        for i in cursor.fetchall():
               print(i)
        user_id=int(input("Enter the id of the record you wish to delete: "))
        cursor.execute(f"DELETE FROM chicken_houses WHERE id = {user_id}")
        db.commit()

        cursor.execute("SELECT * FROM chicken_houses")
        for i in cursor.fetchall():
             print(i)
    def egg_table_deleter():
        print("Here is the entire Eggs Table:\n")
        cursor.execute("SELECT * FROM egg_collected WHERE id>0")
        for i in cursor.fetchall():
               print(i)
        user_id=int(input("Enter the id of the record you wish to delete: "))
        cursor.execute(f"DELETE FROM egg_collected WHERE id = {user_id}")
        db.commit()

        cursor.execute("SELECT * FROM egg_collected")
        for i in cursor.fetchall():
             print(i)

    def feeds_table_deleter():
        print("Here is the entire Feeds Table:\n")
        cursor.execute("SELECT * FROM feeds WHERE id>0")
        for i in cursor.fetchall():
               print(i)
        user_id=int(input("Enter the id of the record you wish to delete: "))
        cursor.execute(f"DELETE FROM feeds WHERE id = {user_id}")
        db.commit()

        cursor.execute("SELECT * FROM feeds")
        for i in cursor.fetchall():
             print(i)



    user_in=input("""\nWhich table do you want to modify?
                    
                        1. Chicken Houses 
                        2. Eggs collected
                        3. Feeds 
                        > """)
    if user_in=="1":
         house_table_deleter()
    elif user_in=="2":
         egg_table_deleter()
    elif user_in=="3":
         feeds_table_deleter()
    
        

def modifier():
    print("""  WELCOME! HERE IS AN OVERVIEW OF THE TABLES. WHICH WOULD YOU LIKE TO MODIFY?
                1. Chicken
                  \n""")
    cursor.execute("SELECT * FROM chicken_houses")
    for i in cursor.fetchall():
            print(i)

    print("\n2. Eggs: \n")
    cursor.execute("SELECT * FROM eggs_collected")
    for i in cursor.fetchall():
        print(i)
    
    print("\n3.Feeds:\n")
    cursor.execute("SELECT * FROM feeds")
    for i in cursor.fetchall():
            print(i)
    
    def house_table_modifier():
        user_input=input("""Which column would you like to modify? 
                            1.House Name
                            2. House Population
                            3. House Daily Feed
                            4. Medication
                            
                            Enter here: """)
        if user_input=="1":
             house_id=int(input("\nEnter the id of the house you would like to change name: "))
             new_name=input("Enter the new name: ")
             cursor.execute("UPDATE chicken_houses SET name = ? WHERE id = ?", (new_name, house_id))
             db.commit()
        
        elif user_input =="2":
             house_id=int(input("\nEnter the id of the house you would like to change population: "))
             new_population=eval(input("Enter the new population: "))
             cursor.execute("UPDATE chicken_houses SET population = ? WHERE id = ?", (new_population, house_id))
             db.commit()

        elif user_input=="3":
             house_id=int(input("\nEnter the id of the house you would like to change daily feed: "))
             new_feeds=eval(input("Enter the new daily feed in terms of mkebes: "))
             cursor.execute("UPDATE chicken_houses SET feeds = ? WHERE id = ?", (new_feeds, house_id))
        
        elif user_input=="4":
             house_id=int(input("\nEnter the id of the house you would like to change medication: "))
             new_medication=eval(input("Enter the new daily feed in terms of mkebes: "))
             cursor.execute("UPDATE chicken_houses SET medication = ? WHERE id = ?", (new_medication, house_id))
        else:
             print("Sorry! Currently Unavailable!")
        

    def egg_table_modifier():
        user_input=input("""\nWhich column would you like to modify? 
                            1.Date
                            2. House
                            3. Number
                            
                            Enter here: """)
        if user_input=="1":
             house_id=int(input("\nEnter the id of the house you would like to change date: "))
             new_date=eval(input("Enter the new date: "))
             cursor.execute("UPDATE egg_collected SET date = ? WHERE id = ?", (new_date, house_id))
             db.commit()
        
        elif user_input =="2":
             house_id=int(input("\nEnter the id of the record you would like to change house collected: "))
             new_house=eval(input("Enter the new house: "))
             cursor.execute("UPDATE egg_collected SET house = ? WHERE id = ?", (new_house, house_id))
             db.commit()

        elif user_input=="3":
             house_id=int(input("\nEnter the id of the house you would like to change number: "))
             new_number=eval(input("Enter the new daily feed in terms of mkebes: "))
             cursor.execute("UPDATE egg_collected SET number = ? WHERE id = ?", (new_number, house_id))
             db.commit()
        
        else:
             print("Sorry! Currently Unavailable!")

    def feeds_table_modifier():
        user_input=input("""\nWhich column would you like to modify? 
                            1.Name
                            2. Quantity
                            3. Remaining
                            
                            Enter here: """)
        if user_input=="1":
             house_id=int(input("\nEnter the id of the record you would like to change name: "))
             new_name=eval(input("Enter the new name: "))
             cursor.execute("UPDATE feeds SET name = ? WHERE id = ?", (new_name, house_id))
             db.commit()
        
        elif user_input =="2":
             house_id=int(input("\nEnter the id of the record you would like to change quantity: "))
             new_quantity=eval(input("Enter the new quantity: "))
             cursor.execute("UPDATE feeds SET quantity = ? WHERE id = ?", (new_quantity, house_id))
             db.commit()

        elif user_input=="3":
             house_id=int(input("\nEnter the id of the record you would like to change amount remaining: "))
             new_remaining=eval(input("Enter the new amount remaining: "))
             cursor.execute("UPDATE feeds SET remaining = ? WHERE id = ?", (new_remaining, house_id))
             db.commit()
       
        else:
             print("Sorry! Currently Unavailable!")   


    user_in=input("\nEnter here: ")
    if user_in=="1":
         house_table_modifier()
    elif user_in=="2":
         egg_table_modifier()
    elif user_in=="3":
         feeds_table_modifier()
    else:
         print("Option Unavailable.")

     

def main():
    #Give the user three choices between creating new records and the other clearly visible options.
    option=input("""Would you like to :
                    
                    1. Create new records.
                    2. Modify existing information
                    3. Delete existing information? 
                    """)
    if option=="1":
        creator()
    if option=="2":
         modifier()
    elif option=="3":
         deleter()
        