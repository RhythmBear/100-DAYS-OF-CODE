import requests
import smtplib
from datetime import datetime

MY_EMAIL = 'eoadepoju10@gmail.com'
MY_PASSWORD = 'Oluwaseyi10.'
RECIPIENT_EMAIL = "femiemmanuel1990@gmail.com"

MY_LAT = 7.452929
MY_LONG = 3.911148

response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()
data = response.json()

iss_latitude = float(data["iss_position"]["latitude"])
iss_longitude = float(data["iss_position"]["longitude"])

#Your position is within +5 or -5 degrees of the ISS position.


def chk_pos():
    if iss_longitude - 5.0 < MY_LONG < iss_longitude + 5.0:
        if iss_latitude - 5.0 < MY_LAT < iss_latitude + 5.0:
            return True
        else:
            return False
    else:
        return False


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

print(sunrise)
print(sunset)

time_now = datetime.now()
current_hour = time_now.hour
print(current_hour)

#If the ISS is close to my current position
if not chk_pos():
    if time_now.hour > sunset or time_now.hour < 5:
        print("look up to the sky")
    else:
        print("it's still daytime you cannot see the ISS")

# and it is currently dark
# Then send me an email to tell me to look up.
    try:
        with smtplib.SMTP("smtp.gmail.com", 587) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=MY_PASSWORD)
            connection.sendmail(from_addr=MY_EMAIL,
                                to_addrs=RECIPIENT_EMAIL,
                                msg="Subject: THE ISS IS ABOVE YOU \n\n"
                                    "Look Up to the sky. You should be able to spot the ISS")

    except:
        print("Failed to send Email")
    else:
        print("Email Delivered Successfully")


# BONUS: run the code every 60 seconds.



