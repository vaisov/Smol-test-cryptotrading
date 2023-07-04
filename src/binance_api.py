```python
import requests
from config import BinanceConfig

class BinanceAPI:
    def __init__(self):
        self.base_url = "https://api.binance.com"
        self.headers = {
            "X-MBX-APIKEY": BinanceConfig.API_KEY
        }

    def get_ticker_price(self, pair):
        response = requests.get(f"{self.base_url}/api/v3/ticker/price", headers=self.headers, params={"symbol": pair})
        response.raise_for_status()
        return response.json()['price']

    def place_order(self, pair, quantity, side, order_type, price=None):
        data = {
            "symbol": pair,
            "side": side,
            "type": order_type,
            "quantity": quantity,
        }
        if price:
            data["price"] = price

        response = requests.post(f"{self.base_url}/api/v3/order", headers=self.headers, data=data)
        response.raise_for_status()
        return response.json()

    def get_order_status(self, pair, order_id):
        response = requests.get(f"{self.base_url}/api/v3/order", headers=self.headers, params={"symbol": pair, "orderId": order_id})
        response.raise_for_status()
        return response.json()

    def cancel_order(self, pair, order_id):
        response = requests.delete(f"{self.base_url}/api/v3/order", headers=self.headers, params={"symbol": pair, "orderId": order_id})
        response.raise_for_status()
        return response.json()
```