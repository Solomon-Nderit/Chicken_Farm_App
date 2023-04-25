import sqlite3

with sqlite3.connect('chicken_farm.db') as db:
    curs=db.cursor()

curs.execute("""CREATE TABLE IF NOT EXISTS chicken_houses(
            id integer PRIMARY KEY AUTOINCREMENT,
            name text NOT NULL,
            population integer NOT NULL,
            feeds float DEFAULT 0,
            medicine text DEFAULT 'none'

            )""")
db.commit()

curs.execute("""CREATE TABLE IF NOT EXISTS feeds(
            id integer PRIMARY KEY AUTOINCREMENT,
            name text NOT NULL,
            quantity text NOT NULL,
            remaining float DEFAULT 0
            
           
)""")

curs.execute("""CREATE TABLE IF NOT EXISTS egg_collected(
                id integer PRIMARY KEY AUTOINCREMENT,
                date text NOT NULL,
                house text ,
                number INTEGER DEFAULT 0)""")
                


db.commit()
db.close()
#Wanted to create a new row in feeds_medical_recordss to store feed quantity.
