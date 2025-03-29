from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import allure
import time
from Logger import Logger
from Base import Base


class Card_page(Base):
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver

    """Locators"""

    button_add_to_cart = "//a[@id='btn_add_to_cart_2763']"
    button_open_basket = "//button[@class='DialogButton _DialogLayout Primary Focusable']"
    name_gothic_2_gold_edition = "//div[@class='EflKs0JjldhDSxbUBaiOp']"

    """Getters"""

    def get_button_add_to_cart(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_add_to_cart)))

    def get_button_open_basket(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.button_open_basket)))

    def get_name_gothic_2_gold_edition(self):
        return WebDriverWait(self.driver, 30).until(EC.element_to_be_clickable((By.XPATH, self.name_gothic_2_gold_edition)))
    
    """Actions"""

    def click_button_add_to_cart(self):
        self.get_button_add_to_cart().click()
        print("click_button_add_to_cart")

    def click_button_open_basket(self):
        self.get_button_open_basket().click()
        print("click_button_open_basket")

    """Methods"""

    def add_card_to_cart(self):
        with allure.step("add_card_to_cart"):
            Logger.add_start_step(method="add_card_to_cart")
            self.get_current_url()
            self.click_button_add_to_cart()
            self.click_button_open_basket()
            time.sleep(1)
            self.get_current_url()
            self.assert_url("https://store.steampowered.com/cart")
            self.assert_word(self.get_name_gothic_2_gold_edition(), "Gothic II: Gold Edition")
            self.get_screenshot()
            Logger.add_end_step(url=self.driver.current_url, method="add_card_to_cart")