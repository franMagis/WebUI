"""
These tests cover SwagLabs log in.
"""
import pytest

from pages.home import SwagLabsHomePage
from pages.logIn import SwagLabsLogInPage


#----------------------log in---------------------------------------------------------------#
@pytest.mark.parametrize('userName', ['standard_user', 'problem_user','performance_glitch_user'])
@pytest.mark.parametrize('password', ['secret_sauce'])
def test_logIn(browser, userName, password):

  logIn_page = SwagLabsLogInPage(browser)
  home_page = SwagLabsHomePage(browser)

  # Given the log in page of swag
  logIn_page.load()

  # When the user type correct credentials
  logIn_page.logIn(userName,password)


  # Then the home page gets load
  home_page.load()
  assert 'Swag Labs' == browser.title

