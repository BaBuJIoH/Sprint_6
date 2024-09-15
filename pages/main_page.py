import allure
from locators.main_page_locators import MainPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class MainPage:
    def __init__(self, driver):
        self.driver = driver

    # Нажать на кнопку Заказать вверху страницы
    @allure.step('Нажимаем на кнопку Заказать вверху страницы')
    def click_order_button_top(self):
        self.driver.find_element(*MainPageLocators.ORDER_BUTTON_TOP).click()

    # Нажать на кнопку Заказать внизу страницы
    @allure.step('Нажимаем на кнопку Заказать внизу страницы')
    def click_order_button_bottom(self):
        self.driver.find_element(*MainPageLocators.ORDER_BUTTON_BOTTOM).click()

    # Нажать на лого Самокат
    @allure.step('Нажимаем на лого Самокат')
    def click_scooter_logo(self):
        self.driver.find_element(*MainPageLocators.SCOOTER_LOGO).click()

    # Нажать на лого Яндекс
    @allure.step('Нажимаем на лого Яндекс')
    def click_yandex_logo(self):
        self.driver.find_element(*MainPageLocators.YANDEX_LOGO).click()

    # Переключение на новую вкладку и ожидание загрузки страницы
    @allure.step('Переключаем на новую вкладку и ожидание загрузки страницы')
    def switch_to_new_tab_and_wait(self, url):
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 10).until(EC.url_to_be(url))

    # Нажать на вопрос по индексу
    @allure.step('Нажимаем на вопрос по индексу')
    def click_question(self, index):
        self.driver.find_element(*MainPageLocators.QUESTIONS[index]).click()

    # Получить ответ по индексу
    @allure.step('Получаем ответ по индексу')
    def get_answer_text(self, index):
        return self.driver.find_element(*MainPageLocators.ANSWERS[index]).text
