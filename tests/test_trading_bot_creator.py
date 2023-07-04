```python
import unittest
from unittest.mock import patch
from src.trading_bot_creator import create_trading_bot

class TestTradingBotCreator(unittest.TestCase):

    @patch('src.trading_bot_creator.BinanceAPI')
    def test_create_trading_bot(self, MockBinanceAPI):
        # Mocking the BinanceAPI
        mock_binance = MockBinanceAPI()
        mock_binance.create_bot.return_value = True

        # Test data
        selected_pair = 'BTC/ETH'
        profitable_strategies = ['strategy1', 'strategy2']

        # Call the function with test data
        result = create_trading_bot(selected_pair, profitable_strategies)

        # Assert the function was called with correct arguments
        mock_binance.create_bot.assert_called_with(selected_pair, profitable_strategies)

        # Assert the function returned True
        self.assertTrue(result)

if __name__ == '__main__':
    unittest.main()
```