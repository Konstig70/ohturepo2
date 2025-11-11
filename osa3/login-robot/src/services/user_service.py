from entities.user import User
import re 

class UserInputError(Exception):
    pass


class AuthenticationError(Exception):
    pass


class UserService:
    def __init__(self, user_repository):
        self._user_repository = user_repository

    def check_credentials(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        user = self._user_repository.find_by_username(username)

        if not user or user.password != password:
            raise AuthenticationError("Invalid username or password")

        return user

    def create_user(self, username, password):
        self.validate(username, password)

        user = self._user_repository.create(
            User(username, password)
        )

        return user

    def validate(self, username, password):
        if not username or not password:
            raise UserInputError("Username and password are required")

        if not re.match("^[a-z]+$", username) or len(username) < 3:
            raise UserInputError("Username needs to be atleast 3 characters long and use characters a-z")
        
        #Salasanan regexiin lisätty myös isot kirjaimet
        if len(password) < 5 or re.match("^[A-Za-z]+$", password):
            raise UserInputError("Password needs to be atleast 5 chars and not be only letters")
        # toteuta loput tarkastukset tänne ja nosta virhe virhetilanteissa
