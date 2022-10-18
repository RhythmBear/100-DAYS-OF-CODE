from smtplib import SMTP


def send_email(name, phone_number, email_adr, message):
    MY_EMAIL = "eoadepoju10@gmail.com"
    MY_PASSWORD = "Oluwaseyi10."

    try:
        with SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL,
                             password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs="femiemmanuel1990@gmail.com",
                                msg=f"""Subject:Email From BLog \n\n
                                        Name: {name}
                                        Email: {email_adr}
                                        Phone Number: {phone_number}
                                        MESSAGE: {message}
                                     """
                                )
    except TimeoutError:
        return "Failed"
    else:
        return "Successful"

