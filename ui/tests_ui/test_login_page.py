import pytest


@pytest.mark.regression
def test_open_login_to_finance(open_login_page_to_finance):
    login_page = open_login_page_to_finance
    assert login_page.is_open() is True


@pytest.mark.regression
def test_authorization_page_name(open_login_page_to_finance):
    login_page = open_login_page_to_finance
    assert login_page.is_page_name_in_page() is True


@pytest.mark.regression
def test_title(open_login_page_to_finance):
    login_page = open_login_page_to_finance
    assert login_page.is_title() is True


@pytest.mark.regression
def test_password_input_clickable(open_login_page_to_finance):
    login_page = open_login_page_to_finance
    assert login_page.is_login_input_clickable() is True


@pytest.mark.regression
def test_ok_button_clickable(open_login_page_to_finance):
    login_page = open_login_page_to_finance
    assert login_page.is_ok_button_clickable() is True


@pytest.mark.regression
def test_registration_button_clickable(open_login_page_to_finance):
    login_page = open_login_page_to_finance
    assert login_page.is_registration_button_clickable() is True


@pytest.mark.regression
def test_authorization_button_clickable(open_login_page_to_finance):
    login_page = open_login_page_to_finance
    assert login_page.is_authorization_button_clickable() is True


@pytest.mark.regression
def test_home_button_clickable(open_login_page_to_finance):
    login_page = open_login_page_to_finance
    assert login_page.is_home_button_clickable() is True


@pytest.mark.regression
@pytest.mark.parametrize("login,password", [('денис', '4iPW.!29TdXfS2b'), ('Денис', '4iPW.9TdXfS2b'), ('Dima', 'Dima9TdXfS2b')])
def test_invalid_authorization(open_login_page_to_finance, login, password):
    login_page = open_login_page_to_finance
    assert login_page.authorization_with_invalid_login_or_password(login, password) is True


@pytest.mark.regression
def test_authorization(open_login_page_to_finance):
    login_page = open_login_page_to_finance
    communal_user_page = login_page.authorization('test_user_1', 'password_user_1')
    assert communal_user_page.is_login_visible('test_user_1') is True
