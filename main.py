#########################################################################################
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
# * ################################################################################# * #
# * #                         Automated Birthday Emailer                            # * #
# * #                         project by: Anthony Akiniz                            # * #
# * #                          github.com/anthonyakiniz                             # * #
# * ################################################################################# * #
# * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * * #
#########################################################################################
# Info:                                                                                 #
# Checks a csv list of birthdays against today's date and will insert their name and    #
# email into a random birthday letter template and send them an e-mail wishing          #
# them a Happy Birthday.                                                                #
#                                                                                       #
# Requirements:                                                                         #
# rename project folder to whatever you prefer: automated-birthday-emailer              #
# cd into project folder: cd automated-birthday-emailer                                 #
#                                                                                       #
# Google Gmail Account:                                                                 #
# Enable 2-Step Verification on your Gmail Account (required to get an App Password)    #
# Gmail App Password (lets you sign in with apps like Python scripts)                   #
# Gmail app password setup: https://myaccount.google.com/apppasswords                   #
# documentation: https://support.google.com/accounts/answer/185833                      #
#                                                                                       #
# Guide:                                                                                #
# 1. Update the birthdays.csv file to your other email address with today's date.       #
#    This will create an entry that can send right away to verify it's working for you. #
#    It is designed to only send an e-mail on the day that is their birthday.           #
#    If multiple people have a birthday on the same day, it will email all of them.     #
# 2. Update your Gmail Address and App Password in 4 spots marked below with arrows.    #
# 3. Launch by clicking run button in top right in VSCode or: py -3 main.py             #
# 4. Can verify sent by viewing your sent folder on your e-mail used.                   #
# 5. After initial test, can modify/add letters in the letter_templates folder.         #
#########################################################################################

import datetime as dt
import random
import smtplib
import pandas

letters_and_email_dict = {}
FROM_EMAIL = "Your Gmail Address"  # <-- Update #1 of 4
PASSWORD = "Your Gmail APP Password"  # <-- Update #2 of 4


# checks today's date against birthday.csv
file = pandas.read_csv('birthdays.csv')
birthday_details = file.to_dict(orient='records')

now = dt.datetime.now()
current_month = now.month
current_day = now.day

for detail in range(len(birthday_details)):
    birthday = birthday_details[detail]
    if birthday['month'] == current_month and birthday['day'] == current_day:
        NAME = birthday['name']
        TO_EMAIL = birthday['email']


# if it's their birthday, inserts their name into a random letter
        with open(f'letter_templates/letter_{random.randint(1, 3)}.txt') as selected_letter:
            letter = selected_letter.read()
            updated_letter = letter.replace('[NAME]', NAME)
            # verifies correct emailid matches letter
            letters_and_email_dict[updated_letter] = TO_EMAIL


# sends letter as email
for (letter, to_email) in letters_and_email_dict.items():

    with smtplib.SMTP('smtp.gmail.com') as connection:
        connection.starttls()
        connection.login(user="Your Gmail Address",  # <-- Update #3 of 4
                         password="Your Gmail APP Password")  # <-- Update #4 of 4
        connection.sendmail(from_addr=FROM_EMAIL,
                            to_addrs=to_email,
                            msg=f"Subject:Happy Birthday!!!\n\n{letter}")

# message prints only in terminal to confirm ran successfully
print("All E-Mails Successfully Sent")
