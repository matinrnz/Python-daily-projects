import datetime as dt
import pandas
import random
import smtplib

MY_EMAIL = ""
PASSWORD = ""

# 1. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
today = (now.month, now.day)

# 2. Use pandas to read the birthdays.csv and dictionary comprehension to create a dictionary
data = pandas.read_csv("birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}

# 3. If there is a match, pick a random letter (letter_1.txt/letter_2.txt/letter_3.txt) from letter_templates and
# replace the [NAME] with the person's actual name from birthdays.csv
if today in birthdays_dict:
    rand_letter = f"letter_templates/letter_{random.randint(1, 3)}.txt"
    with open(rand_letter) as file:
        letter = file.read()
        processed_letter = letter.replace("[NAME]", birthdays_dict[today]["name"])
        # 4. Send the letter generated in step 3 to that person's email address.
        try:
            with smtplib.SMTP("smtp.gmail.com") as connection:
                connection.starttls()
                connection.login(user=MY_EMAIL, password=PASSWORD)
                connection.sendmail(
                    from_addr=MY_EMAIL,
                    to_addrs=MY_EMAIL,
                    msg=f"Subject:Happy Birthday!\n\n{processed_letter}"
                )
                print("Sent")
        except smtplib.SMTPException as e:
            print(f"Failed to send email: {e}")

