"""
These tests cover SwagLabs log in.
"""
import pytest

from pages.home import SwagLabsHomePage
from pages.result import swagLabsResultPage
from pages.logIn import SwagLabsLogInPage


#----------------------log in---------------------------------------------------------------#
@pytest.mark.parametrize('userName', ['standard_user', 'problem_user','performance_glitch_user'])
@pytest.mark.parametrize('password', ['secret_sauce'])
def test_log_out(browser, userName, password):

  logIn_page = SwagLabsLogInPage(browser)
  result_page = swagLabsResultPage(browser)
  home_page = SwagLabsHomePage(browser)
  logIn_page.load()
  logIn_page.logIn(userName, password)

  # Given the log in page of swag
  home_page.load()
  # When the user type correct credentials
  home_page.log_out()


  # Then the home page gets load

  assert 'Swag Labs' == browser.title
  #assert 'Products'  == home_page.title_value()
  #assert 'Products'  == home_page.title_value()