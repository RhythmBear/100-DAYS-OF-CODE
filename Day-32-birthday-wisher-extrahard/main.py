import random
import pandas
import datetime as dt
import smtplib

MY_EMAIL = "eoadepoju10@gmail.com"
PASSWORD = "Oluwaseyi10."
recipient_mail = ""
recipient_name = ""

# #################### Extra Hard Starting Project ######################

# 1. Update the birthdays.csv

df = pandas.read_csv("birthdays.csv", index_col=False)
print(df.to_string())
esther_data = df[df.name == "Esther"]
bd_dict = {(df.month[ind], df.day[ind]): {"Name": df.name[ind], "Email": df.email[ind]} for ind in df.index}
print(bd_dict)

# 2. Check if today matches a birthday in the birthdays.csv
now = dt.datetime.now()
current_month = now.month
current_day = now.day
today_date = (current_month, current_day)

if today_date in bd_dict:
    recipient_details = (bd_dict[today_date])
    recipient_mail = recipient_details["Email"]
    recipient_name = recipient_details["Name"]
    message = f"Today is {recipient_name}'s Birthday. Send an Email to {recipient_mail}."
    print(message)

# 3. If step 2 is true, pick a random letter from letter templates and replace the [NAME] with the person's actual name
# from birthdays.csv
    with open(f"letter_templates/letter_{random.randint(1,3)}.txt") as file:
        letter = file.read()
        birthday_message = letter.replace("[NAME]", recipient_name)
        print(birthday_message)

    # 4. Send the letter generated in step 3 to that person's email address.
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=recipient_mail,
                                msg=f"Subject:Happy Birthday! \n\n{birthday_message}")

    except TimeoutError:
        print("failed to send email.")
    else:
        print(f"Letter successfully delivered to {recipient_mail}")

else:
    print("NO Birthday's Today")