import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options

@pytest.fixture(scope="session")
def chrome_browser_instance(request):
    # selenium webdriver instance
    options = Options()
    options.headless = False #tests run in background without showing, true if need to see for debug
    browser = webdriver.Chrome(chrome_options=options)
    yield browser
    browser.close()
