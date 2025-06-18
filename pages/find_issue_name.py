import allure
from selene.support.shared.jquery_style import s
from selene.support.conditions import be
from selene.support import by


class IssueName:
    @allure.step("Ищем репозиторий {value}")
    def search_for_repository(self, value):
        s('[data-target="qbsearch-input.inputButtonText"]').click()
        s('#query-builder-test').send_keys(value).press_enter()

    @allure.step("Открываем репозиторий {value}")
    def go_to_repository(self, value):
        s(by.partial_link_text(value)).click()

    @allure.step("Открываем вкладку Issues")
    def open_issue_tab(self):
        s('[data-content="Issues"').click()

    @allure.step("Проверяем наличие Issue с названием {value}")
    def should_see_issue_with_name(self, value):
        s(by.text(value)).should(be.visible)
