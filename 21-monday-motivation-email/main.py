import smtplib
import datetime as dt
import random

MY_EMAIL = ""
PASSWORD = ""


def email_sender():
    with open("quotes.txt", mode="r") as quotes:
        quotes_list = list(quotes)
        today_q = random.choice(quotes_list)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{today_q}"
        )
    print("sent")


now = dt.datetime.now()
today = now.weekday()
if today == 0:
    email_sender()





