import requests
import datetime as dt

# Nutritionix Details
API_KEY = "991621dcaf81d6f452d925d5b3959a17"
APP_ID = "0d36815d"
URL = "https://trackapi.nutritionix.com/v2/natural/exercise"

X_APP_ID = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
    "x-remote-user-id": "0"
}

body = {
    "query": input("Tell me what exercise you did today : "),
    "gender": 'male'

}
response = requests.post(url=URL, json=body, headers=X_APP_ID)
exercise_json = response.json()['exercises']
# print(exercise_json, len(exercise_json))

# (name of event, num_of)calories, time)
activity_list = [{"date": dt.datetime.now().strftime("%d/%m/%Y"), "time": dt.datetime.now().strftime("%X"),
                "exercise": i['name'], "duration": i['duration_min'], "calories": i['nf_calories']} for i in exercise_json]

print("Data succesfully acquired and listed")

# Working with the sheety API

sheety_API = "https://api.sheety.co/6058f50226857081a997dc586d44aa18/workoutTracker/workouts"


for i in activity_list:
    body = {
        "workout": i
    }
    response_sheety = requests.post(url=sheety_API, json=body)
    print(response_sheety.text)


