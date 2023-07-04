```python
import unittest
from src.pair import Pair

class TestPair(unittest.TestCase):

    def setUp(self):
        self.pair = Pair('BTC', 'ETH')

    def test_pair_creation(self):
        self.assertEqual(self.pair.base, 'BTC')
        self.assertEqual(self.pair.quote, 'ETH')

    def test_pair_string_representation(self):
        self.assertEqual(str(self.pair), 'BTC/ETH')

if __name__ == '__main__':
    unittest.main()
```