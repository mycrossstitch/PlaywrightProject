import allure
from playwright.sync_api import expect
from base.base_page import BasePage


class BaseModalPage(BasePage):
    LAUNCH = "button:has-text('Launch Pop-Up')"
    MODAL = "#exampleModal"
    TITLE = "#exampleModalLabel"
    CANCEL = "#exampleModal button:has-text('Close')"
    RESULT = "#result-text"

    # ---------- Actions ----------

    @allure.step("Open modal pop-up")
    def open_modal(self):
        self.page.locator(self.LAUNCH).click()

    @allure.step("Close modal with Cancel")
    def close_modal(self):
        self.page.locator(self.CANCEL).click()

    # ---------- Assertions ----------

    @allure.step("Check launch button exists")
    def check_launch_button_exists(self):
        expect(self.page.locator(self.LAUNCH)).to_be_visible()

    @allure.step("Check modal is opened")
    def check_modal_opened(self):
        expect(self.page.locator(self.MODAL)).to_be_visible()

    @allure.step("Check modal is closed")
    def check_modal_closed(self):
        expect(self.page.locator(self.MODAL)).not_to_be_visible()

    @allure.step("Check selected value block is visible")
    def check_result_visible(self):
        expect(self.page.locator(self.RESULT)).to_be_visible()

    @allure.step("Check result block is not visible")
    def check_result_not_visible(self):
        expect(self.page.locator(self.RESULT)).not_to_be_visible()

    @allure.step("Check that sent value is displayed in Selected checkboxes")
    def check_sent_value_is_displayed(self, expected_text: str):
        result = self.page.locator(self.RESULT)
        expect(result).to_have_text(expected_text)

    @allure.step("Check modal title")
    def check_title(self, text):
        expect(self.page.locator(self.TITLE)).to_have_text(text)
