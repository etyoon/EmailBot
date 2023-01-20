import smtplib
from email.message import EmailMessage
import ssl
import bot
from datetime import date

email = {'ethan': 'etyoon06@gmail.com', 'aman': 'amanshah@uchicago.edu', 'jai': 'jaisahni@uchicago.edu', 'adit': 'adit19@uchicago.edu'}
email_sender = 'Dorchester5623@gmail.com'
body = {'T': " It's your turn to take out the trash",
'D': " It's your turn to take out the dishes"}

def go():
    chores = bot.update()
    print(chores)
    for item in chores:
        msg = EmailMessage()
        msg['Subject'] = "Chores for " + str(date.today())
        person, chore = item
        msg['To'] = email[person]
        msg['From'] = email_sender
        msg.set_content("Hi " + str(person) + body[chore])

        context = ssl.create_default_context()

        with smtplib.SMTP_SSL('smtp.gmail.com', 465, context=context) as smtp:
            smtp.login(email_sender, 'azmuulilkcptbaed')
            smtp.sendmail(email_sender, email[person], msg.as_string())
    
    print('Done')

go()
