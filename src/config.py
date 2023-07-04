```python
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Binance API credentials
BINANCE_API_KEY = os.getenv('BINANCE_API_KEY')
BINANCE_SECRET_KEY = os.getenv('BINANCE_SECRET_KEY')

# Selected pair for trading
SELECTED_PAIR = os.getenv('SELECTED_PAIR')

# Path to the directory where strategies are stored
STRATEGIES_DIR = os.getenv('STRATEGIES_DIR')

# Path to the directory where backtest results are stored
BACKTEST_RESULTS_DIR = os.getenv('BACKTEST_RESULTS_DIR')

# Path to the directory where trading bots are stored
TRADING_BOTS_DIR = os.getenv('TRADING_BOTS_DIR')
```