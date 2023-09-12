from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
chrome_driver_path="E:\chromedriver-win64\chromedriver-win64\chromedriver.exe"
service = Service(executable_path=chrome_driver_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=options)

# Navigating to the login page
driver.get("https://practicetestautomation.com/practice-test-login/")

# waiting for page to open
time.sleep(3)

# Finding the username and password fields in the page
username=driver.find_element(By.XPATH,'//*[@id="username"]')
password=driver.find_element(By.XPATH,'//*[@id="password"]')

# Entering the username and password fields
username.send_keys("student")
password.send_keys("Password123")

# Click the submit button
submit_button = driver.find_element(By.XPATH,'//*[@id="submit"]')
submit_button.click()

# Wait for the login to complete
time.sleep(3)

# Verifying that the user is logged in
try:
    driver.find_element(By.XPATH,'//*[@id="error"]')
    print('Login Failed')
except:
    print("Login successful!")

