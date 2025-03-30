from selenium import webdriver
import allure
from Test_page import Test_page


@allure.description("test_test")
def test_test(set_up, set_group):
    options = webdriver.ChromeOptions()
    options.add_experimental_option("detach", True)
    options.add_argument("--headless=new")
    driver = webdriver.Chrome(options=options)

    """Test'"""

    m_p = Test_page(driver)
    m_p.test_2()


    driver.close()
    driver.quit()