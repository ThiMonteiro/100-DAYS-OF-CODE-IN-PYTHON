from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.common.service import Service
from time import sleep

FACEBOOK_EMAIL = 'thiago@gmail.com'
FACEBOOK_PASSWORD = 'thiago@123'


chrome_driver_path = "C:\Desenvolvimento\chromedriver.exe"

service = Service(chrome_driver_path)
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(executable_path=chrome_driver_path)

driver.get("https://tinder.com/")

sleep(2)
botao_login = driver.find_element(By.XPATH, '//*[@id="q554704800"]/div/div[1]/div/div/main/div/div[2]/div/div[3]/div/div/button[1]')
botao_login.click()

sleep(2)
facebook_login = driver.find_element(By.XPATH, '//*[@id="q-1173676276"]/div/div/div[1]/div/div/div[3]/span/div[2]/button')
facebook_login.click()

sleep(2)
base_window = driver.window_handles[0]
facebook_login_windows = driver.window_handles[1]
driver.switch_to.window(facebook_login_windows)

email = driver.find_element(By.XPATH, '//*[@id="email"]')
senha = driver.find_element(By.XPATH, '//*[@id="email"]')

email.send_keys(FACEBOOK_EMAIL)
senha.send_keys(FACEBOOK_PASSWORD)
senha.send_keys(Keys.ENTER)

driver.switch_to.window(base_window)
print(driver.title)

sleep(5)

permitir_localizaçao_botao = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[1]')
permitir_localizaçao_botao.click()

notificaçao_botao = driver.find_element(By.XPATH, '//*[@id="modal-manager"]/div/div/div/div/div[3]/button[2]')
notificaçao_botao.click()

cookies = driver.find_element(By.XPATH, '//*[@id="content"]/div/div[2]/div/div/div[1]/button')
cookies.click()

for n in range(100):

    sleep(1)

    try:
        print("called")
        like_button = driver.find_element(
            By.XPATH,
            '//*[@id="content"]/div/div[1]/div/main/div[1]/div/div/div[1]/div/div[2]/div[4]/button')
        like_button.click()

    except ElementClickInterceptedException:
        try:
            match_popup = driver.find_element(By.CSS_SELECTOR, ".itsAMatch a")
            match_popup.click()

        except NoSuchElementException:
            sleep(2)

driver.quit()





