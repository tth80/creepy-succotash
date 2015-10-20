from django.test import LiveServerTestCase
from contextlib import contextmanager
from selenium.webdriver.firefox.webdriver import WebDriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import staleness_of


class MySeleniumTests(LiveServerTestCase):
    fixtures = ['sites.json']

    @classmethod
    def setUpClass(cls):
        super(MySeleniumTests, cls).setUpClass()
        cls.selenium = WebDriver()
        cls.selenium.set_window_size(1920, 1080)

    @classmethod
    def tearDownClass(cls):
        cls.selenium.quit()
        super(MySeleniumTests, cls).tearDownClass()

    @contextmanager
    def wait_for_page_load(self, timeout=30):
        old_page = self.selenium.find_element_by_tag_name('html')
        print(old_page)
        yield
        WebDriverWait(self.selenium, timeout).until(
            staleness_of(old_page)
        )

    def test_login(self):
        username = 'user.user'
        password = 'pass.pass'

        self.selenium.get(url='{}{}'.format(self.live_server_url, '/accounts/login/'))
        self.selenium.save_screenshot('/home/timo/work/creepy-succotash/static/img/test3.png')
        with self.wait_for_page_load(timeout=10):
            username_input = self.selenium.find_element_by_name('username')
            username_input.send_keys(username)

            password_input = self.selenium.find_element_by_name('password')
            password_input.send_keys(password)

            self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()

            self.selenium.save_screenshot('/home/timo/work/creepy-succotash/static/img/test.png')
            assert 'Please enter a correct username and password.' in self.selenium.page_source

        from django.contrib.auth.models import User
        user = User.objects.create_user(username, password=password)
        user.is_superuser = True
        user.is_staff = False
        user.save()

        assert user.id == 1

        self.selenium.get(url='{}{}'.format(self.live_server_url, '/accounts/login/'))
        with self.wait_for_page_load(timeout=10):
            username_input = self.selenium.find_element_by_name('username')
            username_input.send_keys(username)

            password_input = self.selenium.find_element_by_name('password')
            password_input.send_keys(password)

            self.selenium.find_element_by_xpath('//input[@value="Log in"]').click()

        with self.wait_for_page_load(timeout=10):
            self.selenium.save_screenshot('/home/timo/work/creepy-succotash/static/img/test2.png')
            assert 'Please enter a correct username and password.' not in self.selenium.page_source
