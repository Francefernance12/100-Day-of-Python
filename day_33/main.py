import requests
from datetime import datetime
import smtplib
import time
from os import getenv
from dotenv import load_dotenv

load_dotenv()

# Data
MY_LAT = 00.00  # Your latitude
MY_LONG = 00.00  # Your longitude
EMAIL = 'example01@example.com'  # placeholder
RECIPIENT = 'example@example.com'  # placeholder
PASSWORD = 'App Password Here' # placeholder


# checks if the ISS is close your location
def is_iss_close():
    try:
        response = requests.get(url=getenv("ISS_API_URL"))
        response.raise_for_status()
        data = response.json()

        iss_latitude = float(data["iss_position"]["latitude"])
        iss_longitude = float(data["iss_position"]["longitude"])

        if MY_LAT - 5 <= iss_latitude <= MY_LAT + 5 and MY_LONG - 5 <= iss_longitude <= MY_LONG + 5:
            return True, iss_latitude, iss_longitude
        return False, None, None
    except requests.RequestException as e:
        print(f"Error fetching ISS data: {e}")
        return False, None, None


# collects data of your sunset and sunrise time in your area
def is_night():
    parameters = {
        "lat": MY_LAT,
        "lng": MY_LONG,
        "formatted": 0,
    }

    # collecting the sunrise and sunset hours
    response = requests.get(getenv("SUNRISE_API_URL"), params=parameters)
    response.raise_for_status()
    data = response.json()
    sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
    sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])
    return sunset, sunrise


# will continue to check if its nighttime and the ISS is close to your location for every minute
while True:
    # current time
    print("test")
    time_now = datetime.now()
    is_close, iss_latitude, iss_longitude = is_iss_close()
    sunset, sunrise = is_night()
    if is_close and (sunset <= time_now.hour < sunrise):
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()  # secures connection by making the email encrypted
            connection.login(user=EMAIL, password=PASSWORD)
            connection.sendmail(from_addr=EMAIL, to_addrs=RECIPIENT,
                                msg=f"Subject:ISS here! Look Up!\n\n I am around "
                                    f"your area. My latitude: {iss_latitude}. My "
                                    f"Longitude: {iss_longitude}")
    time.sleep(60)
