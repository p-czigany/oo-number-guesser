from Difference import Difference
from DifferenceSentence import DifferenceSentence
from Guess import Guess
from SecretNumber import SecretNumber


class Main:
    def main(self):
        DifferenceSentence(
            Difference(
                SecretNumber(),
                Guess()
            )
        ).number()


Main().main()
