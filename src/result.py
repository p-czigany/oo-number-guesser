from attempts import Attempts
from secret_number import SecretNumber


class Result(object):
    def __init__(self, attempts: Attempts, secret_number: SecretNumber):
        self.__attempts = attempts
        self.__secret_number = secret_number

    def say(self):
        if not self.__attempts.matches():
            print(f'You lost, sorry. It was: {self.__secret_number.number()}')
        print('Thanks for playing with me!')
