from unittest import TestCase
from unittest.mock import patch, MagicMock

from attempts import Attempts
from difference_sentence import DifferenceSentence


class TestAttempts(TestCase):
    @patch('difference_sentence.DifferenceSentence')
    def test_matches_false(self, mock_difference_sentence):
        # arrange
        mock_difference_sentence_instance = mock_difference_sentence.return_value
        mock_difference_sentence_instance.number.return_value = -13

        # act
        result = Attempts(mock_difference_sentence_instance, 3).matches()

        # assert
        self.assertFalse(result)
        mock_difference_sentence_instance.number.assert_called()

    def test_matches_true(self):
        # arrange
        mock_difference_sentence_instance = MagicMock(spec=DifferenceSentence)
        mock_difference_sentence_instance.number.side_effect = [1, 2, 0]
        attempts = Attempts(mock_difference_sentence_instance, 5)

        # act
        result = attempts.matches()

        # assert
        self.assertTrue(result)
        self.assertEqual(mock_difference_sentence_instance.number.call_count, 3)
