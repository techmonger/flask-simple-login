
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

web = webdriver.Chrome()

Email = "sagar.sws2000@gmail.com"
# Email = "18erecs080.vicky@rietjaipur.ac.in"
passw = "*********"

def fun_signup():
    web.get('https://www.w3schools.com/')
    time.sleep(4)

    login = web.find_element(By.XPATH, '//*[@id="w3loginbtn"]')
    login.click()

    signup = web.find_element(By.XPATH, '//*[@id="root"]/div/div/div[4]/div[1]/div/div[2]/form/div[1]/div[1]/span/span')
    signup.click()

    first = web.find_element(By.XPATH, '//*[@id="modalusername"]')
    first.send_keys(Email)

    last = web.find_element(By.XPATH, '//*[@id="new-password"]')
    last.send_keys(passw)

    Submit = web.find_element(By.XPATH, '//*[@id="root"]/div/div/div[4]/div[1]/div/div[4]/div[1]/button')
    Submit.click()

    fname = "Vicky"
    first = web.find_element(By.XPATH, '//*[@id="modal_first_name"]')
    first.send_keys(fname)

    lname = "Kumar"
    last = web.find_element(By.XPATH, '//*[@id="modal_last_name"]')
    last.send_keys(lname)

    Submit = web.find_element(By.XPATH, '//*[@id="root"]/div/div/div[4]/div[1]/div/div[3]/div/button')
    Submit.click()

# fun_signup()



def fun_login(passw):
    web.get('https://my-learning.w3schools.com/')

    first = web.find_element(By.XPATH, '//*[@id="modalusername"]')
    first.send_keys(Email)

    last = web.find_element(By.XPATH, '//*[@id="current-password"]')
    last.send_keys(passw)

    Submit = web.find_element(By.XPATH, '//*[@id="root"]/div/div/div[4]/div[1]/div/div[4]/div[1]/button')
    Submit.click()

    # try:
    #     input('''
    #     >>> Press Enter to Logout...
    #     ''')

    #     logout = web.find_element(By.XPATH, '//*[@id="navigation"]/div/button')
    #     logout.click()
    # except:
    #     pass


# to automate login
lst_passw = [str(i) for i in range(5)]
lst_passw.append(passw)
# print(lst_passw)

for i in lst_passw:
    time.sleep(2)
    fun_login(i)
