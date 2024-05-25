import random


class SecretNumber(object):
    def __init__(self, number: int = None):
        if number is not None:
            self.__number = number
        else:
            self.__number = random.randint(0, 99)

    def number(self) -> int:
        return self.__number
