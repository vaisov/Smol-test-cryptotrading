```python
import unittest
from unittest.mock import patch
from src.binance_api import BinanceAPI

class TestBinanceAPI(unittest.TestCase):

    @patch('src.binance_api.requests.get')
    def test_get_market_data(self, mock_get):
        mock_response = mock_get.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {'symbol': 'BTCUSDT', 'price': '50000.00'}

        binance_api = BinanceAPI()
        response = binance_api.get_market_data('BTCUSDT')

        self.assertEqual(response, {'symbol': 'BTCUSDT', 'price': '50000.00'})
        mock_get.assert_called_once_with('https://api.binance.com/api/v3/ticker/price', params={'symbol': 'BTCUSDT'})

    @patch('src.binance_api.requests.post')
    def test_place_order(self, mock_post):
        mock_response = mock_post.return_value
        mock_response.status_code = 200
        mock_response.json.return_value = {'orderId': '12345'}

        binance_api = BinanceAPI()
        response = binance_api.place_order('BTCUSDT', 'BUY', 0.01)

        self.assertEqual(response, {'orderId': '12345'})
        mock_post.assert_called_once()

if __name__ == '__main__':
    unittest.main()
```