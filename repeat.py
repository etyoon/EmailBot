import schedule
import time
import send_mail

schedule.every(2).days.do(send_mail.send_mail())

while True:
    schedule.run_pending()
    time.sleep(1)
