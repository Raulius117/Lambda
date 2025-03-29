from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure
import time
from Base import Base
# from Logger import Logger


class Main_page(Base):
    url = "https://store.steampowered.com/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""

    field_search = "//input[@id='store_nav_search_term']"

    """Getters"""

    def get_field_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.field_search)))

    """Actions"""

    def input_field_search(self, field_search):
        self.get_field_search().send_keys(field_search)
        print("input_field_search")

    def enter_field_search(self):
        self.get_field_search().send_keys(Keys.ENTER)
        print("enter_field_search")

    """Methods"""

    def search_in_header(self):
        # with allure.step("search_in_header"):
            # Logger.add_start_step(method="search_in_header")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.input_field_search("Gothic")
            self.enter_field_search()
            time.sleep(1)
            self.get_current_url()
            self.assert_url("https://store.steampowered.com/search/?term=Gothic")
            self.get_screenshot()
            # Logger.add_end_step(url=self.driver.current_url, method="search_in_header")