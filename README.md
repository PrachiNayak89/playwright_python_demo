# playwright_python_demo
Assignment and learning demo of playwright with python
#### Task 2: Cross-Browser Automation for Support and Case Creation
Scenario

The application allows users to create both support tickets and cases. Recently, you’ve been receiving reports of compatibility issues on different browsers. Your task is to create an automation script that performs the following steps on multiple browsers:

- Register and log in as a user.
- Create a support ticket.
- Create a case. 

#### Expected Output

#### An executable automation script that:
- Registers a new user.
- Logs in with the newly registered user.
- Creates both a support ticket and a case.
- Executes on multiple browsers (Chrome, Firefox, etc.).

Application under test (AUT): http://100.27.30.112/ 
API Documentation of AUT: http://100.27.30.112/docs#/ 

#### Automation framework file structure
* pytest.ini
* data.py
* tests/
* report.html (will be created at root level once test runs)

#### Pre-requisite: Installations
    1. pip install pytest-playwright
    2. playwright install
    3. pip install pytest-reporter-html1

##### Run the test/tests - Can be managed directly from pytest.ini too
    pytest -k "Test_case_name" --headed (headless is default mode)
    pytest <file_name with/wo path>
    pytest -m <marker_name>


#### Links
* Playwright installation: https://playwright.dev/python/docs/intro#installing-playwright-pytest
* Pytest HTML 1 report: https://pypi.org/project/pytest-reporter-html1/
* Playwright-pytest CLI options: https://playwright.dev/python/docs/running-tests
