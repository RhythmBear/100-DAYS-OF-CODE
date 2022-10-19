import requests
import datetime as dt
# Creating the User's Profile

pixela_endpoint = "https://pixe.la/v1/users"
# Set pixela token in enviroment variabe=les before running.
pixela_token = os.getenv('pixela_token')
pixela_username = "rhythmbear"

pixela_params = {
    "token": pixela_token,
    "username": pixela_username,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"

}

#
# response = requests.post(pixela_endpoint, json=pixela_params)
# print(response.text)

# Creating new graph on the User's account
graph_endpoint = f"{pixela_endpoint}/{pixela_username}/graphs"
graph_parameters = {
    "id": "hourlygraph1",
    "name": "Coding Habit",
    "unit": "hours",
    "type": "int",
    "color": "momiji"

}

headers = {
    "X-USER-TOKEN": "Okechukwu"
}

#
# new_response = requests.post(url=graph_endpoint, json=graph_parameters, headers=headers)
# print(new_response.text)


# Creating new pixels for the user's account

new_pixel_url = f"{graph_endpoint}/{graph_parameters[ 'id']}"

date_raw = dt.datetime.now().date()
date = date_raw.strftime("%Y%m%d")

print(date)

yesterday_raw = dt.datetime(year=date_raw.year, month=date_raw.month, day=date_raw.day - 1)
model_date = yesterday_raw.strftime("%Y%m%d")

print(model_date)

token_requests_params = {
    "date": model_date,
    "quantity": "2",
}

# pixel_response = requests.post(url=new_pixel_url, json=token_requests_params, headers=headers)
# print(pixel_response.text)

# Edit yesterday's data

put_url = f"https://pixe.la/v1/users/{pixela_username}/graphs/{graph_parameters['id']}/{model_date}"

put_json = {
    "quantity": "3"
}
update_response = requests.put(url=put_url, json=put_json, headers=headers)
print(update_response.text)
