from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

ACCOUNT_EMAIL = "EMAIL"
ACCOUNT_PASSWORD = 'PW'

# Keep Chrome browser open after program finishes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=python%20developer&"
           "location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

# Reject Cookies
time.sleep(2)
reject_button = driver.find_element(by=By.CSS_SELECTOR, value='button[action-type="DENY"]')
reject_button.click()

# Sign in Button
time.sleep(2)
sign_in = driver.find_element(By.CLASS_NAME, value="job-alert-redirect-section__cta")
sign_in.click()

# Sign in
time.sleep(5)
username = driver.find_element(By.ID, value="username")
username.send_keys(ACCOUNT_EMAIL)
password = driver.find_element(By.ID, value="password")
password.send_keys(ACCOUNT_PASSWORD)
password.send_keys(Keys.ENTER)
