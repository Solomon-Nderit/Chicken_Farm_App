import sqlite3
import numpy as np
import time

with sqlite3.connect('chicken_farm.db') as db:
    curs=db.cursor()

def view():
    ls1=[]
    curs.execute("SELECT * FROM chicken_houses")
    for i in curs.fetchall():
        print(i)
    time.sleep(2)
    
    query='''SELECT population FROM chicken_houses WHERE id>0'''
    curs.execute(query)
    for i in curs.fetchall():
        ls1.append(i)
    total=np.sum(ls1)
    print("Current chicken population: %d" %total)

    



