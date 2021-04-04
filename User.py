class User:
    def __init__(self, name, surname, email, password):
        self.name = name
        self.surname = surname
        self.email = email
        self.password = password

    def user_json(self):
        json = {
            "name": self.name,
            "surname": self.surname,
            "email": self.email,
            "password": self.password
        }
        return json
