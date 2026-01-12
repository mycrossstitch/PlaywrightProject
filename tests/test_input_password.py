import allure
import pytest
from utils.field_data_helper import generate_valid_password, SPECIALS
from pages.password_input_page import PasswordInputPage
from playwright.sync_api import Page

# ---------------- Visibility ----------------


@allure.feature("Input Field")
@allure.story("Password Input Field")
@allure.title("Password input should be visible")
def test_input_password_visible(page: Page):
    password_input_page = PasswordInputPage(page)
    password_input_page.open()
    password_input_page.check_input_exists()


# ---------------- Valid cases ----------------


@allure.feature("Input Field")
@allure.story("Password Input Field")
@pytest.mark.parametrize("i", range(3))
def test_valid_password(page: Page, i):
    password = generate_valid_password()
    password_input_page = PasswordInputPage(page)
    password_input_page.open()
    password_input_page.fill_and_submit(password)
    password_input_page.check_result(password)


@allure.feature("Input Field")
@allure.story("Password Input Field")
@allure.title("Password with length 9 should be valid")
def test_valid_password_9(page: Page):
    password = generate_valid_password(9)
    password_input_page = PasswordInputPage(page)
    password_input_page.open()
    password_input_page.fill_and_submit(password)
    password_input_page.check_result(password)


# ---------------- Empty ----------------


@allure.feature("Input Field")
@allure.story("Password Input Field")
@allure.title("Empty password should show required field error")
def test_empty_password(page: Page):
    password_input_page = PasswordInputPage(page)
    password_input_page.open()
    password_input_page.fill_and_submit("")
    password_input_page.check_required_field_error()


# ---------------- Invalid cases ----------------


@allure.feature("Input Field")
@allure.story("Password Input Field")
@allure.title("Password input with only space should show required error")
def test_password_only_space_is_required(page: Page):
    password_input_page = PasswordInputPage(page)
    password_input_page.open()
    password_input_page.fill_and_submit(" ")
    password_input_page.check_error1("This field is required.")


@allure.feature("Input Field")
@allure.story("Password Input Field")
@pytest.mark.parametrize(
    "case", ["short", "no_upper", "no_lower", "no_digit", "no_special"]
)
def test_invalid_password(page: Page, case):
    password = generate_valid_password()
    if case == "short":
        # Меньше 8 символов
        password = password[:7]
    elif case == "no_upper":
        # Убираем все заглавные
        password = "".join(c for c in password if not c.isupper())
    elif case == "no_lower":
        # Убираем все строчные
        password = "".join(c for c in password if not c.islower())
    elif case == "no_digit":
        # Убираем все цифры
        password = "".join(c for c in password if not c.isdigit())
    elif case == "no_special":
        # Убираем спецсимволы
        password = "".join(c for c in password if c not in SPECIALS)

    password_input_page = PasswordInputPage(page)
    password_input_page.open()
    password_input_page.fill_and_submit(password)
    password_input_page.check_error1("Low password complexity")
