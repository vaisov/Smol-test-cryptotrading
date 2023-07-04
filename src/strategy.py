```python
class Strategy:
    def __init__(self, name, parameters):
        self.name = name
        self.parameters = parameters

    def get_name(self):
        return self.name

    def get_parameters(self):
        return self.parameters

class StrategySchema:
    def __init__(self):
        self.schema = {
            "name": {"type": "string", "required": True},
            "parameters": {"type": "dict", "required": True}
        }

    def validate(self, data):
        for key, value in self.schema.items():
            if key not in data:
                return False
            if type(data[key]) != value["type"]:
                return False
        return True
```