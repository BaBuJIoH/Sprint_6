import allure
from locators.order_page_locators import OrderPageLocators
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys

class OrderPage:
    def __init__(self, driver):
        self.driver = driver

    # Выбор станции метро
    @allure.step('Выбираем станцию метро')
    def choose_metro_station(self, metro_station):
        metro_field = self.driver.find_element(*OrderPageLocators.METRO_FIELD)
        metro_field.click()
        metro_field.send_keys(metro_station)
        WebDriverWait(self.driver, 5).until(
            EC.element_to_be_clickable(OrderPageLocators.METRO_DROPDOWN_OPTION)
        ).click()

    # Заполнение формы "Для кого самокат"
    @allure.step('Заполняем форму "Для кого самокат"')
    def fill_order_form(self, name, surname, address, metro, phone):
        self.driver.find_element(*OrderPageLocators.NAME_INPUT).send_keys(name)
        self.driver.find_element(*OrderPageLocators.SURNAME_INPUT).send_keys(surname)
        self.driver.find_element(*OrderPageLocators.ADDRESS_INPUT).send_keys(address)
        self.choose_metro_station(metro)
        self.driver.find_element(*OrderPageLocators.PHONE_INPUT).send_keys(phone)

    # Подтверждение заполненной формы "Для кого самокат"
    @allure.step('Подтверждаем заполненную форму "Для кого самокат"')
    def submit_order(self):
        self.driver.find_element(*OrderPageLocators.NEXT_BUTTON).click()

    # Заполнение формы "Про аренду"
    @allure.step('Заполненяем форму "Про аренду"')
    def fill_rental_form(self, rental_date):
        date_input = self.driver.find_element(*OrderPageLocators.DATE_INPUT)
        date_input.send_keys(rental_date)
        date_input.send_keys(Keys.ESCAPE)  # Нажимаем Escape, чтобы убрать всплывающее окно
        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD_DROPDOWN).click()
        self.driver.find_element(*OrderPageLocators.RENTAL_PERIOD).click()

    # Нажимаем "Заказать" после заполнения формы "Про аренду"
    @allure.step('Нажимаем "Заказать" после заполнения формы "Про аренду"')
    def confirm_order(self):
        self.driver.find_element(*OrderPageLocators.CONFIRM_BUTTON).click()

    # Подтверждение заказа. Кнопка "Да"
    @allure.step('Подтверждаем заказ. Кнопка "Да"')
    def confirm_yes_in_popup(self):
        self.driver.find_element(*OrderPageLocators.CONFIRM_YES_BUTTON).click()

    # Проверка, что появилось всплывающее окно с сообщением об успешном создании заказа
    @allure.step('Проверяем, что появилось всплывающее окно с сообщением об успешном создании заказа')
    def check_success_message(self):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located(OrderPageLocators.SUCCESS_ORDER_MESSAGE)
        )
        success_message = self.driver.find_element(*OrderPageLocators.SUCCESS_ORDER_MESSAGE).text
        assert OrderPageLocators.SUCCESS_MESSAGE in success_message, "Сообщение об успешном заказе не появилось"
