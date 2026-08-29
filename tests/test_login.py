from Demo_Tricentis_Framework.pages.login_page import LoginPage
import pytest

@pytest.mark.smoke
def test_valid_login(setup_and_teardown):
    lp = LoginPage(setup_and_teardown)
    lp.click_login()
    lp.enter_email("tweetyy123@gmail.com")
    lp.enter_password("TTweety@9090")
    lp.click_login_button()

@pytest.mark.regression
def test_invalid_login(setup_and_teardown):
    lp = LoginPage(setup_and_teardown)
    lp.click_login()
    lp.enter_email("twee123@gmail.com")
    lp.enter_password("@9090")
    lp.click_login_button()