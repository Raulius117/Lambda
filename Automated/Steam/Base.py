import datetime


class Base():
    def __init__(self, driver):
        self.driver = driver

    """Method: get_current_url"""

    def get_current_url(self):
        get_url = self.driver.current_url
        print(f"get_current_url: {get_url}")

    """Method: assert_url"""

    def assert_url(self, result):
        get_url = self.driver.current_url
        assert result == get_url, "Error: assert_url"
        print(f"assert_url: {get_url}")

    """Method: assert_word"""

    def assert_word(self, word, result):
        value_word = word.text
        assert result == value_word, "Error: assert_word"
        print(f"assert_word: {value_word}")

    """Method: get_screenshot"""

    def get_screenshot(self):
        now_time = datetime.datetime.now().strftime("%Y.%m.%d-%H.%M.%S")
        self.driver.save_screenshot(f".\\Screenshots\\{now_time}.png")