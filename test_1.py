from login_page import OperationsHelperLogin
from contact_page import OperationsHelperContact
from func import get_post, create_post, login
import time
import logging
import yaml

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)

def test_with_invalid_values(browser, err_label_text):
    logging.info("Test with invalid values starting")
    testpage_login = OperationsHelperLogin(browser)
    testpage_login.go_to_site()
    testpage_login.enter_login("invalid login")
    testpage_login.enter_pass("invalid pass")
    testpage_login.click_login_button()
    assert testpage_login.get_error_text() == err_label_text
    time.sleep(2)

def test_contact_page(browser, contact_text):
    logging.info("Test Contact page starting")   
    testpage_login = OperationsHelperLogin(browser)
    testpage_login.go_to_site()
    testpage_login.enter_login(testdata["login"])
    testpage_login.enter_pass(testdata["password"])
    time.sleep(2)
    testpage_login.click_login_button()
    time.sleep(2)
    testpage_contact = OperationsHelperContact(browser)
    testpage_contact.click_contact_button()
    time.sleep(2)
    assert testpage_contact.get_contact_text() == contact_text
    testpage_contact.enter_name(testdata["name"])
    testpage_contact.enter_email(testdata["email"])
    testpage_contact.enter_content(testdata["content"])
    time.sleep(2)
    testpage_contact.click_send_button()
    time.sleep(2)
    assert testpage_contact.alert_label() == testdata["alert"]

def test_api():
    result = create_post(login())['description']
    all_posts = get_post(login())['data']
    description_list = []
    for item in all_posts:
        description_list.append(item["description"])
    print(description_list)
    assert result in description_list   
    