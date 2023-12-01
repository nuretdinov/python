from datetime import date

class User:
    def __init__(self, name, birth, email):
        self.name = name
        self.birth = birth
        self.email = email

    def get_age(self):
        now_date = date.today()
        user_age = now_date.year - self.birth.year
        return user_age


new_user = User(
    "Max",
    date(1995, 8, 25),
    "max@gmail.com",
)

print(new_user.get_age())
print(new_user.email)

class Admin(User):
    def __init__(self, name, birth, email, pwd):
        super().__init__(name, birth, email)
        self.pwd = pwd

new_admin = Admin(
    "Ann",
    date(1991, 1, 20),
    "Ann@gmail.com",
    "12345",
)
print(new_admin.get_age())
print(new_admin.email)
print(new_admin.pwd)
