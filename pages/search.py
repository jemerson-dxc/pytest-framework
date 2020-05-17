# This module contains DuckDuckGoSearchPage,
# the page object for the DuckDuckGo search page.
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from common.base_page import BasePage


class DuckDuckGoSearchPage(BasePage):
    pass

    # URL
    URL = 'https://www.duckduckgo.com'

    # Locators
    SEARCH_INPUT = (By.ID, 'search_form_input_homepage')

    def __init__(self, browser):
        super().__init__(browser)
        # self.browser = browser

    def load(self):
        self.navigate_to(self.URL)
        # self.browser.get(self.URL)

    def search(self, phrase):
        # search_input = self.browser.find_element(*self.SEARCH_INPUT)
        # search_input.send_keys(phrase + Keys.RETURN)
        self.enter_text_and_select_return(self.SEARCH_INPUT, phrase)
