import sqlite3
import numpy as np
import time

with sqlite3.connect('chicken_farm.db') as db:
    curs=db.cursor()


def view():
    chicken_population=[]
    egg_totals=[]
    print(""" \n1.Current chicken population: \n""")
    time.sleep(0.5)
    curs.execute("SELECT * FROM chicken_houses")
    for i in curs.fetchall():
        print(i)
    time.sleep(2)
    
    query='''SELECT population FROM chicken_houses WHERE id>0'''
    curs.execute(query)
    for i in curs.fetchall():
        chicken_population.append(i)
    total=np.sum(chicken_population)
    print("\nTotal Population: %d" %total)

    print("""\n2.Eggs records: \n""")
    time.sleep(0.5)
    curs.execute("SELECT * FROM egg_collected")
    for i in curs.fetchall():
        print(i)
    time.sleep(2)

    query='''SELECT number from egg_collected WHERE id>0'''
    curs.execute(query)
    for i in curs.fetchall():
        egg_totals.append(i)
    curs.execute("SELECT date from egg_collected WHERE id=1")
    first_date=curs.fetchall()
    total=np.sum(egg_totals)
    print(f"\nThe current total eggs collected since {first_date} is {total}")
    time.sleep(2)

    print("""\n3.Feeds records: \n""")
    time.sleep(0.5)
    curs.execute("SELECT * FROM feeds")
    for i in curs.fetchall():
        print(i)
    time.sleep(2)






def main():
    print("Here is an overview of all your farm. Please enter which table you would like to see more information about.")
    time.sleep(1.5)
    view()
    




