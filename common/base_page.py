from selenium.webdriver.common.keys import Keys


class BasePage:

    def __init__(self, browser):
        self.browser = browser

    def navigate_to(self, url):
        self.browser.get(url)

    def find(self, identifier):
        element = self.browser.find_element(*identifier)
        return element

    def find_elements(self, identifier):
        elements = self.browser.find_elements(*identifier)
        return elements

    def enter_text_and_select_return(self, identifier, text):
        input_field = self.find(identifier)
        input_field.send_keys(text + Keys.RETURN)