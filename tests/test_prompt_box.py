import allure
from playwright.sync_api import Page
from pages.prompt_box_page import PromptBoxPage


@allure.feature("Alerts")
@allure.story("Prompt Box")
@allure.title("Check button exists")
def test_check_button_exists(page: Page):
    prompt_page = PromptBoxPage(page)
    prompt_page.open()
    prompt_page.check_button_exists()

@allure.feature("Alerts")
@allure.story("Prompt Box")
@allure.title("Clicking prompt button shows alert with correct text")
def test_prompt_box_text(page: Page):
    prompt_page = PromptBoxPage(page)
    prompt_page.open()
    prompt_page.check_alert_text("Please enter some text")
    prompt_page.click_button()

@allure.feature("Alerts")
@allure.story("Prompt Box")
@allure.title("Entering text in prompt and clicking OK displays result")
def test_prompt_box_ok_with_text(page: Page):
    prompt_page = PromptBoxPage(page)
    prompt_page.open()
    prompt_page.send_text_to_alert("Hello")
    prompt_page.click_button()
    prompt_page.check_result_text("Hello")

@allure.feature("Alerts")
@allure.story("Prompt Box")
@allure.title("Clicking Cancel on prompt displays Cancel result")
def test_prompt_box_cancel(page: Page):
    prompt_page = PromptBoxPage(page)
    prompt_page.open()
    prompt_page.dismiss_alert()
    prompt_page.click_button()
    prompt_page.check_result_text("You canceled the prompt")


@allure.feature("Alerts")
@allure.story("Prompt Box")
@allure.title("Entering empty in prompt and clicking OK displays result")
def test_prompt_box_ok(page: Page):
    prompt_page = PromptBoxPage(page)
    prompt_page.open()
    prompt_page.accept_alert()
    prompt_page.click_button()
    prompt_page.check_result_text("You entered nothing")