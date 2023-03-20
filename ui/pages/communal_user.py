from ui.pages.base_page import BasePage


class CommunalUser(BasePage):
    def __init__(self, browser):
        self.browser = browser
        super().__init__(self.browser)

    __user_selector = 'div.mx-auto p.text-center'

    def is_login_visible(self, login):
        user = self._wait_for_element(self.__user_selector)
        return user.inner_text() == login



