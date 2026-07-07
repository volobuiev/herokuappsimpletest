# Login Form Automation Testing (Selenium + Pytest)

This project contains automated UI tests for verifying the login functionality on [The Internet Herokuapp](https://the-internet.herokuapp.com/login). The tests are written in Python using the `pytest` framework and `Selenium WebDriver`.

## Project Structure

The test configuration and test scenarios are separated for better maintainability:
* `conftest.py`: Contains `pytest` fixtures (e.g., WebDriver initialization, teardown, and browser options).
* `test_login.py` (or similar): Contains the actual test functions.

## Tech Stack
* **Python 3.x**
* **Selenium WebDriver** (Browser automation)
* **Pytest** (Testing framework)

## Test Coverage
* Successful login with valid credentials.
* Login attempt with an invalid username.
* Login attempt with an invalid password.
* Login attempt with empty input fields.
* Successful logout.

## Installation & Setup

1. Clone the repository.
2. Install the required dependencies:
   ```bash
   pip install pytest selenium
   or
   pip install requirements.txt

Roadmap & Refactoring Plans (To-Do)
To ensure project scalability and code readability, the following architectural improvements are planned:

Page Object Model (POM): Extract locators (e.g., By.ID, "username") and page interaction methods into separate classes. This will decouple technical Selenium details from the test scripts, making the tests cleaner and more resilient to UI changes.

Test Parametrization: Implement the @pytest.mark.parametrize decorator. Instead of having three separate functions for negative testing (test_wrong_username, test_wrong_password, test_empty_input), a single parametrized test will iterate through multiple sets of invalid data.

Credentials Management: Move sensitive data (such as hardcoded passwords) into environment variables (e.g., using .env files) to prevent exposing credentials in the source code.