import allure
import pytest
from faker import Faker
from playwright.sync_api import Page

from pages.email_input_page import EmailInputPage

fake = Faker()


INVALID_EMAILS = [
    "A",
    "a@",
    "a@.",
    "@test.com",
    "test@",
    "test@test",
    "test@test.",
    "test@@test.com",
    "test test@test.com",
    "test@test..com",
    "test@.com",
    "test@com.",
    "test@-com.com",
]

# ---------------- Visibility ----------------


@allure.feature("Input Field")
@allure.story("Email Input Field")
@allure.title("Email input should be visible")
def test_input_email_visible(page: Page):
    email_input_page = EmailInputPage(page)
    email_input_page.open()
    email_input_page.check_input_exists()


# ---------------- Valid cases ----------------


@allure.feature("Input Field")
@allure.story("Email Input Field")
@allure.title("Valid email input")
@pytest.mark.parametrize("i", range(3))
def test_valid_email(page: Page, i):
    email = fake.email()
    email_input_page = EmailInputPage(page)
    email_input_page.open()
    email_input_page.fill_and_submit(email)
    email_input_page.check_result(email)


@allure.feature("Input Field")
@allure.story("Email Input Field")
@pytest.mark.parametrize("email", [" olga@ya.ru ", "olga@localhost"])
def test_valid_special_email(page, email):
    email_input_page = EmailInputPage(page)
    email_input_page.open()
    email_input_page.fill_and_submit(email)
    email_input_page.check_result(email)


# ---------------- Empty ----------------


@allure.feature("Input Field")
@allure.story("Email Input Field")
@allure.title("Empty email should show required field error")
def test_empty_email(page: Page):
    email_input_page = EmailInputPage(page)
    email_input_page.open()
    email_input_page.fill_and_submit("")
    email_input_page.check_required_field_error()


# ---------------- Invalid cases ----------------


@allure.feature("Input Field")
@allure.story("Email Input Field")
@allure.title("Email input with only space should show required error")
def test_email_only_space_is_required(page: Page):
    email_input_page = EmailInputPage(page)
    email_input_page.open()
    email_input_page.fill_and_submit(" ")
    email_input_page.check_error1("This field is required.")


@allure.feature("Input Field")
@allure.story("Email Input Field")
@pytest.mark.parametrize("email", INVALID_EMAILS)
def test_invalid_email(page: Page, email):
    email_input_page = EmailInputPage(page)
    email_input_page.open()
    email_input_page.fill_and_submit(email)
    email_input_page.check_error1("Enter a valid email address.")
