from dotenv import load_dotenv
from os import getenv
import requests
import datetime as dt

load_dotenv()

# Secret Info
APP_ID = getenv('APP_ID')
API_KEY = getenv('API_KEY')
USER_NAME = getenv('USER_NAME')
PASSWORD = getenv('PASSWORD')

# config info
gender = "male"
weight_kg = 68.0389
height_cm = 172.72
age = 22

# input
user_input = input("write down your exercise progress report: ")

# Domain/API Key
host_domain = "https://trackapi.nutritionix.com"
exercise_api_endpoint = f"{host_domain}/v2/natural/exercise"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

json_config = {
    "query": user_input,
    "gender": gender,
    "weight_kg": weight_kg,
    "height_cm": height_cm,
    "age": age
}

response = requests.post(exercise_api_endpoint, json=json_config, headers=headers)
result = response.json()
print(result)

############################# sheety ########################################
# time
current_date = dt.datetime.now().date()
formatted_date = current_date.strftime("%m/%d/%Y")
print(formatted_date)
current_time = dt.datetime.now().time()
formatted_time = current_time.strftime("%X")
print(formatted_time)

# sheety API
sheety_api = 'https://api.sheety.co/9248949dd1024b5119ac2642d3fd6d98/workoutHabits/workouts'


sheety_response = requests.get(sheety_api)
sheety_result = sheety_response.json()


# POST request
for exercise in result["exercises"]:
    sheety_post_config = {
        "workout": {
            "date": formatted_date,
            "time": formatted_time,
            "exercise": exercise["name"].title(),
            "duration": int(exercise["duration_min"]),
            "calories": int(exercise["nf_calories"])
        }
    }
    sheety_post = requests.post(sheety_api, json=sheety_post_config, auth=(USER_NAME, PASSWORD))
    print(sheety_post.text)
