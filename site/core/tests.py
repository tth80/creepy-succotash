from django.test import LiveServerTestCase
from selenium.webdriver.firefox.webdriver import WebDriver


class MySeleniumTests(LiveServerTestCase):
    fixtures = ['data.json']

    @classmethod
    def setUpClass(cls):
        super(MySeleniumTests, cls).setUpClass()
        cls.selenium = WebDriver()

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(MySeleniumTests, cls).tearDownClass()

    def test_login(self):
        self.selenium.get(url='http://dev.utohk.com/accounts/login/')
        username_input = self.selenium.find_element_by_name('username')
        username_input.send_keys('myuser')

        password_input = self.selenium.find_element_by_name('password')
        password_input.send_keys('secret')

        self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()

        assert 'Please enter a correct username and password.' in self.selenium.page_source

        self.selenium.set_window_size(1920, 1080)
        self.selenium.save_screenshot('/home/timo/work/creepy-succotash/static/img/test.png')
