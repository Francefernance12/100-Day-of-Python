from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep


class InternetSpeedTwitterBot:

    def __init__(self):
        self.chrome_options = webdriver.ChromeOptions()
        self.chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=self.chrome_options)
        self.download = None
        self.upload = None

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net")
        sleep(2)
        go = self.driver.find_element(By.CSS_SELECTOR, '.start-text')
        go.click()
        sleep(60)  # wait for diagnostics
        self.download = float(self.driver.find_element(By.CSS_SELECTOR, '.result-item-container-align-center .result-data > span').text)
        self.upload = float(self.driver.find_element(By.CSS_SELECTOR, '.result-item-container-align-left .result-data > span').text)
        return self.download, self.upload

    def tweet_at_provider(self, username, password, down_spd, up_spd):
        self.driver.get("https://twitter.com/home")
        # login to twitter
        sleep(5)
        username_input = self.driver.find_element(By.CSS_SELECTOR, '.css-175oi2r input')
        username_input.send_keys(username)
        username_input.send_keys(Keys.ENTER)
        sleep(2)
        password_input = self.driver.find_element(By.CSS_SELECTOR, '#layers > div > div > div > div > div > div > div.css-175oi2r.r-1ny4l3l.r-18u37iz.r-1pi2tsx.r-1777fci.r-1xcajam.r-ipm5af.r-g6jmlv.r-1awozwy > div.css-175oi2r.r-1wbh5a2.r-htvplk.r-1udh08x.r-1867qdf.r-kwpbio.r-rsyp9y.r-1pjcn9w.r-1279nm1 > div > div > div.css-175oi2r.r-1ny4l3l.r-6koalj.r-16y2uox.r-kemksi.r-1wbh5a2 > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-1jgb5lz.r-13qz1uu.r-1ye8kvj > div.css-175oi2r.r-16y2uox.r-1wbh5a2.r-1dqxon3 > div > div > div.css-175oi2r.r-mk0yit.r-13qz1uu > div > label > div > div.css-175oi2r.r-18u37iz.r-16y2uox.r-1wbh5a2.r-1wzrnnt.r-1udh08x.r-xd6kpl.r-1pn2ns4.r-ttdzmv > div.css-1rynq56.r-bcqeeo.r-qvutc0.r-37j5jr.r-135wba7.r-16dba41.r-1awozwy.r-6koalj.r-1inkyih.r-13qz1uu > input')
        password_input.send_keys(password)
        password_input.send_keys(Keys.ENTER)
        # Writing the tweet
        sleep(5)
        print(f'@Verizon Hey Verizon, Why is my internet speed {down_spd}down/{up_spd}up when I pay up to 100down/50up')
        tweet_input = self.driver.find_element(By.CSS_SELECTOR, '#react-root > div > div > div.css-175oi2r.r-1f2l425.r-13qz1uu.r-417010.r-18u37iz > main > div > div > div > div.css-175oi2r.r-kemksi.r-1kqtdi0.r-13l2t4g.r-1ljd8xs.r-1phboty.r-16y2uox.r-184en5c.r-61z16t.r-11wrixw.r-1jgb5lz.r-13qz1uu.r-1ye8kvj > div > div.css-175oi2r.r-kemksi.r-184en5c > div > div.css-175oi2r.r-kemksi.r-1h8ys4a > div:nth-child(1) > div > div > div > div.css-175oi2r.r-1iusvr4.r-16y2uox.r-1777fci.r-1h8ys4a.r-1bylmt5.r-13tjlyg.r-7qyjyx.r-1ftll1t > div:nth-child(1) > div > div > div > div > div > div > div > div > div > div > label > div.css-175oi2r.r-1wbh5a2.r-16y2uox > div > div > div > div > div > div.DraftEditor-editorContainer > div > div > div > div')
        tweet_input.send_keys(f'@Verizon Hey Verizon, Why is my internet speed {down_spd}down/{up_spd}up when I pay up to 100down/50up')


