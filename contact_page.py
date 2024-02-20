from BaseApp import BasePage
from selenium.webdriver.common.by import By
import logging
import yaml

class TestSearchLocatorsContact:
    ids = dict()
    with open("./locators.yaml") as f:
        locators = yaml.safe_load(f)
    for locator in locators["xpath"].keys():
        ids[locator] = (By.XPATH, locators["xpath"][locator])
    for locator in locators["css"].keys():
        ids[locator] = (By.CSS_SELECTOR, locators["css"][locator])
    
class OperationsHelperContact(BasePage):
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
#BUTTONS
    def click_contact_button(self):
        self.click_button(TestSearchLocatorsContact.ids["x_btn_contact"], description="contact")
    
    def click_send_button(self):
        self.click_button(TestSearchLocatorsContact.ids["x_btn_send"], description="send")

#GET TEXT
    def get_contact_text(self):
        return self.get_text_from_element(TestSearchLocatorsContact.ids["x_label_contact_us"], description="contact label")


#ENTER TEXT    
    def enter_name(self, name):
        self.enter_text_into_field(TestSearchLocatorsContact.ids["x_name"], name, description="name field")
        
    def enter_email(self, email):
        self.enter_text_into_field(TestSearchLocatorsContact.ids["x_email"], email, description="email field")
        
    def enter_content(self, content):
        self.enter_text_into_field(TestSearchLocatorsContact.ids["x_content"], content, description="content field")
        
#ALERT       
    def alert_label(self):
        alert = self.driver.switch_to.alert
        text = alert.text
        logging.info(f"Message in alert after clicking Send button: {text}")
        return text