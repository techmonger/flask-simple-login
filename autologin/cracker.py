
from selenium import webdriver
import time, random

web = webdriver.Chrome()
Email = "login_bot_"
passw = str(random.randint(0, 15))
print(f'''
>>>> passw : {passw}
''')
add_Email = []
counter = 0

def fun_signup(Email):
    web.get('http://127.0.0.1:5000/signup/')

    first = web.find_element_by_xpath('//*[@id="username"]')
    first.send_keys(Email)

    last = web.find_element_by_xpath('//*[@id="password"]')
    last.send_keys(passw)

    bio = web.find_element_by_xpath('//*[@id="bio"]')
    bio.send_keys(passw, ' has been cracked.')

    Submit = web.find_element_by_xpath('//*[@id="signup"]/input[3]')
    Submit.click()

    try:
        check = web.find_element_by_css_selector('.flashes').text
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
    web.get('http://127.0.0.1:5000/login/')

    first = web.find_element_by_xpath('//*[@id="username"]')
    first.send_keys(Email)

    last = web.find_element_by_xpath('//*[@id="password"]')
    last.send_keys(passw)

    Submit = web.find_element_by_xpath('//*[@id="submit"]')
    Submit.click()

    try:
        check = web.find_element_by_css_selector('.flashes')
        if check.text == 'Invalid username or password.':
            
            print(f'''
            >>>> {check.text}
            ''')

            passw = str(int(passw) + 1)
            fun_login(passw)
    except:
        pass

    try:
        check = web.find_element_by_css_selector('.welcome').text
        if check == 'Welcome':

            input('''
            >>> Press Enter to Logout...
            ''')

            logout = web.find_element_by_xpath('/html/body/p/a')
            logout.click()
    except:
        pass


# to automate signup
time.sleep(2)
Email = fun_signup(Email)[0]

# to automate login
passw = "0"
time.sleep(2)
fun_login(passw)
