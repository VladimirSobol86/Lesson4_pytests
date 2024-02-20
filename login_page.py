from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml

class TestSearchLocatorsLogin:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])
              
class OperationsHelperLogin(BasePage):
#Метод ввода текста:
    def enter_text_into_field(self, locator, word, description=None):
        if description:
            element_name = description
        else:
            element_name = locator
        logging.debug(f"Send {word} to element {element_name}")

        field = self.find_element(locator)
        if not field:
            logging.error(f"Element {locator} is not found")
            return False
        try:
            field.clear()
            field.send_keys(word)
        except:
            logging.exception(f"Exception while operation with {locator}")
            return False
        return True

#Метод нажатия кнопки:
    def click_button(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator

        button = self.find_element(locator)
        if not button:
            return False
        try:
            button.click()
        except:
            logging.exception("Exception with click")
            return False
        logging.debug(f"Clicked {element_name} button")
        return True

#Метод получения текста:
    def get_text_from_element(self, locator, description=None):
        if description:
            element_name = description
        else:
            element_name = locator   
        field = self.find_element(locator, time=3)
        if not field:
            return None
        try:
            text = field.text
        except:
            logging.exception(f"Exception while get text from {element_name}")
            return None
        logging.debug(f"We find text {text} in field {element_name}")
        return text
#ENTER TEXT
    def enter_login(self, word):
        self.enter_text_into_field(TestSearchLocatorsLogin.ids["x_login"], word, description="login form")
        
    def enter_pass(self, word):
        self.enter_text_into_field(TestSearchLocatorsLogin.ids["x_password"], word, description="password form")  

#BUTTONS      
    def click_login_button(self):
        self.click_button(TestSearchLocatorsLogin.ids["css_btn_login"], description="login")

#GET TEXT    
    def get_error_text(self):
        return self.get_text_from_element(TestSearchLocatorsLogin.ids["x_err_label"], description="error")