from unittest import TestCase
from unittest.mock import patch

from difference_sentence import DifferenceSentence


class TestDifferenceSentence(TestCase):
    @patch('difference.Difference')
    def test_number(self, mock_difference):
        # arrange
        mock_difference_instance = mock_difference.return_value
        mock_difference_instance.number.return_value = -13

        # act
        result = DifferenceSentence(mock_difference_instance).number()

        # assert
        self.assertEqual(-13, result)
        mock_difference_instance.number.assert_called_once()
