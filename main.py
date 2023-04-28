import sqlite3
import db_table_creator
import db_inserter
import numpy as np
import db_viewer


with sqlite3.connect('chicken_farm.db') as db:
    curs=db.cursor()


def main():
    user_in=input("""             WELCOME
    
                    1.View Chicken records
                    2.Modify Chicken record
                    
                    Input: """)

    if user_in=='1':
        db_viewer.view() 
    if user_in=='2':
        db_inserter.main()

main()