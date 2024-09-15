import pytest
import allure
from pages.main_page import MainPage
from pages.order_page import OrderPage

#  Весь флоу позитивного сценария с двумя наборами данных через параметризацию.
@allure.title('Позитивный сценарий заказа самоката')
@allure.description('Заполняем все обязательные поля во вкладке "Для кого самокат", нажимаем "Далее", заполняем все обязательные поля во вкладке "Про аренду", нажимаем "Заказать", подтверждаем заказ. Проверяем, что появилось сообщение "Заказ оформлен".')
@pytest.mark.parametrize("name, surname, address, metro, phone, rental_date", [
    ("Алексей", "Петров", "Москва, Кремль", "Арбатская", "89871234567", "20.09.2024"),
    ("Татьяна", "Сидорова", "Петербург, Невский пр.", "Невский проспект", "89897654321", "23.09.2024")
])
def test_order_scooter_top_button(driver, name, surname, address, metro, phone, rental_date):
    main_page = MainPage(driver)
    main_page.click_order_button_top()
    order_page = OrderPage(driver)
    order_page.fill_order_form(name, surname, address, metro, phone)
    order_page.submit_order()
    order_page.fill_rental_form(rental_date)
    order_page.confirm_order()
    order_page.confirm_yes_in_popup()
    order_page.check_success_message()
