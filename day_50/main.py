from os import getenv
from dotenv import load_dotenv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep


load_dotenv()


# secrets
FB_PHONE_NUMBER = getenv('PHONE_NUMBER')
FB_PASSWORD = getenv('PASSWORD')

# keep window open
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

# starts the window
driver = webdriver.Chrome(options=chrome_options)
driver.get("https://tinder.com/")


### facebook login ###
sleep(2)
login_button = driver.find_element(By.XPATH, '//*[text()="Log in"]')
login_button.click()

sleep(2)
facebook_login = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span/div[2]/button/div[2]/div[2]/div/div/div')
facebook_login.click()
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)

# Switch to Facebook login window
sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# Login and hit enter
email_entry = driver.find_element(By.ID, 'email')
password_entry = driver.find_element(By.ID, 'pass')
email_entry.send_keys(FB_PHONE_NUMBER)
password_entry.send_keys(FB_PASSWORD)
password_entry.send_keys(Keys.ENTER)

# Switch back to Tinder window
sleep(2)
driver.switch_to.window(base_window)
print(driver.title)

# dismissing popup
sleep(2)
allow_loc = driver.find_element(By.CSS_SELECTOR, '[aria-label="Allow"]')
accept_cookie = driver.find_element(By.XPATH, '/html/body/div[2]/div/div[2]/div/div/div[1]/div[1]/button/div[2]/div[2]')
accept_cookie.click()
allow_loc.click()
sleep(1)
miss_out = driver.find_element(By.CSS_SELECTOR, '[aria-label="I’ll miss out"]')
miss_out.click()

# Declining

for _ in range(95):
    try:
        sleep(2)
        nope = driver.find_element(By.CSS_SELECTOR, '#u-684883901 > div > div.App__body.H\(100\%\).Pos\(r\).Z\(0\) > div > main > div.H\(100\%\) > div > div > div.Mt\(a\).Px\(4px\)--s.Pos\(r\).Expand.H\(--recs-card-height\)--ml.Maw\(--recs-card-width\)--ml > div.recsCardboard__cardsContainer.H\(100\%\).Pos\(r\).Z\(1\) > div > div.Pos\(a\).B\(0\).Iso\(i\).W\(100\%\).Start\(0\).End\(0\) > div > div.Mx\(a\).Fxs\(0\).Sq\(70px\).Sq\(60px\)--s.Bd.Bdrs\(50\%\).Bdc\(\$c-ds-border-gamepad-nope-default\)')
        nope.click()
    except ElementClickInterceptedException:
        try:
            # add tinder popup
            not_interested = driver.find_element(By.CSS_SELECTOR, '#u1881702319 > div > div > div.Pt\(12px\).Pb\(8px\).Px\(36px\)--ml.Px\(24px\) > button.c1p6lbu0.D\(b\).Mx\(a\)')
            not_interested.click()
        except NoSuchElementException:
            sleep(2)


driver.quit()

