from models.user import User

class UserService:
    def __init__(self):
        self.users = []

    
    def add_user(self, name, email):
        user = User(name, email)
        self.users.append(user)
        return user