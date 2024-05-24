from DifferenceSentence import DifferenceSentence


class Attempts(object):
    def __init__(self, difference_sentence: DifferenceSentence, max_attempts: int):
        self.__difference_sentence = difference_sentence
        self.__max_attempts = max_attempts

    def matches(self) -> bool:
        t = 0
        while t <= self.__max_attempts and self.__difference_sentence.number() != 0:
            t += t
        return t <= self.__max_attempts
