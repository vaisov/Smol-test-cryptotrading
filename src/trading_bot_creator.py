```python
from binance_api import BinanceAPI
from strategy import StrategySchema
from pair import PairSchema
from config import config

class TradingBotCreator:
    def __init__(self, api: BinanceAPI, strategies: list[StrategySchema], pair: PairSchema):
        self.api = api
        self.strategies = strategies
        self.pair = pair

    def create_trading_bot(self):
        trading_bot = {}
        for strategy in self.strategies:
            trading_bot[strategy.name] = self.api.create_bot(strategy, self.pair)
        return trading_bot

if __name__ == "__main__":
    api = BinanceAPI(config['api_key'], config['api_secret'])
    strategies = gather_strategies()
    pair = selected_pair
    bot_creator = TradingBotCreator(api, strategies, pair)
    trading_bot = bot_creator.create_trading_bot()
```