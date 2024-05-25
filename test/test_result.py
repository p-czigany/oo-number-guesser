from unittest import TestCase
from unittest.mock import patch

from result import Result


class TestResult(TestCase):

    @patch('attempts.Attempts')
    @patch('secret_number.SecretNumber')
    def test_say_when_losing(self, mock_attempts, mock_secret_number):
        # arrange
        mock_attempts_instance = mock_attempts.return_value
        mock_attempts_instance.matches.return_value = False
        mock_secret_number_instance = mock_secret_number.return_value
        mock_secret_number_instance.number.return_value = 42

        # act
        Result(mock_attempts_instance, mock_secret_number_instance).say()

        # assert
        mock_attempts_instance.matches.assert_called_once()
        mock_secret_number_instance.number.assert_called_once()

    @patch('attempts.Attempts')
    @patch('secret_number.SecretNumber')
    def test_say_when_winning(self, mock_attempts, mock_secret_number):
        # arrange
        mock_attempts_instance = mock_attempts.return_value
        mock_attempts_instance.matches.return_value = True
        mock_secret_number_instance = mock_secret_number.return_value

        # act
        Result(mock_attempts_instance, mock_secret_number_instance).say()

        # assert
        mock_attempts_instance.matches.assert_called_once()
        mock_secret_number_instance.number.assert_not_called()
