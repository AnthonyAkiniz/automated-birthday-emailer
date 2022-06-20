# Automated Birthday Emailer
Checks a csv list of birthdays against today's date and will insert their name and email into a random birthday letter template and send them an e-mail wishing them a Happy Birthday. 

# Requirements
rename project folder to whatever you prefer: automated-birthday-emailer<br>
cd into project folder: cd automated-birthday-emailer<br>

# Google Gmail Account
Enable 2-Step Verification on your Gmail Account (required to get an App Password)<br>
Gmail App Password (lets you sign in with apps like Python scripts)<br>
Gmail app password setup: https://myaccount.google.com/apppasswords<br>
documentation: https://support.google.com/accounts/answer/185833<br>

# Guide
1. Update the birthdays.csv file to your other email address with today's date.<br>
   This will create an entry that can send right away to verify it's working for you.<br>
   It is designed to only send an e-mail on the day that is their birthday.<br>
   If multiple people have a birthday on the same day, it will email all of them.<br>
2. Update your Gmail Address and App Password in 4 spots marked in the code with arrows.<br>
3. Launch by clicking run button in top right in VSCode or: py -3 main.py<br>
4. Can verify sent by viewing your sent folder on your e-mail used.<br>
5. After initial test, can modify/add letters in the letter_templates folder.<br>
