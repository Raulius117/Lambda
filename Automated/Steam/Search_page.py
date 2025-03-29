from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure
import time
from Logger import Logger
from Base import Base


class Search_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""

    checkbox_windows = "//div[@data-loc='Windows']"
    link_gothic_2_gold_edition = "//span[contains(text(), 'Gothic II: Gold Edition')]"

    """Getters"""

    def get_checkbox_windows(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.checkbox_windows)))

    def get_link_gothic_2_gold_edition(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_gothic_2_gold_edition)))
    
    """Actions"""

    def click_checkbox_windows(self):
        self.get_checkbox_windows().click()
        print("click_checkbox_windows")

    def click_link_gothic_2_gold_edition(self):
        self.get_link_gothic_2_gold_edition().click()
        print("click_link_gothic_2_gold_edition")

    """Methods"""

    def search_on_search_page(self):
        with allure.step("search_on_search_page"):
            Logger.add_start_step(method="search_on_search_page")
            self.get_current_url()
            self.click_checkbox_windows()
            self.click_link_gothic_2_gold_edition()
            time.sleep(1)
            self.get_current_url()
            self.assert_url("https://store.steampowered.com/app/39510/Gothic_II_Gold_Edition/")
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="search_on_search_page")