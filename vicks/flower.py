
from firebase_admin import db
from firebase_admin import credentials
cred = credentials.Certificate('vicks/fireson.json')

url = 'https://ideationology-4c639-default-rtdb.asia-southeast1.firebasedatabase.app/'
path = {'databaseURL' : url}

import firebase_admin
if not firebase_admin._apps:
    firebase_admin.initialize_app(cred, path)


class Bank_Account:
    def __init__(self, username):
        self.username = db.reference(f'Bank_Account/User/{username}')
        self.balance = self.username.get()

        if self.balance is None:
            self.username.set(0)

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


# obj = Bank_Account('firebase', 50)
# d = obj.deposit(1000)
# w = obj.withdraw(100)
# s = obj.display()
# print(s)
