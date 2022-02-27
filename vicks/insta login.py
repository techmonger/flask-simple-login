
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

web = webdriver.Chrome()

Email = "vix.bot"
passw = "*********"


def fun_login(passw):
    web.get('https://www.instagram.com/')
    time.sleep(2)

    first = web.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
    first.send_keys(Email)

    last = web.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
    last.send_keys(passw)

    Submit = web.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
    Submit.click()

    time.sleep(2)
    save = web.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')
    save.click()


# to automate login
time.sleep(2)
fun_login(passw)
