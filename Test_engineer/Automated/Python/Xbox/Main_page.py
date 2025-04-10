from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import allure
import time
from Logger import Logger
from Base import Base


class Main_page(Base):
    url = "https://www.xbox.com/"

    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""

    button_search = "//button[@id='search']"
    field_search = "//input[@id='cli_shellHeaderSearchInput']"

    """Getters"""

    def get_button_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_search)))

    def get_field_search(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.field_search)))

    """Actions"""

    def click_button_search(self):
        self.get_button_search().click()
        print("click_button_search")

    def input_field_search(self, field_search):
        self.get_field_search().send_keys(field_search)
        print("input_field_search")

    def enter_field_search(self):
        self.get_field_search().send_keys(Keys.ENTER)
        print("enter_field_search")

    """Methods"""

    def search_in_header(self):
        with allure.step("search_in_header"):
            Logger.add_start_step(method="search_in_header")
            self.driver.get(self.url)
            self.driver.maximize_window()
            self.get_current_url()
            self.click_button_search()
            self.input_field_search("Halo")
            self.enter_field_search()
            time.sleep(3)
            self.get_current_url()
            self.assert_url("https://www.xbox.com/ru-ru/Search/Results?q=Halo")
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="search_in_header")