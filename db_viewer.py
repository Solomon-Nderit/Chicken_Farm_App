import sqlite3
import numpy as np
import time
from email.message import EmailMessage
import ssl
import smtplib

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
    total_chicken=np.sum(chicken_population)
    print("\nTotal Population: %d" %total_chicken)

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
    total_eggs=np.sum(egg_totals)
    print(f"\nThe current total eggs collected since {first_date} is {total_eggs}")
    time.sleep(2)

    print("""\n3.Feeds records: \n""")
    time.sleep(0.5)
    curs.execute("SELECT * FROM feeds")
    for i in curs.fetchall():
        print(i)
    time.sleep(2)

    def emailer(email):
        email_sender = 'cluckcontrol@gmail.com'
        email_password=input('Enter password: ')
        email_receiver=(email)

        body= (f'The current  total chicken population is {total_chicken} and the current egg totals are {total_eggs}')

        em=EmailMessage()
        em['From']=email_sender
        em['To']=email_receiver

        em['Subject']='Farm Records'
        em.set_content(body)

        context=ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com',465,context=context) as smtp:
            try:
                smtp.login(email_sender,email_password)
                smtp.sendmail(email_sender,email_receiver,em.as_string())
                print("All good sir")
            except:
                print('Error! Mail not sent')
    
    user_email=input('Enter your email to recieve a condensed form of the data:  ')
    emailer(user_email)
            









def main():
    print("Here is an overview of all your farm. Please enter which table you would like to see more information about.")
    time.sleep(1.5)
    view()
    
    




