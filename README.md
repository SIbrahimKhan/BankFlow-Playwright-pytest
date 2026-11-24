# BankFlow – Banking Application Automation

A UI test automation framework built using **Python, Playwright, and Pytest** to validate key functionalities of a banking web application.

## Tech Stack

- Python
- Playwright
- Pytest
- Page Object Model (POM)
- python-dotenv
- Allure Reports

## Project Features

- Data-driven testing using Pytest parameterization
- Page Object Model for maintainable test code
- Environment-based configuration using `.env`
- Reusable page methods and fixtures
- Positive and negative login test scenarios
- Test execution and reporting with Pytest and Allure

## Test Scenarios

| Test Scenario | Expected Result |
|---|---|
| Valid login | User navigates to Accounts Overview |
| Invalid username and password | Appropriate error message appears |
| Valid username, invalid password | Login is rejected |
| Empty username and password | Validation message appears |

## Project Structure

```text
BankFlow-Playwright-pytest/
├── pages/
│   ├── __init__.py
│   └── login_page.py
├── tests/
│   └── test_login.py
├── test_data/
│   └── login_data.py
├── utils/
│   ├── __init__.py
│   └── config.py
├── conftest.py
├── pytest.ini
├── requirements.txt
├── .gitignore
└── README.md
```

## Installation

Clone the repository:

```bash
git clone https://github.com/SIbrahimKhan/BankFlow-Playwright-pytest.git
cd BankFlow-Playwright-pytest
```

Create and activate a virtual environment:

```bash
python3 -m venv venv
source venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
playwright install chromium
```

Create a `.env` file in the project root:

```env
BASE_URL=https://parabank.parasoft.com/parabank/index.htm
```

## Run Tests

```bash
python -m pytest
```

Run tests with detailed output:

```bash
python -m pytest -v -s
```

## Allure Reporting

Generate Allure results:

```bash
python -m pytest --alluredir=allure-results
```

View the report:

```bash
allure serve allure-results
```

## Application Under Test

[ParaBank Demo Banking Application](https://parabank.parasoft.com/parabank/index.htm)

## Author

Ibrahim Khan

[GitHub Profile](https://github.com/SIbrahimKhan)