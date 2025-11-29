from model.repository.user_repository import UserRepository


class UserService:
    def __init__(self):
        self.repository = UserRepository()

    def save (self ,user):
        self.repository.save(user)

    def update (self ,user):
        self.repository.update(user)

    def delete (self ,id):
        self.repository.delete(id)

    def find_all(self):
        self.repository.find_all()

    def find_one(self ,id):
        self.repository.find_one(id)