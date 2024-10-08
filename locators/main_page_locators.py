from selenium.webdriver.common.by import By

class MainPageLocators:
    # Локаторы для главной страницы
    ORDER_BUTTON_TOP = (By.XPATH, '//button[contains(text(), "Заказать")][1]')  # Кнопка Заказать вверху страницы
    ORDER_BUTTON_BOTTOM = (By.XPATH, '//button[contains(@class,"Button_Middle")]')  # Кнопка Заказать внизу страницы
    SCOOTER_LOGO = (By.XPATH, '//img[@alt="Scooter"]')  # Лого Самокат
    YANDEX_LOGO = (By.XPATH, '//img[@alt="Yandex"]')  # Лого Яндекс
    COOKIE_CONFIRM_BUTTON = (By.XPATH, "//button[text()='да все привыкли']")
    # Кнопки вопросов
    QUESTIONS = [(By.ID, 'accordion__heading-0'),
                     (By.ID, 'accordion__heading-1'),
                     (By.ID, 'accordion__heading-2'),
                     (By.ID, 'accordion__heading-3'),
                     (By.ID, 'accordion__heading-4'),
                     (By.ID, 'accordion__heading-5'),
                     (By.ID, 'accordion__heading-6'),
                     (By.ID, 'accordion__heading-7')]
    # Кнопки ответов
    ANSWERS = [(By.ID, 'accordion__panel-0'),
                   (By.ID, 'accordion__panel-1'),
                   (By.ID, 'accordion__panel-2'),
                   (By.ID, 'accordion__panel-3'),
                   (By.ID, 'accordion__panel-4'),
                   (By.ID, 'accordion__panel-5'),
                   (By.ID, 'accordion__panel-6'),
                   (By.ID, 'accordion__panel-7')]

    # Текст ответов для каждого вопроса в FAQ
    ANSWER_TEXTS = ('Сутки — 400 рублей. Оплата курьеру — наличными или картой.',
                    'Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим.',
                    'Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30.',
                    'Только начиная с завтрашнего дня. Но скоро станем расторопнее.',
                    'Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010.',
                    'Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится.',
                    'Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои.',
                    'Да, обязательно. Всем самокатов! И Москве, и Московской области.')
