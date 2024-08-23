from os import getenv
from dotenv import load_dotenv
from instagramFollowers import InstaFollower

load_dotenv()

# Secrets
USERNAME = getenv('USER_NAME')
PASSWORD = getenv('PASSWORD')

instaFollower = InstaFollower()
instaFollower.login(USERNAME, PASSWORD)
instaFollower.find_followers()

