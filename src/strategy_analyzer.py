```python
from src.strategy_backtester import backtest_strategy
from src.strategy import StrategySchema

def find_profitable_strategies(strategies, selected_pair):
    profitable_strategies = []
    max_profit = 0

    for strategy in strategies:
        profit = backtest_strategy(strategy, selected_pair)
        if profit > max_profit:
            max_profit = profit
            profitable_strategies = [strategy]
        elif profit == max_profit:
            profitable_strategies.append(strategy)

    return profitable_strategies

def analyze_strategies():
    from src.strategy_gatherer import gather_strategies
    from src.pair import selected_pair

    strategies = gather_strategies()
    profitable_strategies = find_profitable_strategies(strategies, selected_pair)

    return profitable_strategies
```