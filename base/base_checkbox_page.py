import allure
from playwright.sync_api import expect
from base.base_page import BasePage


class BaseCheckboxPage(BasePage):
    BUTTON = "#submit-id-submit"
    RESULT = "#result-text"

    CHECKBOX1 = None
    CHECKBOX2 = None
    CHECKBOX3 = None

    LABEL1 = None
    LABEL2 = None
    LABEL3 = None

    # ---------------- Actions ----------------

    @allure.step("Select checkbox #{index}")
    def select_checkbox(self, index: int):
        locator = self._get_checkbox(index)
        locator.check()

    @allure.step("Unselect checkbox #{index}")
    def unselect_checkbox(self, index: int):
        locator = self._get_checkbox(index)
        locator.uncheck()

    @allure.step("Click on the submit button")
    def click_button(self):
        self.page.locator(self.BUTTON).click()

    # ---------------- Helpers ----------------

    def _get_checkbox(self, index: int):
        selector = getattr(self, f"CHECKBOX{index}")
        return self.page.locator(selector)

    def _get_label(self, index: int):
        selector = getattr(self, f"LABEL{index}")
        return self.page.locator(selector)

    # ---------------- Assertions ----------------

    @allure.step("Check that there are {count} checkboxes")
    def check_checkbox_count(self, count: int):
        checkboxes = [self.CHECKBOX1, self.CHECKBOX2, self.CHECKBOX3]
        actual = [c for c in checkboxes if c is not None]
        assert len(actual) == count, f"Expected {count} checkboxes, got {len(actual)}"

    @allure.step("Check that label of checkbox #{index} is '{text}'")
    def check_label(self, index: int, text: str):
        expect(self._get_label(index)).to_have_text(text)

    @allure.step("Check that the submit button is enabled")
    def check_button_enabled(self):
        expect(self.page.locator(self.BUTTON)).to_be_enabled()

    @allure.step("Check that the result is not displayed")
    def check_result_not_displayed(self):
        expect(self.page.locator(self.RESULT)).not_to_be_visible()

    @allure.step("Check that result text is '{text}'")
    def check_result_text_is(self, text):
        expect(self.page.locator(self.RESULT)).to_have_text(text)
