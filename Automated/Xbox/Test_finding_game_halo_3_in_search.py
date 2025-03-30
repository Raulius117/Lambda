from selenium import webdriver
import allure
from Main_page import Main_page
from Search_page import Search_page


@allure.description("test_finding_game_halo_3_in_search")
def test_finding_game_halo_3_in_search(set_up, set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    """Нажатие на кнопку "Search" и ввод в поле 'Search...' слова 'Halo', а потом нажатие кнопки 'ENTER'"""

    m_p = Main_page(driver)
    m_p.search_in_header()

    """Нахождение игры "Halo 3" в поиске и нажатие на ссылку 'Halo 3'"""

    s_p = Search_page(driver)
    s_p.search_on_search_page()


    driver.close()
    driver.quit()