import pytest
from selenium.webdriver.chrome import webdriver
from selenium import webdriver

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("headless")


# we need to add command liner (--browser)
def pytest_addoption(parser):
    parser.addoption("--browser")





@pytest.fixture
def setup(request):
    # then we have to give value to --browser
    browser = request.config.getoption("--browser")
    if browser == "chrome":
        print("Test Run - Browser Chrome")
        driver = webdriver.Chrome()
    elif browser == "firefox":
        print("Test Run - Browser Firefox")
        driver = webdriver.Firefox()
    elif browser == "edge" :
        print("Test Run - Browser Edge")
        driver = webdriver.Edge()
    else:
        print("Test Run - Headless")
        driver = webdriver.Chrome(options=chrome_options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
    yield driver
    driver.quit()

# Pytest -v  --html=HTMLReports/myreport.html -n=2  --browser edge
