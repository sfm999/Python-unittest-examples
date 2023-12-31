# Ways to run this
**NOTE** that all commands will be run in verbose mode because I like knowing what tests ran, not just what failed. The verbose mode is triggered by adding the `-v` flag into your run command.

## Our project structure

```
project/  
|-- code/  
|   |-- __init__.py  
|   |-- calculations.py  
|-- tests/  
|   |-- __init__.py  
|   |-- test_calculations.py  
|   |-- test_str.py  
```

We will use `test_calculations.py` throughout our tests for consistency. Feel free to try some of them out on `test_str.py`, just don't forget to change the relevant values :grinning:

## Run all tests with discovery
```bash
python3 -m unittest discover -v
```

## Run tests by file
```bash
python3 -m unittest tests/test_calculations.py -v
```

## Run a specific test file by pattern
```bash
python3 -m unittest discover -p test_calculations.py -v
```

## Run a specific TestCase
```bash
python3 -m unittest tests.test_calculations.TestCalculations -v
```

## Run a specific test from a specific TestCase
```bash
python3 -m unittest tests.test_calculations.TestCalculations.test_sum -v
```