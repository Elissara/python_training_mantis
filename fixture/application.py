from selenium import webdriver
from fixture.session import SessionHelper
from fixture.project import ProjectHelper
from fixture.james import JamesHelper
from fixture.signup import SignupHelper
from fixture.mail import MailHelper
from fixture.soap import SoapHelper


class Application:
    def __init__(self, browser, config):
        if browser == 'firefox':
            self.wd = webdriver.Firefox()
        elif browser == 'edge':
            self.wd = webdriver.Edge()
        elif browser == 'chrome':
            self.wd = webdriver.Chrome()
        else:
            raise ValueError("Unrecognized browser %s % browser")
        self.wd.implicitly_wait(2)
        self.project = ProjectHelper(self)
        self.session = SessionHelper(self)
        self.signup = SignupHelper(self)
        self.mail = MailHelper(self)
        self.soap = SoapHelper(self)
        self.james = JamesHelper(self)
        self.config = config
        self.base_url = config['web']['baseUrl']
        self.password = config['webadmin']['password']

    def is_valid(self):
        try:
            self.wd.current_url
            return True
        except:
            return False

    def open_home_page(self):
        wd = self.wd
        wd.get(self.base_url)

    def return_to_home_page(self):
        wd = self.wd
        wd.find_element_by_link_text("home").click()

    def destroy(self):
        self.wd.quit()

