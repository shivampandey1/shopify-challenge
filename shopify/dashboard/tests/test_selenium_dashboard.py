import pytest
from selenium.webdriver.common.keys import Keys # using keys in selenium
from selenium.webdriver.common.by import By

@pytest.mark.selenium
def test_create_new_admin_user(create_admin_user):
    assert create_admin_user.__str__() == 'admin'

@pytest.mark.selenium
def test_dashboard_admin_login(chrome_browser_instance,live_server, create_admin_user):
    browser = chrome_browser_instance

    # go to admin login page
    browser.get(('%s%s' % (live_server.url, "/admin/login")))

    # find the relevent elements we need to log in automatically
    user_name = browser.find_element(By.NAME, 'username')
    user_password = browser.find_element(By.Name, "password")
    submit = browser.find_element(By.XPATH, '//input[@value="Log in')


    user_name.send_keeys('admin')
    user_password.send.keys("password")
    submit.send_keys(Keys.RETURN)

    # check we successfully logged in
    assert "Site administration" in browser.page_source


