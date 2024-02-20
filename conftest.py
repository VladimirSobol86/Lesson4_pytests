import pytest
#from module import Site
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager
import yaml

with open("./testdata.yaml") as f:
    testdata = yaml.safe_load(f)
    browser = testdata["browser"]

#настройка нужна, чтоб убрать ненужные ошибки селениума при запуске
#options.add_experimental_option('excludeSwitches', ['enable-logging']) 

@pytest.fixture(scope="session")
def browser():
    if browser == "firefox":
        service = Service(executable_path=GeckoDriverManager().install()) 
        options = webdriver.FirefoxOptions()
        driver = webdriver.Firefox(service=service, options=options) #не может установить драйвер
    else:
        service = Service(executable_path=ChromeDriverManager().install())
        options = webdriver.ChromeOptions()
        options.add_experimental_option('excludeSwitches', ['enable-logging'])
        driver = webdriver.Chrome(service=service, options=options)
    yield driver
    driver.quit()

 
@pytest.fixture
def err_label_text():
    return "401"

# @pytest.fixture
# def site(scope = "session"):
#     site_instance = Site(testdata["address"])
#     yield site_instance
#     site_instance.close()
    
@pytest.fixture
def btn_home_text():
    return "Home"

#HW fixtures

@pytest.fixture
def title_text():
    return "New post creation"

@pytest.fixture
def contact_text():
    return "Contact us!"