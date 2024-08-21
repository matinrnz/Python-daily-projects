from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

# Keep Chrome browser open after program finishes
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("detach", True)

driver = webdriver.Chrome(options=chrome_options)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")

# Hone in on anchor tag using CSS selectors
# article_count = driver.find_element(By.CSS_SELECTOR, value="#articlecount a")
# print(article_count.text)
# driver.quit()
# article_count.click()

# Find element by Link Text
# all_portals = driver.find_element(By.LINK_TEXT, value="Content portals")
# all_portals.click()

# Find the "Search" <input> by Name
# search_button = driver.find_element(By.XPATH, value='//*[@id="p-search"]/a/span[1]')
# search_button.click()
# search = driver.find_element(By.NAME, value="search")

# Sending keyboard input to Selenium
# search.send_keys("Python", Keys.ENTER)

driver.get("https://secure-retreat-92358.herokuapp.com/")
first_name = driver.find_element(By.NAME, value="fName")
last_name = driver.find_element(By.NAME, value="lName")
email = driver.find_element(By.NAME, value="email")
submit = driver.find_element(By.TAG_NAME, value="button")
first_name.send_keys("M")
last_name.send_keys("MM")
email.send_keys("MM@MM.com")
submit.click()
