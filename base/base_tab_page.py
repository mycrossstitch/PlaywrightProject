import allure
from playwright.sync_api import expect
from base.base_page import BasePage
import re


class NewTabPage(BasePage):

    LINK_OR_BUTTON = None
    RESULT = "#result-text"

    # ---------------- Actions ----------------
    @allure.step("Click on the link or button and wait for a new tab to open")
    def click_and_wait_new_tab(self):
        with self.page.context.expect_page() as new_page_info:
            self.page.locator(self.LINK_OR_BUTTON).click()

        self.new_page = new_page_info.value
        self.new_page.wait_for_load_state()

    # ---------------- Assertions ----------------
    @allure.step("Check that a new tab was opened")
    def check_new_tab_opened(self):
        pages = self.page.context.pages
        assert len(pages) == 2, f"Expected 2 tabs, got {len(pages)}"

    @allure.step("Check that the new tab URL ends with '/elements/new_tab/new_page'")
    def check_new_tab_url(self):
        expect(self.new_page).to_have_url(re.compile(r"/elements/new_tab/new_page$"))

    @allure.step("Check that the result text in the new tab is '{text}'")
    def check_new_tab_result_text_is_(self, text):
        result = self.new_page.locator(self.RESULT)
        expect(result).to_have_text(text)
