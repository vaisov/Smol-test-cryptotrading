```python
import unittest
from src import config

class TestConfig(unittest.TestCase):

    def setUp(self):
        self.config = config.Config()

    def test_api_key(self):
        self.assertIsNotNone(self.config.API_KEY, "API Key is not set")

    def test_api_secret(self):
        self.assertIsNotNone(self.config.API_SECRET, "API Secret is not set")

    def test_selected_pair(self):
        self.assertIsNotNone(self.config.SELECTED_PAIR, "Selected pair is not set")

if __name__ == '__main__':
    unittest.main()
```