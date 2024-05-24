import random


class SecretNumber(object):
    def __init__(self):
        self.__number = random.randint(0, 99)

    def number(self) -> int:
        return self.__number
