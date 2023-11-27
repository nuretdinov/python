from datetime import datetime, date, time

class User:
    def __init__(self, name, birth, email):
        self.name = name
        self.birth = birth
        self.email = email

    def getAge(self):
        nowDate = date.today()
        userAge = nowDate.year - self.birth.year
        return userAge

newUser = User(
    "Max",
    date(1995, 8, 25),
    "max@gmail.com",
)

print(newUser.getAge())
print(newUser.email)

class Admin(User):
    def __init__(self, name, birth, email, pwd):
        super().__init__(name, birth, email)
        self.pwd = pwd

newAdmin = Admin(
    "Ann",
    date(1991, 1, 20),
    "Ann@gmail.com",
    "12345",
)
print(newAdmin.getAge())
print(newAdmin.email)
print(newAdmin.pwd)