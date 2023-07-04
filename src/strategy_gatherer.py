```python
import requests
from src.strategy import StrategySchema

def gather_strategies():
    strategies = []
    # Assuming we have a URL that provides us with the strategies
    strategies_url = "http://example.com/strategies"

    response = requests.get(strategies_url)
    data = response.json()

    for item in data:
        strategy = StrategySchema().load(item)
        strategies.append(strategy)

    return strategies
```