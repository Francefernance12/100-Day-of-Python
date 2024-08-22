import pandas as pd
import datetime as dt
import smtplib
from random import randint

# email info
my_email = "test@example.com" # placeholder email
password = "Enter App Password"  # app password

# CSV Birthday Data
data = pd.read_csv("birthdays.csv")
data_list = data.values.tolist()
birthday_name = [name[0] for name in data_list]
birthday_email = [email[1] for email in data_list]
birthday_year = [year[2] for year in data_list]
birthday_month = [month[3] for month in data_list]
birthday_day = [day[4] for day in data_list]


# current time
current_date = dt.datetime.now()  # current date and time
current_year = current_date.year  # current year
current_month = current_date.month  # current month
current_day = current_date.day  # current day


place_holder = "[NAME]"  # placeholder used to replace text with name

for i in range(len(birthday_name)):
    if current_month == int(birthday_month[i]) and current_day == int(birthday_day[i]):

        # randomly chooses a letter sample
        random_letter_template = f"./letter_templates/letter_{randint(1, 3)}.txt"

        # grab content from the random_letter_template
        with open(random_letter_template, "r") as template:
            content = template.read()

        new_content = content.replace(place_holder, birthday_name[i])


# 4. Send the letter generated in step 3 to that person's email address.
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # secures connection by making the email encrypted
            connection.login(user=my_email, password=password)
            connection.sendmail(from_addr=my_email, to_addrs=birthday_email[i],
                                msg=f"Subject:Fake Birthday\n\n {new_content}")




