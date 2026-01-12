import allure
from playwright.sync_api import expect
from base.base_page import BasePage


class BaseInputPage(BasePage):
    INPUT = None
    RESULT = "#result-text"
    ERROR1 = None
    ERROR2 = None

    # ---------------- Actions ----------------
    @allure.step("Fill input with value '{value}' and submit")
    def fill_and_submit(self, value):
        field = self.page.locator(self.INPUT)
        field.fill(value)
        field.press("Enter")

    # ---------------- Assertions ----------------
    @allure.step("Check that input field exists")
    def check_input_exists(self):
        input_field = self.page.locator(self.INPUT)
        expect(input_field).to_be_visible()

    @allure.step("Check that result text is '{expected_text}'")
    def check_result(self, expected_text):
        expect(self.page.locator(self.RESULT)).to_have_text(expected_text)

    @allure.step("Check that error '{error_locator}' has text '{expected_text}'")
    def check_error(self, error_locator, expected_text):
        expect(self.page.locator(error_locator)).to_have_text(expected_text)

    @allure.step("Check that ERROR1 has text '{expected_text}'")
    def check_error1(self, expected_text):
        self.check_error(self.ERROR1, expected_text)

    @allure.step("Check that ERROR2 has text '{expected_text}'")
    def check_error2(self, expected_text):
        self.check_error(self.ERROR2, expected_text)

    @allure.step("Check that required field error is displayed")
    def check_required_field_error(self):
        possible_messages = [
            "Пожалуйста, заполните это поле",
            "Заполните это поле",
            "Необходимо заполнить это поле",
            "Please fill out this field",
            "Please fill in this field",
            "Fill out this field",
            "This field is required",
            "You need to fill out this field",
        ]

        for message in possible_messages:
            locator = self.page.locator(f"text={message}")
            if locator.count() > 0:
                expect(locator).to_be_visible()
                return
