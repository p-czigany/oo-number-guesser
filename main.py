from attempts import Attempts
from difference import Difference
from difference_sentence import DifferenceSentence
from guess import Guess
from result import Result
from secret_number import SecretNumber


class Main:
    def main(self):
        Result(
            Attempts(
                DifferenceSentence(
                    Difference(
                        SecretNumber(),
                        Guess()
                    )
                ), 3
            ),
            SecretNumber()
        ).say()


Main().main()
