import requests
from twilio.rest import Client

MY_PHONE_NUMBER = "+2347080304532"


# Twilio Account
MY_ACCOUNT_SID = "ACc0d617f3c2fe7c20630cc447683652b9"
MY_AUTH_TOKEN = "88afaea9937dbe15930b16658f2a4a26"
MY_TWILIO_PHONE = "+17073833614"

#  Open Weather Map Variables
LAT_TEST = 39.647099
LONG_TEST = 66.960289
MY_LAT = 7.348720
MY_LONG = 3.879290
API_KEY = "dd8274bccf3e42bed35622bbc1bee89e"

PARAMETERS = {"lat": MY_LAT,
              "lon": MY_LONG,
              "appid": API_KEY,
              "exclude": "minutely,current,daily"
              }

response = requests.get("https://api.openweathermap.org/data/2.5/onecall", params=PARAMETERS)
response.raise_for_status()
weather = response.json()
print("Data Successfully retrieved from API")

hourly_data = weather["hourly"]

print(len(hourly_data))

for i in hourly_data[:12]:
    print()
    code = i["weather"][0]["id"]

    if code <= 600:
        print("Come out with an umbrella")

        client = Client(MY_ACCOUNT_SID, MY_AUTH_TOKEN)
        message = client.messages.create(
            body="It's most Likely Going to Rain today. Take an Umbrella☂️if you'll be going out. ",
            from_=MY_TWILIO_PHONE,
            to=MY_PHONE_NUMBER
        )

        print(message.status)
