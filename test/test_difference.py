from unittest import TestCase
from unittest.mock import patch

from difference import Difference
from secret_number import SecretNumber


class TestDifference(TestCase):
    @patch('guess.Guess')
    def test_number(self, mock_guess):
        # arrange
        mock_guess_instance = mock_guess.return_value
        mock_guess_instance.number.return_value = 42

        # act
        result = Difference(SecretNumber(55), mock_guess_instance).number()

        # assert
        self.assertEqual(-13, result)
        mock_guess_instance.number.assert_called_once()
