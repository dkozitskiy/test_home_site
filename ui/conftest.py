import pytest
from playwright.sync_api import Playwright, sync_playwright

from ui.pages.login_to_finance import LoginPageToFinance


# фикстура для инициализации браузера
@pytest.fixture()
def browser():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)
        yield browser
        browser.close()


@pytest.fixture()
def open_login_page_to_finance(browser):
    page = browser.new_page()
    page.goto('http://matroskin.pythonanywhere.com/finance/communal_user/')
    return LoginPageToFinance(page)
