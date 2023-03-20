from playwright.sync_api import Playwright, sync_playwright


class BasePage:
    def __init__(self, browser):
        self.browser = browser

    def _wait_for_element(self, selector, timeout=120):
        element = self.browser.wait_for_selector(selector, timeout=timeout)
        return element

    def _check_selector(self, selector):
        try:
            self._wait_for_element(selector)
            return True
        except:
            return False

    def _text_in_element(self, selector, text):
        element = self.browser.locator(selector)
        element_text = element.inner_text()
        if element_text == text:
            return True
        else:
            return False

    def _check_title(self, title):
        if self.browser.title() == title:
            return True
        else:
            return False

    def _wait_for_element_and_check_clickable(self, selector: str) -> bool:
        try:
            input_element = self._wait_for_element(selector)
            if input_element.is_enabled():
                return True
            else:
                return False
        except:
            return False

    def _click(self, selector: str):
        element = self._wait_for_element(selector)
        element.click()

    def _send_keys(self, selector: str, text: str):
        element = self._wait_for_element(selector)
        element.fill('')
        element.fill(text)







