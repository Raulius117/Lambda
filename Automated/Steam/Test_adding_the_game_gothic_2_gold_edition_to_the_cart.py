from selenium import webdriver
import allure
from Main_page import Main_page
from Search_page import Search_page
from Card_page import Card_page


@allure.description("test_adding_the_game_gothic_2_gold_edition_to_the_cart")
def test_adding_the_game_gothic_2_gold_edition_to_the_cart(set_up, set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    """Ввод в поле 'search' слова 'Gothic' и нажатие кнопки 'ENTER'"""

    m_p = Main_page(driver)
    m_p.search_in_header()

    """Включение чекбокса 'Windows', а затем нажатие на ссылку 'Gothic II: Gold Edition'"""

    s_p = Search_page(driver)
    s_p.search_on_search_page()

    """Добавление игры 'Gothic II: Gold Edition' в корзину и переход в корзину"""

    c_p = Card_page(driver)
    c_p.add_card_to_cart()

    driver.close()
    driver.quit()