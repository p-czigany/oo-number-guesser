from unittest import TestCase
from unittest.mock import patch

from secret_number import SecretNumber


class TestSecretNumber(TestCase):
    @patch('random.randint', return_value=42)
    def test_secret_number_when_randomized(self, mock_randint):
        # arrange
        secret_number = SecretNumber()

        # act
        result = secret_number.number()

        # assert
        self.assertEqual(result, 42)
        mock_randint.assert_called_once_with(0, 99)

    def test_secret_number_when_given(self):
        # arrange
        secret_number = SecretNumber(42)

        # act
        result = secret_number.number()

        # assert
        self.assertEqual(result, 42)
