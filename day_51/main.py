from os import getenv
from dotenv import load_dotenv
from internetProvider import InternetSpeedTwitterBot

load_dotenv()

# Secrets
USERNAME = getenv('USER_NAME')
PASSWORD = getenv('PASSWORD')
print(USERNAME)
print(PASSWORD)

# Checking Internet Speed
twitter_bot = InternetSpeedTwitterBot()
download_speed, upload_speed = twitter_bot.get_internet_speed()
print(download_speed)
print(upload_speed)
# check if the speed is what you paid for
if download_speed <= 50 and upload_speed <= 50:
    twitter_bot.tweet_at_provider(USERNAME, PASSWORD, download_speed, upload_speed)

