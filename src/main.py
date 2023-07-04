```python
from strategy_gatherer import gather_strategies
from strategy_backtester import backtest_strategy
from strategy_analyzer import find_profitable_strategies
from trading_bot_creator import create_trading_bot
from config import selected_pair

def main():
    # Gather all possible strategies
    strategies = gather_strategies()

    # Backtest all strategies one by one on selected pair
    for strategy in strategies:
        backtest_strategy(strategy, selected_pair)

    # Find the most profitable strategy or strategies
    profitable_strategies = find_profitable_strategies(strategies)

    # Create a trading bot for selected pair on Binance to use selected strategy/-ies to make profit
    trading_bot = create_trading_bot(profitable_strategies, selected_pair)

if __name__ == "__main__":
    main()
```