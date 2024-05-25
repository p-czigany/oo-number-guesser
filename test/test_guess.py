from unittest import TestCase
from unittest.mock import patch

from guess import Guess


class TestGuess(TestCase):
    @patch('builtins.input', return_value='42')
    def test_number(self, mock_result):
        # act
        result = Guess().number()

        # assert
        self.assertEqual(result, 42)
