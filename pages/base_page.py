import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    # Ожидание кликабельности элемента
    def wait_for_clickable(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable(locator))

    def find_element(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator))

    # Кликаем на элемент
    def click_element(self, locator):
        element = self.find_element(locator)
        element.click()

    # Получение текста ответа
    def get_answer(self, locator):
        return self.driver.find_element(*locator).text

    # Ввод текста
    def send_keys(self, locator, text):
        element = self.wait_for_clickable(locator)
        element.clear()
        element.send_keys(text)

    # Нажать Escape
    def click_escape(self):
        self.driver.find_element(By.TAG_NAME, "body").send_keys(Keys.ESCAPE)

    # Ожидание отображения текста
    def wait_for_text(self, locator, timeout=10):
        return WebDriverWait(self.driver, timeout).until(EC.presence_of_element_located(locator)).text

    # Переключить на другую вкладку
    @allure.step('переходим на другую вкладку')
    def switch_new_tab(self, url):
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(EC.url_to_be(url))

    # Получить url
    def get_current_url(self):
        return self.driver.current_url

    # Прокрутить страницу вниз на xxxx пикселей
    def scroll_down(self, pixels):
        self.driver.execute_script(f"window.scrollBy(0, {pixels});")

    def scroll_to_element(self, locator):
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)
        WebDriverWait(self.driver, 10).until(
            EC.element_to_be_clickable(locator)
        )
