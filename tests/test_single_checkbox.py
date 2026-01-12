import allure
from playwright.sync_api import Page
from pages.single_checkbox_page import OneCheckboxPage


@allure.feature("Checkbox")
@allure.story("Single Checkbox")
@allure.title("Check that there is exactly one checkbox on the page")
def test_one_checkbox_count(page: Page):
    one_checkbox_page = OneCheckboxPage(page)
    one_checkbox_page.open()
    one_checkbox_page.check_checkbox_count(1)


@allure.feature("Checkbox")
@allure.story("Single Checkbox")
@allure.title("Verify the label of the single checkbox")
def test_one_checkbox_label(page: Page):
    one_checkbox_page = OneCheckboxPage(page)
    one_checkbox_page.open()
    one_checkbox_page.check_label(1, "Select me or not")


@allure.feature("Checkbox")
@allure.story("Single Checkbox")
@allure.title("Ensure the user can select the single checkbox")
def test_one_checkbox_can_be_selected(page: Page):
    one_checkbox_page = OneCheckboxPage(page)
    one_checkbox_page.open()
    one_checkbox_page.select_checkbox(1)


@allure.feature("Checkbox")
@allure.story("Single Checkbox")
@allure.title("Check that the submit button is always enabled")
def test_one_checkbox_submit_button_always_enabled(page: Page):
    one_checkbox_page = OneCheckboxPage(page)
    one_checkbox_page.open()
    one_checkbox_page.check_button_enabled()


@allure.feature("Checkbox")
@allure.story("Single Checkbox")
@allure.title(
    "Verify no result is shown when no checkbox is selected and button is pressed"
)
def test_one_checkbox_no_selection_no_result(page: Page):
    one_checkbox_page = OneCheckboxPage(page)
    one_checkbox_page.open()
    one_checkbox_page.click_button()
    one_checkbox_page.check_result_not_displayed()


@allure.feature("Checkbox")
@allure.story("Single Checkbox")
@allure.title(
    "Verify result text is shown when the single checkbox is selected and button is pressed"
)
def test_one_checkbox_selected_shows_result(page: Page):
    one_checkbox_page = OneCheckboxPage(page)
    one_checkbox_page.open()
    one_checkbox_page.select_checkbox(1)
    one_checkbox_page.click_button()
    one_checkbox_page.check_result_text_is("select me or not")
