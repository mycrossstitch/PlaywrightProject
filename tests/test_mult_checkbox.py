import allure
import pytest
from playwright.sync_api import Page
from pages.mult_checkbox_page import ThreeCheckboxPage


@allure.feature("Checkbox")
@allure.story("Multy Checkboxes")
@allure.title("Check that there are exactly three checkboxes on the page")
def test_three_checkboxes_count(page: Page):
    three_checkbox_page = ThreeCheckboxPage(page)
    three_checkbox_page.open()
    three_checkbox_page.check_checkbox_count(3)


@allure.feature("Checkbox")
@allure.story("Multy Checkboxes")
@pytest.mark.parametrize("index, label", [(1, "One"), (2, "Two"), (3, "Three")])
def test_three_checkboxes_labels(page: Page, index, label):
    three_checkbox_page = ThreeCheckboxPage(page)
    three_checkbox_page.open()
    three_checkbox_page.check_label(index, label)


@allure.feature("Checkbox")
@allure.story("Multy Checkboxes")
@pytest.mark.parametrize("index", [1, 2, 3])
def test_three_checkboxes_can_be_selected(page: Page, index):
    three_checkbox_page = ThreeCheckboxPage(page)
    three_checkbox_page.open()
    three_checkbox_page.select_checkbox(index)


@allure.feature("Checkbox")
@allure.story("Multy Checkboxes")
@allure.title("Check that the submit button is always enabled")
def test_three_checkboxes_submit_button_always_enabled(page: Page):
    three_checkbox_page = ThreeCheckboxPage(page)
    three_checkbox_page.open()
    three_checkbox_page.check_button_enabled()


@allure.feature("Checkbox")
@allure.story("Multy Checkboxes")
@allure.title("Verify no result is displayed if no checkbox is selected")
def test_three_checkboxes_no_selection_no_result(page: Page):
    three_checkbox_page = ThreeCheckboxPage(page)
    three_checkbox_page.open()
    three_checkbox_page.click_button()
    three_checkbox_page.check_result_not_displayed()


@allure.feature("Checkbox")
@allure.story("Multy Checkboxes")
@pytest.mark.parametrize(
    "indexes, result",
    [
        ([1], "one"),
        ([2], "two"),
        ([3], "three"),
        ([1, 2], "one, two"),
        ([1, 3], "one, three"),
        ([2, 3], "two, three"),
        ([1, 2, 3], "one, two, three"),
    ],
)
def test_three_checkboxes_selected_show_result(page: Page, indexes, result):
    three_checkbox_page = ThreeCheckboxPage(page)
    three_checkbox_page.open()
    for index in indexes:
        three_checkbox_page.select_checkbox(index)
    three_checkbox_page.click_button()
    three_checkbox_page.check_result_text_is(result)
