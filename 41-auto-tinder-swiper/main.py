from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from time import sleep
import os

ACCOUNT_EMAIL = os.environ.get("ACCOUNT_EMAIL")
ACCOUNT_PASSWORD = os.environ.get("ACCOUNT_PASSWORD")

# Keep Chrome browser open after program finishes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
driver.get("http://www.tinder.com")

# Maximize the window
driver.maximize_window()

sleep(2)
login_button = driver.find_element(By.XPATH, '//*[@id="u849573418"]/div/div[1]/div/main/div[1]/div/div/div/div/'
                                             'div/header/div/div[2]/div[2]/a/div[2]/div[2]/div')
login_button.click()

sleep(3)
decline = driver.find_element(By.XPATH, '//*[@id="u-878807658"]/div/div[2]/div/div/div[1]/div[2]/button/div[2]/'
                                        'div[2]/div')
decline.click()

# Login with Facebook
# sleep(2)
# fb_login = driver.find_element(By.XPATH, '//*[@id="u-878807658"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/span'
#                                          '/div[2]/button/div[2]/div[2]')
# fb_login.click()
#
# # Switch to Facebook login window
# sleep(2)
# base_window = driver.window_handles[0]
# fb_login_window = driver.window_handles[1]
# driver.switch_to.window(fb_login_window)
# print(driver.title)
#
# sleep(2)
# decline_button = driver.find_element(By.XPATH, '//*[@id="facebook"]/body/div[2]/div[2]/div/div/div/div/div[3]/'
#                                                'div[2]/div/div[1]/div[2]/div')
# decline_button.click()
#
# # Login and hit enter
# sleep(2)
# email_input = driver.find_element(By.NAME, 'email')
# email_input.send_keys(ACCOUNT_EMAIL)
#
# pass_input = driver.find_element(By.NAME, 'pass')
# pass_input.send_keys(ACCOUNT_PASSWORD)
# pass_input.send_keys(Keys.ENTER)
#
# # Switch back to Tinder window
# driver.switch_to.window(base_window)
# print(driver.title)
#
# # Allow location
# allow_location = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
# allow_location.click()
#
# # Disallow notifications
# notifications = driver.find_element(By.XPATH,'//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
# notifications.click()
#
# # Allow cookies
# cookies = driver.find_element(By.XPATH,'//*[@id="content"]/div/div[2]/div/div/div[1]/button')
# cookies.click()


# Login with Google
# Switching back to the default content
# Switch to the first iframe on the page (index starts at 0)
driver.switch_to.frame(0)
sleep(10)

google_button = driver.find_element(By.XPATH, '//*[@id="container"]/div/div[2]/span[1]')
google_button.click()

# Switch to Google login window
sleep(2)
login_window = driver.window_handles[1]
driver.switch_to.window(login_window)

# Email and hit next
sleep(6)
email_input = driver.find_element(By.XPATH, '//*[@id="identifierId"]')
email_input.send_keys(ACCOUNT_EMAIL)
email_input.send_keys(Keys.ENTER)
