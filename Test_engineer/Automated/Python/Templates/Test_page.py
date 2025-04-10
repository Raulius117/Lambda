from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure
import time
from Logger import Logger
from Base import Base


class Test_page(Base):
    url = "https://www.test.com/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""

    test = "//test[@test='test']"

    """Getters"""

    def get_test(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.test)))

    """Actions"""

    def click_test(self):
        self.get_test().click()
        print("click_test")

    def input_test(self, test):
        self.get_test().send_keys(test)
        print("input_test")

    def enter_test(self):
        self.get_test().send_keys(Keys.ENTER)
        print("enter_test")

    """Methods"""

    def test_2(self):
        with allure.step("test_2"):
            Logger.add_start_step(method="test_2")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_test()
            self.input_test("Test")
            self.enter_test()
            time.sleep(3)
            self.get_current_url()
            self.assert_url("https://www.test.com/test")
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="test_2")