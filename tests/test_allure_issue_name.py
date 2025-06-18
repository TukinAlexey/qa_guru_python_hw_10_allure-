import allure
from allure_commons.types import Severity
from selene.support import by
from selene.support.conditions import be
from selene.support.shared.jquery_style import s
from pages.find_issue_name import IssueName


def test_issue_name_only_selen(open_browser):
    s('[data-target="qbsearch-input.inputButtonText"]').click()
    s('#query-builder-test').send_keys("qa_guru_python_hw_10_allure-").press_enter()

    s(by.partial_link_text('python_hw_10_allure-')).click()

    s('[data-content="Issues"').click()

    s(by.text("test_issue")).should(be.visible)


def test_issue_name_dynamic_steps(open_browser):
    with allure.step("Ищем репозиторий"):
        s('[data-target="qbsearch-input.inputButtonText"]').click()
        s('#query-builder-test').send_keys("qa_guru_python_hw_10_allure-").press_enter()
    with allure.step("Открываем репозиторий"):
        s(by.partial_link_text('python_hw_10_allure-')).click()
    with allure.step("Открываем вкладку Issues"):
        s('[data-content="Issues"').click()
    with allure.step("Проверяем наличие Issue с названием test_issue"):
        s(by.text("test_issue")).should(be.visible)


def test_issue_name_decorator_steps(open_browser):
    issue_name = IssueName()

    issue_name.search_for_repository('qa_guru_python_hw_10_allure-')
    issue_name.go_to_repository("qa_guru_python_hw_10_allure-")
    issue_name.open_issue_tab()
    issue_name.should_see_issue_with_name("test_issue")


@allure.tag("test")
@allure.severity(Severity.MINOR)
@allure.label('owner', 'atukin')
@allure.feature('Issues_name')
@allure.story('Проверка названия Issue')
@allure.link('https://github.com', name='Testing')
def test_allure_labels():
    pass
