from selenium import webdriver
import pytest
import allure
from Main_page import Main_page
from Search_page import Search_page

# @pytest.mark.run(order=1)
# @allure.description("test test")
# set_up, set_group
def test_test():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    """Ввод в поле 'search' слово 'Gothic' и нажатие кнопки 'ENTER'"""

    m_p = Main_page(driver)
    m_p.search_in_header()

    """Включение чекбоксов 'Games' и 'Windows', а затем нажатие на ссылку 'Gothic II: Gold Edition'"""

    s_p = Search_page(driver)
    s_p.search_on_search_page()

    driver.close()
    driver.quit()