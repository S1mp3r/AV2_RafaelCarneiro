import unittest
from unittest.mock import patch
from io import StringIO
import random

from q1_RafaelCarneiro import cash_Transaction, fund_Transfer, credit, create_transaction

class TestTransactionFunctions(unittest.TestCase):

    def setUp(self):
        self.user_name = "test_user"
        self.user_Fund = round(random.uniform(1, 5000), 2)

    def test_cash_Transaction(self):
        with patch('builtins.input', side_effect=['100']):
            with patch('sys.stdout', new_callable=StringIO) as fake_out:
                result = lambda: cash_Transaction(self.user_Fund)
                result()
                self.assertEqual(result, "Transaction Completed")
                self.assertIn("Printing Payment Receipt", fake_out.getvalue())

    def test_fund_Transfer(self):
        with patch('builtins.input', side_effect=['Confirm']):
            result = lambda: fund_Transfer(self.user_Fund, self.user_name)
            result()
            self.assertEqual(result, "Transaction Completed")

        with patch('builtins.input', side_effect=['Cancel']):
            result = lambda: fund_Transfer(self.user_Fund, self.user_name)
            result()
            self.assertEqual(result, "Close Transaction")

    def test_credit(self):
        with patch('builtins.input', side_effect=['Confirm']):
            result = lambda: credit(self.user_Fund, self.user_name)
            result()
            self.assertEqual(result, "Transaction Completed")

        with patch('builtins.input', side_effect=['Cancel']):
            result = lambda: credit(self.user_Fund, self.user_name)
            result()
            self.assertEqual(result, "Close Transaction")

    def test_create_transaction(self):
        with patch('builtins.input', side_effect=['100']):
            result = lambda: create_transaction("Cash")
            result()
            self.assertEqual(result, "Transaction Completed")

        with patch('builtins.input', side_effect=['Confirm']):
            result = lambda: create_transaction("Fund Transfer")
            result()
            self.assertEqual(result, "Transaction Completed")

        with patch('builtins.input', side_effect=['Cancel']):
            result = lambda:  create_transaction("Fund Transfer")
            result()
            self.assertEqual(result, "Close Transaction")

        with patch('builtins.input', side_effect=['Confirm']):
            result = lambda: create_transaction("Credit")
            result()
            self.assertEqual(result, "Transaction Completed")

        with patch('builtins.input', side_effect=['Cancel']):
            result = lambda: create_transaction("Credit")
            result()
            self.assertEqual(result, "Close Transaction")

        result = lambda: create_transaction("Invalid")
        result()
        self.assertEqual(result, "Incorrect Value")

if __name__ == '__main__':
    unittest.main()

