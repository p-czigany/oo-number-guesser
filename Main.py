from Difference import Difference
from Guess import Guess
from SecretNumber import SecretNumber


class Main:
    def main(self):
        print(f'The difference is: {Difference(SecretNumber(), Guess()).number()}')


Main().main()
