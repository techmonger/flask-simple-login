
# https://stackoverflow.com/a/69875984/11493297
from selenium.webdriver.common.by import By

from selenium import webdriver
import time, random

Email = "bot_"
passw = str(random.randint(0, 50))

print(f'''
>>>> passw : {passw}
''')

add_Email = []
chance = counter = 0

web = webdriver.Chrome()

def fun_signup(Email):
    # web.get('http://127.0.0.1:5000/signup/')
    web.get('https://vixtest.herokuapp.com/signup/')

    first = web.find_element(By.XPATH, '//*[@id="username"]')
    first.send_keys(Email)

    last = web.find_element(By.XPATH, '//*[@id="password"]')
    last.send_keys(passw)

    bio = web.find_element(By.XPATH, '//*[@id="bio"]')
    bio.send_keys(passw, ' has been cracked.')

    Submit = web.find_element(By.XPATH, '//*[@id="signup"]/input[3]')
    Submit.click()

    try:
        check = web.find_element(By.CSS_SELECTOR, '.flashes').text
        if check.split()[0] == 'Username':

            print(f'''
            >>>> {check}
            ''')

            global counter
            counter += 1
            Email += str(counter)

            fun_signup(Email)
            add_Email.append(Email)
            return add_Email

        else:
            add_Email.append(Email)
            return add_Email
    except:
        pass


def fun_login(passw):
    # web.get('http://127.0.0.1:5000/login/')
    web.get('https://vixtest.herokuapp.com/login/')

    first = web.find_element(By.XPATH, '//*[@id="username"]')
    first.send_keys(Email)

    last = web.find_element(By.XPATH, '//*[@id="password"]')
    last.send_keys(passw)

    Submit = web.find_element(By.XPATH, '//*[@id="submit"]')
    Submit.click()

    try:
        check = web.find_element(By.CSS_SELECTOR, '.flashes')
        if check.text == 'Invalid username or password.':
            
            print(f'''
            >>>> {check.text}
            ''')

            guessed_passw = str(int(passw) + 1)

            # GAME...
            # guessed_passw = input('Enter guessed Password : ')
            # if int(guessed_passw) > int(passw):

            #     print('Password is Greater than Guessed...')
            #     chance += 1

            # elif int(guessed_passw) < int(passw):
            #     print('Password is Lesser than Guessed...')
            #     chance += 1

            # if int(guessed_passw) == int(passw):
            #     print('Guessed Password is Correct...')
            #     print('>>>>>>> ', chance)

            fun_login(guessed_passw)
    except:
        pass

    try:
        check = web.find_element(By.CSS_SELECTOR, '.welcome').text
        if check == 'Welcome':

            input('''
            >>> Press Enter to Logout...
            ''')

            logout = web.find_element(By.XPATH, '/html/body/p/a')
            logout.click()
    except:
        pass


# to automate signup
time.sleep(2)
Email = fun_signup(Email)[0]

# to automate login
passw = "0"
# Email = "bot_"
time.sleep(2)
fun_login(passw)
