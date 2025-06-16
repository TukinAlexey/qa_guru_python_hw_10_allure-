from selene.support import by
from selene.support.conditions import be
from selene.support.shared.jquery_style import s


def test_github(open_browser):

    s('[data-target="qbsearch-input.inputButtonText"]').click()
    s('#query-builder-test').send_keys("qa_guru_python_hw_10_allure-").press_enter()

    s(by.partial_link_text('python_hw_10_allure-')).click()

    s('[data-content="Issues"').click()

    s(by.text("test_issue")).should(be.visible)
