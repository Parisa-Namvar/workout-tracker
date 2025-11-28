class User:
    def __init__(self, id, username, password, first_name, last_name, age, register_date, phone_number, email=None):
        self.id = id
        self.username = username
        self.password = password
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.register_date = register_date
        self.phone_number = phone_number
        self.email = email

def __repr__(self):
    return (f"{self.__dict__}")
