import pytest
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

@pytest.fixture(scope="module")
def driver():
    # Setup the Chrome driver using webdriver_manager
    driver = webdriver.Chrome(ChromeDriverManager().install())
    # Set an implicit wait time for elements to appear
    driver.implicitly_wait(10)
    yield driver
    driver.quit()
