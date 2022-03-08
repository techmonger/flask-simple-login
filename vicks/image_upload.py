
from firebase_admin import db
from firebase_admin import credentials
import base64


cred = credentials.Certificate('fireson.json')
url = 'https://ideationology-4c639-default-rtdb.asia-southeast1.firebasedatabase.app/'
path = {'databaseURL' : url}


import firebase_admin
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, path)

def friends():
    return db.reference(f'Upload/Account').get()

class Bank_Account:
    def __init__(self, username):
        self.username = db.reference(f'Upload/Account/{username}/Balance')
        self.balance = self.username.get()

        if self.balance is None:
            self.username.set(1000)


    def deposit(self, amount):
        self.balance = self.username.get()
        self.balance += amount

        self.username.set(self.balance)
        return self.display()


    def withdraw(self, amount):
        self.balance = self.username.get()

        if self.balance>=amount:
            self.balance-=amount

            self.username.set(self.balance)
        return self.display()


    def display(self):
        return self.username.get()


class Upload():
    def __init__(self, username, img):
        self.username = db.reference(f'Upload/Account/{username}/Image')
        self.img = img
        self.path = self.username.get()
        # print(self.path)

        if self.path is None:
            self.username.set('Welcome')


    def img2txt(self):
        with open(f"{self.img}", "rb") as image2string:
            converted_string = base64.b64encode(image2string.read())

        self.username.set(converted_string.decode('utf-8')) # save image


    def txt2img(self):
        byte = self.username.get() # fetch image

        decodeit = open(f'{self.img}', 'wb')
        decodeit.write(base64.b64decode(byte))
        decodeit.close()


# ------------------------------------------------


# user = ['Vicky Kumar', 'firebase', ]

# obj = Bank_Account(user[1])
# obj.deposit(1000)
# obj.withdraw(100)
# s = obj.display()
# print(s)


# up_obj = Upload(user[0], 'vicky.jpg')
# up_obj.img2txt()
# up_obj.txt2img()
