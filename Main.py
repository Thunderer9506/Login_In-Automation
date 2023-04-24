from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

chrome_options = Options()
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')

driver = webdriver.Chrome(options=chrome_options)

driver.get("https://practicetestautomation.com/practice-test-login/")

username_scrape = driver.find_element(By.ID,"username")
username_scrape.send_keys("student")

password_scrape =driver.find_element(By.ID,"password")
password_scrape.send_keys("Password123")

submit_scrape = driver.find_element(By.ID,"submit")

submit_scrape.click()
driver.quit()
