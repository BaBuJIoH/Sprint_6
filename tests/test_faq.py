import pytest
import allure
from pages.main_page import MainPage
from locators.main_page_locators import MainPageLocators

class TestFAQ(MainPage):
    def __init__(self, driver):
        super().__init__(driver)

    # Проверки соответствия ответов ожидаемым в FAQ через параметризацию
    @allure.title('Проверка соответствия ответов ожидаемым в FAQ')
    @allure.description('Нажимаем на стрелку вопроса, дожидаемся появления ответа. Проверяем, что каждый ответ соответствует ожидаемому для данного вопроса.')
    @pytest.mark.parametrize("question_index", [0, 1, 2, 3, 4, 5, 6, 7])
    def test_faq_questions(self, question_index):
        self.click_question(question_index)
        answer_text = self.get_answer_text(question_index)
        assert answer_text == MainPageLocators.ANSWER_TEXTS[question_index], "Текст ответа не соответствует ожидаемому"
