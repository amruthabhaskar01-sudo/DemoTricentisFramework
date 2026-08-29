

import pytest

from selenium import webdriver

@pytest.fixture
def setup_and_teardown():
    driver = webdriver.Chrome()   ## setup
    driver.maximize_window()
    driver.get('https://demowebshop.tricentis.com/')
    yield driver
    driver.quit()     ## teardown



## Cross browser Testing
'''
import pytest
from selenium import webdriver

@pytest.fixture(params=['chrome','firefox','edge'])
def setup_and_teardown(request):

    parameter = request.param    ## store the current parameter

    if parameter == 'chrome':
        driver = webdriver.Chrome()
    elif parameter == 'firefox':
        driver = webdriver.Firefox()
    elif parameter == 'edge':
        driver = webdriver.Edge()


    driver.get('https://demowebshop.tricentis.com/')

    yield driver
    driver.quit()

'''


## request is built in pytest object
## Whenever a fixture is parameterized , the current parameter is stored
#  inside request.param








