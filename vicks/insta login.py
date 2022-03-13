
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

web = webdriver.Chrome()
Email = "*********"
passw = "********"

web.get('https://www.instagram.com/')
time.sleep(2)

def fun_login(passw):
    try:
        first = web.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[1]/div/label/input')
        first.send_keys(Email)

        last = web.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[2]/div/label/input')
        last.send_keys(passw)

        Submit = web.find_element(By.XPATH, '//*[@id="loginForm"]/div/div[3]')
        Submit.click()

        time.sleep(2)
        save = web.find_element(By.XPATH, '//*[@id="react-root"]/section/main/div/div/div/div/button')
        save.click()

        print(passw)
    except:
        web.refresh()

# while 1:
time.sleep(2)
fun_login(passw)

# ---------------------------------

# from itertools import permutations
# stri = "!#$%&*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ_abcdefghijklmnopqrstuvwxyz|~"

# lst = list(stri)
# # for i in range(6, len(lst)):
# comb = permutations(lst, 6)
# print(list(comb))
