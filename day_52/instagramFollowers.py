from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class InstaFollower:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)

    def login(self, username, password):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(2)
        email_input = self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Phone number, username, or email"]')
        email_input.send_keys(username)
        password_input = self.driver.find_element(By.CSS_SELECTOR, '[aria-label="Password"]')
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        sleep(2)

    def find_followers(self):
        self.driver.get("https://www.instagram.com/chefsteps/")
        sleep(2)
        follower_button = self.driver.find_element(By.XPATH, '/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[2]/section/main/div/header/section/ul/li[2]/button')
        follower_button.click()
        sleep(2)
        self.follow()

    def follow(self):
        follow_box = self.driver.find_element(By.CLASS_NAME, "_aano")
        follow_buttons = self.driver.find_elements(By.CSS_SELECTOR, "._aano button")
        for button in follow_buttons:
            button.click()
            sleep(1.1)
        self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", follow_box)


