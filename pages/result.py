# This module contains DuckDuckGoResultPage,
# the page object for the DuckDuckGo search result page.
from selenium.webdriver.common.by import By

from common.base_page import BasePage


class DuckDuckGoResultPage(BasePage):
    RESULT_LINKS = (By.CSS_SELECTOR, 'a.result__a')

    SEARCH_INPUT = (By.ID, 'search_form_input')

    def __init__(self, browser):
        super().__init__(browser)
        # self.browser = browser

    def result_link_titles(self):
        #links = self.browser.find_elements(*self.RESULT_LINKS)
        links = self.find_elements(self.RESULT_LINKS)
        titles = [link.text for link in links]
        return titles

    def search_input_value(self):
        #search_input = self.browser.find_element(self.SEARCH_INPUT)
        search_input = self.find(self.SEARCH_INPUT)
        value = search_input.get_attribute('value')
        return value

    def title(self):
        return self.browser.title
