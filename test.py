import unittest
from unittest import TestCase
from unittest.mock import patch, call

import bitcoin

class TestBitCoins(TestCase):

    
    @patch('bitcoin.exchange_rate')# Testing if the coverting rate is correct
    def test_convert(self, mock_rate ):
        mock_rate_float = 1234.56
        example_api_response={'bpi': 'USD', 'rate_float': mock_rate_float}
        mock_rate.side_effect = [example_api_response]
        conversion = bitcoin.get_convert_rate(100, mock_rate_float)
        self.assertEqual(123456, conversion)

    #
    @patch('builtins.input', side_effect=['2',  'abc', '5star', 'gitinit','', '6', '10'])
    def test_get_coins_input(self, mock_input):# Testing user only to enter numbers 
        coins = bitcoin.get_coins()
        self.assertEqual(2, coins)
    
     
    @patch('builtins.input', side_effect=['5', '-1', '-89', '', '99', 'abn'])
    def test_get_coins_negative(self, mock_input):#testing only numbers greater or equal to 0
        coins = bitcoin.get_coins()
        self.assertEqual(5, coins)

   



if __name__ == "__main__":
    unittest.main()
