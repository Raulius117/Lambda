import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver

    """Method get current URL"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"Current URL: {get_url}")

    """Method assert URL"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert result == get_url, "Error assert URL"
        print(f"Assert URL: {get_url}")

    """Method assert word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert result == value_word, "Error value word"
        print(f"Assert word: {value_word}")

    """Method screenshot"""

    def get_screenshot(self):
        now_time = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        self.driver.save_screenshot(f".\\Screenshots\\{now_time}.png")