# Code Analyzer

This repository contains a code analyzer that can be used to review and analyze code in a given repository.

## Usage

To use the analyzer, you will need to create an instance of the `Analyzer` class and call the `analyze_repo` function.

Here is a basic example:

```python
from analyzer import Analyzer

# Specify the path to the repository
repo_path = "/path/to/your/repository"

# Create an instance of the Analyzer class
analyzer = Analyzer()

# Analyze the repository
results = analyzer.analyze_repo(repo_path)

# Print the results
print(results)
```

## Examples

For more detailed examples, please refer to the `example1.py` and `example2.py` files in the `examples` directory.

- [Example 1](./examples/example1.py)
- [Example 2](./examples/example2.py)

Please note that you will need to replace "/path/to/your/repository" with the actual path to the repository you want to analyze.