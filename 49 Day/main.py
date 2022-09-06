from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.common.exceptions import NoSuchElementException
import time

EMAIL = "thiago@gmail.com"
PASSWORD = "thiago@123"
PHONE = "(00) 99999-9999"

chrome_driver_path = "C:\Desenvolvimento\chromedriver.exe"

service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://www.linkedin.com/jobs/search/?f_LF=f_AL&geoId=102257491&keywords=marketing%20intern&location=London%2C%20England%2C%20United%20Kingdom&redirect=false&position=1&pageNum=0")

time.sleep(2)
sign_in_button = driver.find_element(By.ID, "Sign in")
sign_in_button.click()

time.sleep(5)
email_field = driver.find_element(By.ID, "username")
email_field.send_keys(EMAIL)
password_field = driver.find_element(By.ID, "password")
password_field.send_keys(PASSWORD)
password_field.send_keys(Keys.ENTER)

time.sleep(5)

all_listings = driver.find_element(By.CSS_SELECTOR, ".job-card-container--clickable")

for listing in all_listings:
    print("called")
    listing.click()
    time.sleep(2)
    try:
        apply_button = driver.find_element(By.CSS_SELECTOR, ".jobs-s-apply button")
        apply_button.click()

        time.sleep(5)
        phone = driver.find_element(By.NAME, "fb-single-line-text__input")
        if phone.text == "":
            phone.send_keys(PHONE)
        
        submit_button = driver.find_element(By.CSS_SELECTOR, "footer button")
        if submit_button.get_attribute("data-control-name") == "continue_unify":
            close_button = driver.find_element(By.NAME, "artdeco-modal__dismiss")
            close_button.click()
            
            time.sleep(2)
            discard_button = driver.find_element(By.NAME, "artdeco-modal__confirm-dialog-btn")[1]
            discard_button.click()
            print("Complex application, skipped.")
            continue
        else:
            submit_button.click()

        time.sleep(2)
        close_button = driver.find_element(By.NAME, "artdeco-modal__dismiss")
        close_button.click()

    except NoSuchElementException:
        print("No application button, skipped.")
        continue

time.sleep(5)
driver.quit()

