from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementClickInterceptedException, NoSuchElementException
from time import sleep
import os

FB_EMAIL = os.environ.get("FB_EMAIL")
FB_PASSWORD = os.environ.get("FB_PASSWORD")

# Keep Chrome browser open after program finishes.
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrome_options)
driver.get("http://www.tinder.com")

# Maximize the window
driver.maximize_window()

# Click login
sleep(2)
login_button = driver.find_element(By.XPATH, '//*[@id="c-351009880"]/div/div[1]/div/main/div[1]/div/div/div/div/'
                                             'div/header/div/div[2]/div[2]/a/div[2]/div[2]')
login_button.click()

# Facebook loginsleep92
sleep(2)
fb_login = driver.find_element(By.XPATH, '//*[@id="c-2079390956"]/div/div[1]/div/div[1]/div/div/div[2]/div[2]/'
                                         'span/div[2]/button/div[2]/div[2]')
fb_login.click()

# Switch to Facebook login window
sleep(2)
base_window = driver.window_handles[0]
fb_login_window = driver.window_handles[1]
driver.switch_to.window(fb_login_window)
print(driver.title)

# Decline cookies
sleep(2)
decline_button = driver.find_element(By.XPATH, '//*[@id="facebook"]/body/div[2]/div[2]/div/div/div/div/div[3]/'
                                               'div[2]/div/div[1]/div[2]/div')
decline_button.click()

# Login and hit enter
sleep(2)
email_input = driver.find_element(By.NAME, 'email')
email_input.send_keys(FB_EMAIL)
pass_input = driver.find_element(By.NAME, 'pass')
pass_input.send_keys(FB_PASSWORD)
pass_input.send_keys(Keys.ENTER)

# Switch back to Tinder window
sleep(2)
driver.switch_to.window(base_window)
print(driver.title)

# Allow location
sleep(5)
allow_location_button = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
allow_location_button.click()
# Disallow notifications
notifications_button = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notifications_button.click()
# Allow cookies
cookies = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()


for n in range(100):
    # 1-second delay between likes.
    sleep(1)
    try:
        print("called")
        like_button = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]'
                                                    '/div/div[2]/div[4]/button')
        like_button.click()

    # Catches the cases where there is a "Matched" pop-up in front of the "Like" button:
    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()

        # Catches the cases where the "Like" button has not yet loaded, so wait 2 seconds before retrying.
        except NoSuchElementException:
            sleep(2)

driver.quit()
