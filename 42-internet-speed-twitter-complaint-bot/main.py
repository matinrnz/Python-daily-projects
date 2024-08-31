from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

PROMISED_DOWN = 150
PROMISED_UP = 10
CHROME_DRIVER_PATH = os.environ.get("CHROME_DRIVER_PATH")
TWITTER_EMAIL = os.environ.get("TWITTER_EMAIL")
TWITTER_PASSWORD = os.environ.get("TWITTER_PASSWORD")
TWITTER_USERNAME = os.environ.get("TWITTER_USERNAME")


class InternetSpeedTwitterBot:
    def __init__(self, driver_path=None):
        service = Service(executable_path=driver_path)
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        sleep(10)
        reject_button = self.driver.find_element(By.XPATH, '//*[@id="onetrust-reject-all-handler"]')
        reject_button.click()
        sleep(5)
        go_button = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]'
                                                       '/div[1]/a/span[4]')
        go_button.click()
        sleep(80)
        self.down = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]'
                                                       '/div[3]/div/div[3]/div/div/div[2]/div[1]/div[1]/div/div[2]')
        self.up = self.driver.find_element(By.XPATH, '//*[@id="container"]/div/div[3]/div/div/div/div[2]/div[3]/'
                                                     'div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]')
        return self.down.text, self.up.text

    def tweet_at_provider(self):
        self.driver.get("https://x.com/")
        sleep(5)
        refuse = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[1]/div/div/div/div[2]/button[2]/div')
        refuse.click()
        sleep(5)
        close = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div/div[2]/div/div/div/button/div')
        close.click()
        sleep(5)
        sign_in = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/div/div/div[2]/main/div/div/div[1]/div'
                                                     '/div/div[3]/div[3]/a')
        sign_in.click()
        sleep(12)
        email = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]/div'
                                                   '/div/div[2]/div[2]/div/div/div/div[4]/label/div/div[2]/div/input')
        email.send_keys(TWITTER_EMAIL)
        sleep(8)
        next_button = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/'
                                                         'div[2]/div/div/div[2]/div[2]/div/div/div/button[2]/div')
        next_button.click()
        sleep(8)
        username = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]'
                                                      '/div/div/div[2]/div[2]/div[1]/div/div[2]/label/div/div[2]/div/'
                                                      'input')
        username.send_keys(TWITTER_USERNAME)
        username.send_keys(Keys.ENTER)
        sleep(8)
        password = self.driver.find_element(By.XPATH, '//*[@id="layers"]/div[2]/div/div/div/div/div/div[2]/div[2]'
                                                      '/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/'
                                                      'div[2]/div[1]/input')
        password.send_keys(TWITTER_PASSWORD)
        password.send_keys(Keys.ENTER)
        sleep(10)


bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
result = bot.get_internet_speed()
down = float(result[0])
up = float(result[1])
print(f"down: {down}\nup: {up}")
if down < PROMISED_DOWN or up < PROMISED_UP:
    print('oh!')
    bot.tweet_at_provider()
