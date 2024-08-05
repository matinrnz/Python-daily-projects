# Exercise tracking using Nutritionix and Sheety
import requests
from datetime import datetime
import os

SHEET_ENDPOINT = os.environ["ENV_SHEET_ENDPOINT"]
APP_ID = os.environ["ENV_APP_ID"]
API_KEY = os.environ["ENV_API_KEY"]
TOKEN = os.environ["ENV_TOKEN"]

exercise_endpoint = "https://trackapi.nutritionix.com//v2/natural/exercise"

GENDER = "female"
WEIGHT_KG = 50

exercise_text = input("Tell me which exercises you did: ")

# Nutritionix API Call
headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

exercise_params = {
    "query": exercise_text,
    "gender": GENDER,
    "weight_kg": WEIGHT_KG,
}

response = requests.post(url=exercise_endpoint, json=exercise_params, headers=headers)
result = response.json()


# Add a new row
today_date = datetime.now().strftime("%d/%m/%Y")
now_time = datetime.now().strftime("%X")

for exercise in result["exercises"]:
    sheet_inputs = {
        "workout": {
            "date": today_date,
            "time": now_time,
            "exercise": exercise["name"].title(),
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }

    # sheet_response = requests.post(url=SHEET_ENDPOINT, json=sheet_inputs)
    # print(sheet_response.text)

    # Bearer Token Authentication
    bearer_headers = {
        "Authorization": f"Bearer {TOKEN}"
    }
    sheet_response = requests.post(
        SHEET_ENDPOINT,
        json=sheet_inputs,
        headers=bearer_headers
    )
    print(f"Sheety Response: \n {sheet_response.text}")
