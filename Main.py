from Attempts import Attempts
from Difference import Difference
from DifferenceSentence import DifferenceSentence
from Guess import Guess
from Result import Result
from SecretNumber import SecretNumber


class Main:
    def main(self):
        Result(
            Attempts(
                DifferenceSentence(
                    Difference(
                        SecretNumber(),
                        Guess()
                    )
                ), 7
            ),
            SecretNumber()
        ).say()


Main().main()
