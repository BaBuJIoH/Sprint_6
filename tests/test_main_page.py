import pytest
import allure
from pages.main_page import MainPage
from links import Links

class TestMainPage(MainPage):
    def __init__(self, driver):
        super().__init__(driver)

    # Проверка, что при нажатии на лого "Яндекс" в новой вкладке открывается Дзен
    @allure.title('Проверка открытия страницы Дзен')
    @allure.description('Нажимаем на лого Яндекс и переходим в новую открывшуюся вкладку. Проверяем, что url соответствует адресу страницы Дзен')
    def test_click_yandex_logo(self):
        self.click_yandex_logo()
        self.switch_to_new_tab()
        current_url = self.get_to_current_url()
        expected_url = Links.DZEN_URL
        assert expected_url in current_url, 'Главная страница Дзен не открылась'

    # Проверка, что при нажатии на лого "Самокат" открывается главная страница Самоката
    @allure.title('Проверка перехода на главную страницу Самоката')
    @allure.description('Переходим на страницу заказа и оттуда нажимаем лого Самоката. Проверяем, что url соответствует главной странице Самоката')
    def test_click_Scooter_logo(self):
        self.click_order_button_top()
        self.click_scooter_logo()
        current_url = self.get_to_current_url()
        expected_url = Links.BASE_URL
        assert expected_url in current_url, 'Главная страница Самоката не открывается после нажатия на Лого'

    # Проверка, что при нажатии на кнопку "Заказать" вверху страницы, перейдём на страницу заказа самоката
    @allure.title('Проверка кликабельности кнопки "Заказать" вверху страницы')
    @allure.description('Нажимаем на кнопку "Заказать" вверху страницы. Проверяем, что url этой страницы соответствует url заказа самоката')
    def test_click_order_button_top(self):
        self.click_order_button_top()
        current_url = self.get_to_current_url()
        expected_url = Links.ORDER_URL
        assert expected_url in current_url, 'Страница заказа не открылась после нажатия на кнопку "Заказать" вверху страницы'

    # Проверка, что при нажатии на кнопку "Заказать" внизу страницы, перейдём на страницу заказа самоката
    @allure.title('Проверка кликабельности кнопки "Заказать" внизу страницы')
    @allure.description('Нажимаем на кнопку "Заказать" внизу страницы. Проверяем, что url этой страницы соответствует url заказа самоката')
    def test_click_order_button_bottom(self):
        self.scroll_page_down(1800)
        self.click_order_button_bottom()
        current_url = self.get_to_current_url()
        expected_url = Links.ORDER_URL
        assert expected_url in current_url, 'Страница заказа не открылась после нажатия на кнопку "Заказать" внизу страницы'
