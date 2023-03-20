from ui.pages.base_page import BasePage
import time

from ui.pages.communal_user import CommunalUser


class LoginPageToFinance(BasePage):
    def __init__(self, browser):
        self.browser = browser
        super().__init__(self.browser)

    __navbar_selector = '[id="navbarCollapse"]'
    __page_name_selector = 'h1.h3.mb-3.fw-normal.text-center'
    __login_input_selector = '#id_username'
    __password_input_selector = '#id_password'
    __ok_button = '#id_ok'
    __registration_button = '#id_registration'
    __authorization_button = '#id_authorization'
    __home_button = '#id_home'
    __page_name = 'Авторизация'
    __title = 'Авторизация'
    __error_msg = 'Пожалуйста, введите правильные имя пользователя и пароль. Оба поля могут быть чувствительны к регистру.'

    def is_open(self):
        return self._check_selector(self.__navbar_selector)

    def is_page_name_in_page(self):
        return self._text_in_element(self.__page_name_selector, self.__page_name)

    def is_title(self):
        return self._check_title(self.__title)

    def is_login_input_clickable(self):
        return self._wait_for_element_and_check_clickable(self.__login_input_selector)

    def is_password_input_clickable(self):
        return self._wait_for_element_and_check_clickable(self.__password_input_selector)

    def is_ok_button_clickable(self):
        return self._wait_for_element_and_check_clickable(self.__ok_button)

    def is_registration_button_clickable(self):
        return self._wait_for_element_and_check_clickable(self.__registration_button)

    def is_authorization_button_clickable(self):
        return self._wait_for_element_and_check_clickable(self.__authorization_button)

    def is_home_button_clickable(self):
        return self._wait_for_element_and_check_clickable(self.__authorization_button)

    def authorization_with_invalid_login_or_password(self, login, password):
        self._send_keys(self.__login_input_selector, login)
        self._send_keys(self.__password_input_selector, password)
        self._click(self.__ok_button)
        page_content = self.browser.text_content("html")
        if self.__error_msg in page_content:
            return True
        else:
            return False

    def authorization(self, login, password):
        self._send_keys(self.__login_input_selector, login)
        self._send_keys(self.__password_input_selector, password)
        self._click(self.__ok_button)
        return CommunalUser(self.browser)










