from difference_sentence import DifferenceSentence


class Attempts(object):
    def __init__(self, difference_sentence: DifferenceSentence, max_attempts: int):
        self.__difference_sentence = difference_sentence
        self.__max_attempts = max_attempts

    def matches(self) -> bool:
        t = 1
        while t <= self.__max_attempts and self.__difference_sentence.number() != 0:
            t += 1
        return t <= self.__max_attempts
