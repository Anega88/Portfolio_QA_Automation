## Python_Project
Final Python project for UI and API test automation.

### Libraries Used
- **pytest** — A library for writing and executing tests. 
   It provides tools for organizing and running tests, verifying 
   expected results, and generating reports.

- **selenium** — A library for automated interaction with web 
   browsers. It is used for testing web interfaces and allows 
   emulating user actions such as clicks and text input.

- **webdriver-manager** — A library for automatically downloading
   and updating browser drivers (e.g., ChromeDriver for Chrome), 
   simplifying the setup and execution of tests with Selenium.

- **allure-pytest** — A pytest plugin that generates detailed test
   reports in Allure format, including test results, error screenshots,
   and other metadata.

- **requests** — A library for making HTTP requests. It is used for 
   testing APIs, allowing you to send requests to a server and receive 
   responses.

### Steps
1. Clone the project: 'git clone https://github.com/Anega88/Portfolio_QA_Automation.git' 
   To do this, open a new terminal via the menu: Terminal -> New terminal.
2. Navigate to the project directory: 'cd Portfolio_QA_Automation'
3. Install dependencies from the 'requirements.txt' file: 'pip install -r requirements.txt'
4. Run tests in the terminal:
   - All tests: 'pytest'
   - 'pytest -s ui' to run only UI tests.
   - 'pytest -s api' to run only API tests.
5. Allure reports are automatically collected after running the tests.
6. Open the Allure report: 'allure open allure-report'

### Notes

1. Make sure Allure is installed. If it is not, you can install it by following the 
   [official Allure installation guide.](https://allurereport.org/)
2. To work with **Selenium**, you will need a browser driver:
   - For Firefox, use **GeckoDriver**: https://github.com/mozilla/geckodriver/releases
   - For Chrome, use **ChromeDriver**: https://sites.google.com/chromium.org/driver/

### Project Structure

   The project includes:

- **Functional and API tests** for the target website.
- **Configuration files** for setting up the test environment and parameters.
- **Scripts for interacting with web pages**, including authentication and access verification.

### File Descriptions

1. **config.py** — A file containing parameters for configuring tests,
   such as the site URL or authentication data. This helps to easily 
   change settings without modifying the test code.

2. **conftest.py** — A file for setting up fixtures and shared objects 
   used in tests, such as WebDriver settings or data for all tests. 
   This helps avoid code duplication.

3. **pytest.ini** — A file where you can configure how pytest will run
   the tests, for example, specifying which tests to run, setting up logging,
   and configuring parameters for Allure reports.

4. **gitignore** — A file used to specify files and directories that 
   should not be included in the Git repository. This is useful for excluding 
   temporary files.