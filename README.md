# Pytest_Playwright

For parallel execution, in pytest.ini, set "addopts = -n 4"

#### Test Execution

```
# Headless browser
python -m pytest

# Headed browser
python -m pytest --headed

# Tagged test
python -m pytest -m fuzzyMatching
python -m pytest -m standardMatching
python -m pytest -m contact
python -m pytest -m duncansafeproduct

# Headed with tag
python -m pytest -m duncansafeproduct --headed
```

#### Allure Report

```
allure serve reports/allure-results
```
