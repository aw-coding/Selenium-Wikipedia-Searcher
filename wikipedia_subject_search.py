# Enter a topic to search Wikipedia for. Results will be shown in the console.
# This program is compatible with Wikipedia's current bot policies (robots.txt). Please use responsibly.


from selenium import webdriver
from selenium.webdriver.common.keys import Keys # allows user to enter key inputs
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

PATH = "C:\Program Files (x86)\chromedriver.exe"    # the path to the chromedriver executable. Replace this with your path.
driver = webdriver.Chrome(PATH)

driver.get("https://en.wikipedia.org/wiki/Main_Page")               # open the webdriver at this address

search = driver.find_element_by_id("searchInput")

search_subject = input("Enter the topic you would like to search for.")

#search.send_keys("Selenium")
search.send_keys(search_subject)

search.send_keys(Keys.RETURN)


try:
    mw_redirect = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "mw-content-text"))
    )
    print(mw_redirect.text)
finally:
    driver.quit()





