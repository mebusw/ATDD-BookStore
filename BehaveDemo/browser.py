from selenium import webdriver
from hamcrest import *
from selenium.webdriver.common.keys import Keys

class Browser(object):

    base_url = 'http://localhost:8080'
    driver = webdriver.Chrome()
    driver.implicitly_wait(10)

    def close(self):
        """
        close the webdriver instance
        """
        self.driver.close()
        self.driver.quit()

    def visit(self, location=''):
        """
        navigate webdriver to different pages
        """
        url = self.base_url + location
        self.driver.get(url)

    def find_by_id(self, selector):
        """
        find a page element in the DOM
        """
        return self.driver.find_element_by_id(selector)

    def find_by_name(self, selector):
        """
        find a page element in the DOM
        """
        return self.driver.find_element_by_name(selector)

    def find_by_xpath(self, selector):
        """
        find a page element in the DOM
        """
        return self.driver.find_element_by_xpath(selector)

    def page_should_contain(self, text):
        """
        
        """
        assert_that(self.driver.page_source, contains_string(text))

    def input_text(self, elem, text):
        """
        
        """
        elem.clear()
        elem.send_keys(text)
        elem.send_keys(Keys.RETURN)