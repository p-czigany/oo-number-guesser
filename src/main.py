from attempts import Attempts
from difference import Difference
from difference_sentence import DifferenceSentence
from guess import Guess
from result import Result
from secret_number import SecretNumber


class Main:
    def main(self):
        secret_number = SecretNumber()
        Result(
            Attempts(
                DifferenceSentence(
                    Difference(
                        secret_number,
                        Guess()
                    )
                ), 3
            ),
            secret_number
        ).say()


Main().main()
