from guess import Guess
from secret_number import SecretNumber


class Difference(object):
    def __init__(self, secret_number: SecretNumber, guess: Guess):
        self.__secret_number = secret_number
        self.__guess = guess

    def number(self) -> int:
        return self.__guess.number() - self.__secret_number.number()
