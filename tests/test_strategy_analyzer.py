```python
import unittest
from src.strategy_analyzer import find_profitable_strategies

class TestStrategyAnalyzer(unittest.TestCase):

    def setUp(self):
        self.strategies = [
            {"name": "strategy1", "profit": 10},
            {"name": "strategy2", "profit": 20},
            {"name": "strategy3", "profit": 30},
            {"name": "strategy4", "profit": 40},
        ]
        self.selected_pair = {"pair": "BTC/ETH"}

    def test_find_profitable_strategies(self):
        profitable_strategies = find_profitable_strategies(self.strategies, self.selected_pair)
        self.assertIsInstance(profitable_strategies, list)
        self.assertGreater(len(profitable_strategies), 0)
        self.assertTrue(all(strategy["profit"] > 0 for strategy in profitable_strategies))

if __name__ == "__main__":
    unittest.main()
```