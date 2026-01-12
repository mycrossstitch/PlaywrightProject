import allure
import pytest
from playwright.sync_api import Page
from pages.text_input_page import TextInputPage
from utils.field_data_helper import generate_test_string


# ---------------- Visibility ----------------


@allure.feature("Input Field")
@allure.story("Text Input Field")
@allure.title("Input field should be visible")
def test_input_text_visible(page: Page):
    text_input_page = TextInputPage(page)
    text_input_page.open()
    text_input_page.check_input_exists()


# ---------------- Valid cases ----------------


@allure.feature("Input Field")
@allure.story("Text Input Field")
@pytest.mark.parametrize(
    "case", ["min", "max", "random", "spaces_random", "spaces_max"]
)
def test_valid_text(page: Page, case):
    text_input_page = TextInputPage(page)
    text_input_page.open()

    if case == "min":
        string = generate_test_string(True, 2)
    elif case == "max":
        string = generate_test_string(True, 25)
    elif case == "random":
        string = generate_test_string(True)
    elif case == "spaces_random":
        string = f" {generate_test_string(True)} "
    elif case == "spaces_max":
        string = f" {generate_test_string(True, 25)} "
    else:
        raise ValueError(f"Unknown case: {case}")

    text_input_page.fill_and_submit(string)
    text_input_page.check_result(string)


# ---------------- Invalid cases ----------------


@allure.feature("Input Field")
@allure.story("Text Input Field")
@pytest.mark.parametrize(
    "case",
    [
        "too_short_valid",
        "too_long_valid",
        "too_short_invalid",
        "too_long_invalid",
        "invalid_chars",
        "only_space",
    ],
)
def test_invalid_text(page: Page, case):
    text_input_page = TextInputPage(page)
    text_input_page.open()

    if case == "too_short_valid":
        string = generate_test_string(True, 1)
        error1 = "Please enter 2 or more characters"
        error2 = None

    elif case == "too_long_valid":
        string = generate_test_string(True, 26)
        error1 = "Please enter no more than 25 characters"
        error2 = None

    elif case == "too_short_invalid":
        string = generate_test_string(False, 1)
        error1 = "Please enter 2 or more characters"
        error2 = "Enter a valid string consisting of letters, numbers, underscores or hyphens."

    elif case == "too_long_invalid":
        string = generate_test_string(False, 26)
        error1 = "Please enter no more than 25 characters"
        error2 = "Enter a valid string consisting of letters, numbers, underscores or hyphens."

    elif case == "invalid_chars":
        string = generate_test_string(False)
        error1 = "Enter a valid string consisting of letters, numbers, underscores or hyphens."
        error2 = None

    elif case == "only_space":
        string = " "
        error1 = "This field is required."
        error2 = None
    else:
        raise ValueError(f"Unknown case: {case}")

    text_input_page.fill_and_submit(string)
    text_input_page.check_error1(error1)
    if error2:
        text_input_page.check_error2(error2)


# ---------------- Empty ----------------


@allure.feature("Input Field")
@allure.story("Text Input Field")
@allure.title("Empty input should show required field error")
def test_input_text_empty(page: Page):
    text_input_page = TextInputPage(page)
    text_input_page.open()
    text_input_page.fill_and_submit("")
    text_input_page.check_required_field_error()
