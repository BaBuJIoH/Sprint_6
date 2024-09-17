import allure
from pages.base_page import BasePage
from locators.order_page_locators import OrderPageLocators

class OrderPage(BasePage):
    def __init__(self, driver):
        super().__init__(driver)

    # Выбор станции метро
    @allure.step('Выбираем станцию метро')
    def choose_metro_station(self, metro_station):
        self.send_keys(OrderPageLocators.METRO_FIELD, metro_station)
        self.click_element(OrderPageLocators.METRO_DROPDOWN_OPTION)

    # Заполнение формы "Для кого самокат"
    @allure.step('Заполняем форму "Для кого самокат"')
    def fill_order_form(self, name, surname, address, metro, phone):
        self.send_keys(OrderPageLocators.NAME_INPUT, name)
        self.send_keys(OrderPageLocators.SURNAME_INPUT, surname)
        self.send_keys(OrderPageLocators.ADDRESS_INPUT, address)
        self.choose_metro_station(metro)
        self.send_keys(OrderPageLocators.PHONE_INPUT, phone)

    # Подтверждение заполненной формы "Для кого самокат"
    @allure.step('Подтверждаем заполненную форму "Для кого самокат"')
    def submit_order(self):
        self.click_element(OrderPageLocators.NEXT_BUTTON)

    # Заполнение формы "Про аренду"
    @allure.step('Заполненяем форму "Про аренду"')
    def fill_rental_form(self, rental_date):
        self.send_keys(OrderPageLocators.DATE_INPUT, rental_date)
        self.click_escape(OrderPageLocators.DATE_INPUT)
        self.click_element(OrderPageLocators.RENTAL_PERIOD_DROPDOWN)
        self.click_element(OrderPageLocators.RENTAL_PERIOD)

    # Нажимаем "Заказать" после заполнения формы "Про аренду"
    @allure.step('Нажимаем "Заказать" после заполнения формы "Про аренду"')
    def confirm_order(self):
        self.click_element(OrderPageLocators.CONFIRM_BUTTON)

    # Подтверждение заказа. Кнопка "Да"
    @allure.step('Подтверждаем заказ. Кнопка "Да"')
    def confirm_yes_in_popup(self):
        self.click_element(OrderPageLocators.CONFIRM_YES_BUTTON)

    # Проверка, что появилось всплывающее окно с сообщением об успешном создании заказа
    @allure.step('Проверяем, что появилось всплывающее окно с сообщением об успешном создании заказа')
    def check_success_message(self):
        success_message = self.wait_for_text(OrderPageLocators.SUCCESS_ORDER_MESSAGE)
        assert OrderPageLocators.SUCCESS_MESSAGE in success_message, "Сообщение об успешном заказе не появилось"
