import unittest
from unittest.mock import patch
import json
from utils import get_data

class TestGetData(unittest.TestCase):

    @patch('builtins.open')
    def test_empty_file(self, mock_open):
        mock_open.return_value.__enter__.return_value.read.return_value = ''
        file_path = 'data/operations.json'
        transactions = get_data(file_path)
        self.assertEqual(transactions, [])

    @patch('builtins.open')
    def test_valid_json(self, mock_open):
        mock_open.return_value.__enter__.return_value.read.return_value = json.dumps([
            {'id': 1, 'amount': 100, 'date': '2023-10-26'},
            {'id': 2, 'amount': 50, 'date': '2023-10-27'}
        ])
        file_path = 'data/operations.json'
        transactions = get_data(file_path)
        self.assertEqual(transactions, [
            {'id': 1, 'amount': 100, 'date': '2023-10-26'},
            {'id': 2, 'amount': 50, 'date': '2023-10-27'}
        ])

    @patch('builtins.open')
    def test_invalid_json(self, mock_open):
        mock_open.return_value.__enter__.return_value.read.return_value = 'invalid json'
        file_path = 'data/operations.json'
        with self.assertRaises(json.JSONDecodeError):
            get_data(file_path)

if __name__ == '__main__':
    unittest.main()
