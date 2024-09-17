import allure
from pages.base_page import BasePage
from locators.main_page_locators import MainPageLocators

class MainPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Нажать на кнопку Заказать вверху страницы
    @allure.step('Нажимаем на кнопку Заказать вверху страницы')
    def click_order_button_top(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_TOP)

    # Нажать на кнопку Заказать внизу страницы
    @allure.step('Нажимаем на кнопку Заказать внизу страницы')
    def click_order_button_bottom(self):
        self.click_element(MainPageLocators.ORDER_BUTTON_BOTTOM)

    # Нажать на лого Самокат
    @allure.step('Нажимаем на лого Самокат')
    def click_scooter_logo(self):
        self.click_element(MainPageLocators.SCOOTER_LOGO)

    # Нажать на лого Яндекс
    @allure.step('Нажимаем на лого Яндекс')
    def click_yandex_logo(self):
        self.click_element(MainPageLocators.YANDEX_LOGO)

    # Нажать на вопрос по индексу
    @allure.step('Нажимаем на вопрос по индексу')
    def click_question(self, index):
        self.click_element(MainPageLocators.QUESTIONS[index])

    # Получить ответ по индексу
    @allure.step('Получаем ответ по индексу')
    def get_answer_text(self, index):
        self.wait_for_clickable(MainPageLocators.QUESTIONS[index])
        self.get_answer(MainPageLocators.ANSWERS[index])

    # Переключить на другую вкладку
    @allure.step('переходим на другую вкладку')
    def switch_to_new_tab(self):
        self.switch_new_tab()

    # Получаем url
    def get_to_current_url(self):
        self.get_current_url()

    # Прокрутка страницы
    def scroll_page_down(self, pixels):
        self.scroll_down(pixels)
