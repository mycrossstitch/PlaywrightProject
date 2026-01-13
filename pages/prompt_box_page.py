import allure
from playwright.sync_api import expect

from config.links import Links
from base.base_alert_page import BaseAlertPage


class PromptBoxPage(BaseAlertPage):

    url = Links.PROMPT_BOX_PAGE

    @allure.step("Check the prompt result text is '{text}'")
    def check_result_text(self, text: str):
        expect(self.page.locator("#result-text")).to_have_text(text)
