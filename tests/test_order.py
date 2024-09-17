import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage

class TestOrder(MainPage, OrderPage):
    def __init__(self, driver):
        super().__init__(driver)

    #  Весь флоу позитивного сценария с двумя наборами данных через параметризацию.
    @allure.title('Позитивный сценарий заказа самоката')
    @allure.description('Заполняем все обязательные поля во вкладке "Для кого самокат", нажимаем "Далее", заполняем все обязательные поля во вкладке "Про аренду", нажимаем "Заказать", подтверждаем заказ. Проверяем, что появилось сообщение "Заказ оформлен".')
    @pytest.mark.parametrize("name, surname, address, metro, phone, rental_date", [
        ("Алексей", "Петров", "Москва, Кремль", "Арбатская", "89871234567", "20.09.2024"),
        ("Татьяна", "Сидорова", "Петербург, Невский пр.", "Невский проспект", "89897654321", "23.09.2024")
    ])
    def test_order_scooter_top_button(self, name, surname, address, metro, phone, rental_date):

        self.click_order_button_top()
        self.fill_order_form(name, surname, address, metro, phone)
        self.submit_order()
        self.fill_rental_form(rental_date)
        self.confirm_order()
        self.confirm_yes_in_popup()
        self.check_success_message()

