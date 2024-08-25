from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import os

ACCOUNT_EMAIL = os.environ.get("ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = os.environ.get("ACCOUNT_PASSWORD")

# Keep Chrome browser open after program finishes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://www.tinder.com")

# Maximize the window
driver.maximize_window()

sleep(2)
login_button = driver.find_element(By.XPATH, '//*[@id="u849573418"]/div/div[1]/div/main/div[1]/div/div/div/div/'
                                             'div/header/div/div[2]/div[2]/a/div[2]/div[2]/div')
login_button.click()

sleep(2)
fb_login = driver.find_element(By.XPATH, '//*[@id="u-878807658"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span'
                                         '/div[2]/button/div[2]/div[2]')
fb_login.click()

sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

sleep(2)
decline_button = driver.find_element(By.XPATH, '//*[@id="facebook"]/body/div[2]/div[2]/div/div/div/div/div[3]/'
                                               'div[2]/div/div[1]/div[2]/div')
decline_button.click()

sleep(2)
email_input = driver.find_element(By.NAME, 'email')
email_input.send_keys(ACCOUNT_EMAIL)

pass_input = driver.find_element(By.NAME, 'pass')
pass_input.send_keys(ACCOUNT_PASSWORD)

submit_input = driver.find_element(By.ID, 'loginbutton')
submit_input.click()
