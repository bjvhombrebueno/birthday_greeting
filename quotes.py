import smtplib
import random
my_email = "glaucous.zaffre@gmail.com"
my_password = "dbopkxpkzqwmbvlh"



import datetime as dt
now = dt.datetime.now()
if now.weekday() == 0:
    with open("quotes.txt") as my_quotes:
        quotes_list = my_quotes.readlines()
        send_quote = random.choice(quotes_list)
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=my_password)
            connection.sendmail(from_addr=my_email, to_addrs="ben.bonulo@hotmail.com", msg=f"Subject:Inspo\n\n{send_quote}")
