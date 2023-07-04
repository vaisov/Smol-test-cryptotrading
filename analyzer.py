```python
import os

class Analyzer:
    def __init__(self, repo_path):
        self.repo_path = repo_path
        self.results = []

    def analyze_repo(self):
        for root, dirs, files in os.walk(self.repo_path):
            for file in files:
                if file.endswith(".py"):
                    with open(os.path.join(root, file), "r") as f:
                        self.results.append(f.read())
        return self.results
```