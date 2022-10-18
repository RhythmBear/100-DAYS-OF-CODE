import requests
import datetime as dt

# response = requests.get(url="http://api.open-notify.org/iss-now.json")
# response.raise_for_status()
# response_json = response.json()
# iss_location = (response_json["iss_position"]["latitude"],response_json["iss_position"]["longitude"])
#
# print(iss_location)
MY_LAT = 6.811898
MY_LNG = 6.750110

current_dt = dt.datetime.now()
current_hour = cuurent_dt.hour

response = requests.get("https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()


data = response.json()
sunrise_time = data["results"]["sunrise"]
sunset_time = data["results"]["sunset"]

print(sunrise_time)
print(sunset_time)

sunrise = sunrise_time.split("T")[1].split("+")[0]
sunrise_hour = int(sunrise.split(":")[0])

sunset = sunset_time.split("T")[1].split("+")[0]
sunset_hour = int(sunset.split(":")[0])

print(type(sunset_hour))
print(sunrise_hour)
