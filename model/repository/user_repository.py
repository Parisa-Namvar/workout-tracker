import sqlite3
from model.entity.user import User

class UserRepository:
    def connect(self):
        self.connection = sqlite3.connect("./db/gym.db")
        self.cursor = self.connection.cursor()

    def disconnect(self):
        self.cursor.close()
        self.connection.close()

    def save (self ,user):
        self.connect()
        self.cursor.execute("insert into users (username, password, first_name, last_name, age, "
                            "register_date, phone_number, email) values (?,?,?,?,?,?,?,?)",
                            [user.username, user.password,user.first_name,user.last_name,
                             user.age,user.register_date,user.phone_number,user.email])
        self.connection.commit()
        self.disconnect()

    def update (self ,user):
        self.connect()
        self.cursor.execute("update users set (username=?, password=?, first_name=?, last_name=?, age=?, "
                            "register_date=?, phone_number=?, email=?) where id=?)",
                            [user.username, user.password,user.first_name,user.last_name,
                             user.age,user.register_date,user.phone_number,user.email,user.id])
        self.connection.commit()
        self.disconnect()

    def delete (self ,id):
        self.connect()
        self.cursor.execute("delete from users where id=?)",[id])
        self.disconnect()

    def find_all(self):
        self.connect()
        self.cursor.execute("select * from users")
        user_list = [ User (*user) for user in self.cursor.fetchall()]
        self.disconnect()
        return user_list

    def find_one(self ,id):
        self.connect()
        self.cursor.execute("select * from users where id = ?",[id])
        user_list = [ User (*user) for user in self.cursor.fetchall()]
        self.disconnect()
        return user_list