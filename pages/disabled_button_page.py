import allure
from playwright.sync_api import expect
from config.links import Links
from base.base_button_page import BaseButtonPage


class DisableButtonPage(BaseButtonPage):

    url = Links.DISABLE_BUTTONS_PAGE
    SELECT = "#id_select_state"

    # ---------------- Actions ----------------

    @allure.step("Select state '{value}' from dropdown")
    def select_state(self, value: str):
        """
        value: 'enabled' or 'disabled'
        """
        select = self.page.locator(self.SELECT)
        select.select_option(value)

    # ---------------- Assertions ----------------

    @allure.step("Check that the button is disabled")
    def check_button_disabled(self):
        button = self.page.locator(self.BUTTON)
        expect(button).to_be_disabled()

    @allure.step("Check that the button is enabled")
    def check_button_enabled(self):
        button = self.page.locator(self.BUTTON)
        expect(button).to_be_enabled()

    @allure.step("Check that selected state in dropdown is '{value}'")
    def check_selected_state_is(self, value: str):
        select = self.page.locator(self.SELECT)
        expect(select).to_have_value(value)

    @allure.step("Check that dropdown state '{value}' is applied to button immediately")
    def check_state_applied_to_button(self, value: str):
        """
        Dropdown state should immediately affect button state
        """
        if value == "enabled":
            self.check_button_enabled()
        elif value == "disabled":
            self.check_button_disabled()
        else:
            raise ValueError(f"Unknown state: {value}")
