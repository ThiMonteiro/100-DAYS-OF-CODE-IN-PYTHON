from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from selenium.common.exceptions import ElementClickInterceptedException
from time import sleep


CHROME_DRIVER_PATH = "C:\Desenvolvimento\chromedriver.exe"
SIMILAR_ACCOUNT = "instagram"
USERNAME = "thiago@monteiro"
PASSWORD = "thiago@123"

class InstaFollower:
    def __init__(self, path):
        self.service = Service(path)
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        sleep(5)

        username = self.driver.find_element(By.NAME, "username")
        password = self.driver.find_element(By.NAME, "password")

        username.send_keys(USERNAME)
        password.send_keys(PASSWORD)

        sleep(2)
        password.send_keys(Keys.ENTER)

    def find_followers(self):
        sleep(5)
        self.driver.get(f"https://www.instagram.com/{SIMILAR_ACCOUNT}")

        sleep(2)
        followers = self.driver.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/header/section/ul/li[2]/a')
        followers.click()

        sleep(2)
        modal = self.driver.find_element(By.XPATH, '/html/body/div[4]/div/div/div[2]')

        for i in range(10):
            self.driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", modal)
            sleep(2)


    def follow(self):
        all_buttons = self.driver.find_element(By.CSS_SELECTOR, "li button")
        for button in all_buttons:
            try:
                button.click()
                sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element(By.XPATH, '/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()



bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()


