from selenium import webdriver
import pytest
import allure
from Main_page import Main_page

# @pytest.mark.run(order=1)
# @allure.description("test test")
# set_up, set_group
def test_test():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    m_p = Main_page(driver)
    m_p.search_in_header()

    driver.close()
    driver.quit()