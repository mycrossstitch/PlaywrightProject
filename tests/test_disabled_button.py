import allure
import pytest
from playwright.sync_api import Page
from pages.disabled_button_page import DisableButtonPage


@allure.feature("Buttons")
@allure.story("Disabled Button")
@allure.title("Button should be disabled by default")
def test_button_disabled_by_default(page: Page):
    disable_button_page = DisableButtonPage(page)
    disable_button_page.open()
    disable_button_page.check_button_disabled()


@allure.feature("Buttons")
@allure.story("Disabled Button")
@allure.title("User can enable the button via dropdown")
def test_enable_button(page: Page):
    disable_button_page = DisableButtonPage(page)
    disable_button_page.open()
    disable_button_page.select_state("enabled")
    disable_button_page.check_selected_state_is("enabled")
    disable_button_page.check_button_enabled()


@allure.feature("Buttons")
@allure.story("Disabled Button")
@allure.title("User can disable the button again after enabling")
def test_disable_button_again(page: Page):
    disable_button_page = DisableButtonPage(page)
    disable_button_page.open()
    disable_button_page.select_state("enabled")
    disable_button_page.select_state("disabled")
    disable_button_page.check_selected_state_is("disabled")
    disable_button_page.check_button_disabled()


@allure.feature("Buttons")
@allure.story("Disabled Button")
@pytest.mark.parametrize("state", ["enabled", "disabled"])
def test_dropdown_state_is_applied_immediately(page: Page, state):
    disable_button_page = DisableButtonPage(page)
    disable_button_page.open()
    disable_button_page.select_state(state)
    disable_button_page.check_selected_state_is(state)
    disable_button_page.check_state_applied_to_button(state)


@allure.feature("Buttons")
@allure.story("Disabled Button")
@allure.title("Press button and check result")
def test_button_press(page: Page):
    disable_button_page = DisableButtonPage(page)
    disable_button_page.open()
    disable_button_page.select_state("Enabled")
    disable_button_page.click_button()
    disable_button_page.check_result_text_is_("Submitted")
