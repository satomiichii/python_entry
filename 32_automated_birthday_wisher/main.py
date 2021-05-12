import smtplib
import datetime as dt
import random
import pandas

my_email = 'YOUR_EMAIL.com'
password = 'YOUR_EMAIL_PASSWORD'
email_server = 'smtp.gmail.com'

# ################## Extra Hard Starting Project ###################

# 1. Update the birthdays.csv > Done

# 2. Check if today matches a birthday in the birthdays.csv

now = dt.datetime.now()
month = now.month
date = now.day

print(month, date)

data = pandas.read_csv('birthdays.csv')
bd_list = data.to_dict(orient='records')
bd_is_today = []


def is_today_birthday():
    global bd_is_today, month, date
    for bd in bd_list:
        if bd['month'] == month and bd['day'] == date:
            bd_is_today.append(bd)
    return len(bd_is_today) != 0


# 3. If step 2 is true, pick a random letter from
# letter templates and replace the [NAME] with the person's actual name from birthdays.csv
if is_today_birthday():
    random_idx = random.randint(1, 3)
    with open(f'letter_templates/letter_{random_idx}.txt') as letter:
        letter_template = letter.read()

# 4. Send the letter generated in step 3 to that person's email address.
    with smtplib.SMTP(email_server) as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        for person in bd_is_today:
            new_message = letter_template.replace('[NAME]', person['name'])
            connection.sendmail(from_addr=my_email,
                                to_addrs=person['email'],
                                msg=f"Subject:Happy Birthday! \n\n {new_message}")


# now = dt.datetime.now()
# day_of_week = now.weekday()
# print(day_of_week)
#
# if day_of_week == 2:
#     with open('quotes.txt') as data:
#         quotes_list = data.readlines()
#         random_quote = random.choice(quotes_list)
#     with smtplib.SMTP('YOUR_EMAIL_SERVER') as connection:
#         connection.starttls()
#         connection.login(user=my_email, password=password)
#         connection.sendmail(from_addr=my_email, to_addrs='YOUR_FRIEND_EMAIL',
#                             msg=f"Subject:This week's quote\n\n{random_quote}")
#
#
