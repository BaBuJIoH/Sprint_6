import pytest
import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators

# Проверки соответствия ответов ожидаемым в FAQ через параметризацию
@allure.title('Проверка соответствия ответов ожидаемым в FAQ')
@allure.description('Нажимаем на стрелку вопроса, дожидаемся появления ответа. Проверяем, что каждый ответ соответствует ожидаемому для данного вопроса.')
@pytest.mark.parametrize("question_index", [0, 1, 2, 3, 4, 5, 6, 7])
def test_faq_questions(driver, question_index):
    main_page = MainPage(driver)
    question_element = driver.find_element(*MainPageLocators.QUESTIONS[question_index])
    driver.execute_script("arguments[0].scrollIntoView();", question_element)
    WebDriverWait(driver, 3).until(
        EC.element_to_be_clickable(MainPageLocators.QUESTIONS[question_index])
    )
    main_page.click_question(question_index)
    answer_text = main_page.get_answer_text(question_index)
    assert answer_text == MainPageLocators.ANSWER_TEXTS[question_index], "Текст ответа не соответствует ожидаемому"
