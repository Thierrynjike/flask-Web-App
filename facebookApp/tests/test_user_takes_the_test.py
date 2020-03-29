from flask_testing import LiveServerTestCase
from selenium import webdriver
import selenium.webdriver.support.ui as ui
from selenium.webdriver.common.action_chains import ActionChains
from flask import url_for



from .. import app
from .. import models

class TestUserTakesTheTest(LiveServerTestCase):
    def create_app(self):
        #config file just for the tests
        app.config.from_object('facebookApp.tests.config')
        return app

    #Method executed before each test
    def setUp(self):
        """Setup the driver and create test users"""
        #the browser is supposed to be firefox
        self.driver=webdriver.Firefox()
        #ad data in the db
        models.init_db()
        self.wait = ui.WebDriverWait(self.driver,1000)
        self.result_page = url_for('result',
                                   first_name=app.config['FB_USER_NAME'],
                                   id=app.config['FB_USER_ID'],
                                   gender=app.config['FB_USER_GENDER'],
                                   _external=True)

    # method executed after each test
    def tearDown(self):
        self.driver.quit()

    def test_user_login(self):
        # we open the browser with the server adress
        self.driver.get(self.get_server_url())
        # the adress in the url must be what we expect
        assert self.driver.current_url == 'http://localhost:8943/'

    def get_el(self,selector):
        return self.driver.find_element_by_css_selector(selector)

    def clicks_on_login(self):
        button=self.get_el(".fb-login-button")
        self.wait.until(lambda driver: self.driver.find_element_by_tag_name("iframe").is_displayed())
        ActionChains(self.driver).click(button).perform()

    def sees_login_page(self):
        # do nothing until another window opens
        self.wait.until(lambda driver: len(self.driver.window_handles) > 1)
        # windows_handles returns all the opened windows list in the openin order
        # thus, while the the authentication page is the last opened
        # it will be the last element of the list
        self.driver.switch_to_window(self.driver.window_handles[-1])
        # we wait the end of page loading
        self.wait.until(lambda driver: self.get_el('#email'))
        self.driver.current_url.startswitch('https://www.facebook.com/login.php')

    def enter_text_field(self,selector,text):
        # we find the field to fill
        text_field=self.get_el(selector)
        # we delete values that already exist
        text_field.clear()
        text_field.send_keys(text)

    def submits_form(self):
        # the email field has id=email
        self.enter_text_field('#email',app.config['FB_USER_EMAIL'])
        # password field has id=pass
        self.enter_text_field('#pass', app.config['FB_USER_PW'])
        # the we click on the submit button
        self.get_el('#loginbutton input[name=login]').click()



    def test_user_login(self):
        # we open the browser with the server address
        self.driver.get(self.get_server_url())
        self.clicks_on_login()
        self.sees_login_page()
        self.submits_form()
        self.driver.switch_to_window(self.driver.window_handles[0])
        # Now we wait the last windows to be closed
        # and there is only one window opened
        self.wait.until(lambda driver: len(self.driver.window_handles) == 1)
        # the address in the url must be the expected one
        # We expect a '?' in the url
        self.wait.until(lambda driver:'?' in self.driver.current_url)
        # url matches with the expected path
        assert self.driver.current_url == self.result_page
