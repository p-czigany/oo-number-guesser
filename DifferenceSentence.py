from Difference import Difference


class DifferenceSentence(object):
    def __init__(self, difference: Difference):
        self.__difference = difference

    def number(self) -> int:
        x = self.__difference.number()
        if x < 0:
            print('Too small.')
        elif x > 0:
            print('Too large.')
        else:
            print('That\'s it!')
        return x
