```python
import unittest
from src.strategy import Strategy, StrategySchema

class TestStrategy(unittest.TestCase):

    def setUp(self):
        self.strategy = Strategy()
        self.strategy_schema = StrategySchema()

    def test_strategy_creation(self):
        strategy_data = {
            'name': 'Test Strategy',
            'description': 'This is a test strategy',
            'parameters': {'param1': 1, 'param2': 2}
        }
        strategy = self.strategy.create(strategy_data)
        self.assertEqual(strategy.name, 'Test Strategy')
        self.assertEqual(strategy.description, 'This is a test strategy')
        self.assertEqual(strategy.parameters, {'param1': 1, 'param2': 2})

    def test_strategy_schema(self):
        strategy_data = {
            'name': 'Test Strategy',
            'description': 'This is a test strategy',
            'parameters': {'param1': 1, 'param2': 2}
        }
        errors = self.strategy_schema.validate(strategy_data)
        self.assertEqual(len(errors), 0)

if __name__ == '__main__':
    unittest.main()
```