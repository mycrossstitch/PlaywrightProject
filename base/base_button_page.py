import allure
from playwright.sync_api import expect
from base.base_page import BasePage


class BaseButtonPage(BasePage):
    BUTTON = "#submit-id-submit"
    RESULT = "#result-text"

    # ---------------- Actions ----------------
    @allure.step("Click on the submit button")
    def click_button(self):
        button = self.page.locator(self.BUTTON)
        button.click()

    # ---------------- Assertions ----------------
    @allure.step("Check that the submit button exists")
    def check_button_exists(self):
        button = self.page.locator(self.BUTTON)
        expect(button).to_be_visible()

    @allure.step("Check that result text is '{text}'")
    def check_result_text_is_(self, text):
        result = self.page.locator(self.RESULT)
        expect(result).to_have_text(text)
