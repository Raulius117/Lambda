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

    link_halo_3 = "//span[contains(text(), 'Halo 3')]"
    name_halo_3 = "//h1[@data-testid='ProductDetailsHeaderProductTitle']"

    """Getters"""

    def get_link_halo_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.link_halo_3)))

    def get_name_halo_3(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_halo_3)))
    
    """Actions"""

    def click_link_halo_3(self):
        self.get_link_halo_3().click()
        print("click_link_halo_3")

    """Methods"""

    def search_on_search_page(self):
        with allure.step("search_on_search_page"):
            Logger.add_start_step(method="search_on_search_page")
            self.get_current_url()
            self.click_link_halo_3()
            time.sleep(3)
            self.get_current_url()
            self.assert_url("https://www.xbox.com/ru-RU/games/store/halo-3/BSXZVK24CMR3/0001")
            self.assert_word(self.get_name_halo_3(), "Halo 3")
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="search_on_search_page")