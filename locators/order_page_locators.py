from selenium.webdriver.common.by import By

class OrderPageLocators:
    # Локаторы для страницы заказа
    NAME_INPUT = (By.XPATH, '//input[@placeholder="* Имя"]')  # Поле ввода имени
    SURNAME_INPUT = (By.XPATH, '//input[@placeholder="* Фамилия"]')  # Поле ввода фамилии
    ADDRESS_INPUT = (By.XPATH, '//input[@placeholder="* Адрес: куда привезти заказ"]')  # Поле ввода адреса
    METRO_FIELD = (By.XPATH, "//input[@placeholder='* Станция метро']")  # Поле выбора станции метро
    METRO_DROPDOWN_OPTION = (By.XPATH, "//ul[contains(@class, 'select-search__options')]//li[1]")   # Локатор для первой станции в выпадающем списке после ввода текста
    PHONE_INPUT = (By.XPATH, '//input[@placeholder="* Телефон: на него позвонит курьер"]')  # Поле ввода номера телефона
    NEXT_BUTTON = (By.XPATH, '//button[text()="Далее"]')  # Кнопка "Далее"
    DATE_INPUT = (By.XPATH, '//input[@placeholder="* Когда привезти самокат"]')  # Поле выбора даты
    RENTAL_PERIOD_DROPDOWN = (By.CLASS_NAME, 'Dropdown-control')  # Строка "Срок аренды"
    RENTAL_PERIOD = (By.XPATH, f"//div[text()='сутки']")  # Выбор срока аренды на сутки
    CONFIRM_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Заказать']")  # Кнопка "Заказать" в форме заказа
    CONFIRM_YES_BUTTON = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g') and contains(@class, 'Button_Middle__1CSJM') and text()='Да']") # Кнопка "Да" подтверждение заказа
    SUCCESS_MODAL = (By.CLASS_NAME, 'Order_ModalHeader__3FDaJ')  # Окно подтверждения
    SUCCESS_ORDER_MESSAGE = (By.CSS_SELECTOR, 'div.Order_ModalHeader__3FDaJ')  # Сообщение о потверждении заказа в окне подтверждения
    SUCCESS_MESSAGE = 'Заказ оформлен'  # Ожидаемое сообщение о подтверждении заказа
