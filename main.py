import pandas
import datetime as dt
import smtplib
from random import choice


# 2. Check if today matches a birthday in the birthdays.csv
dataframe = pandas.read_csv('birthdays.csv')
dates = dataframe.to_dict(orient='records')
letters = None
sender_email = 'sender@email.com'
pwd = 'password_of_the_sender'
today = dt.datetime.now()

today_birthdays = [x for x in dates if x['month'] == today.month and x['day'] == today.day]

if len(today_birthdays) > 0:
    with open('./letter_templates/letter_1.txt') as lt:
        lt1 = lt.read()
    with open('./letter_templates/letter_2.txt') as lt:
        lt2 = lt.read()
    with open('./letter_templates/letter_3.txt') as lt:
        lt3 = lt.read()
    letters = [lt1, lt2, lt3]

if letters is not None:
    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user=sender_email, password=pwd)
        for x in today_birthdays:
            chosen_letter = choice(letters)
            lt_to_send = chosen_letter.replace('[NAME]', x['name'])
            connection.sendmail(from_addr=sender_email, to_addrs='notification@email.com',
                                msg=f"Subject:BD\n\nIt is {x['name']}'s Birthday")
            connection.sendmail(from_addr=sender_email, to_addrs=x['email'],
                                msg=f'Subject:Happy Birthday!\n\n{lt_to_send}'
                                )
