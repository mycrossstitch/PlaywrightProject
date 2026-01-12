import allure
from playwright.sync_api import expect
from base.base_page import BasePage
from config.links import Links


class IFramePage(BasePage):

    url = Links.IFRAMES_PAGE
    IFRAME = ".embed-responsive-item"

    # ---------------- Actions ----------------

    def get_frame(self):
        return self.page.frame_locator(self.IFRAME)

    # ---------------- Assertions ----------------

    @allure.step("Check iframe exists")
    def check_iframe_exists(self):
        iframe = self.page.locator(self.IFRAME)
        expect(iframe).to_be_visible()

    @allure.step("Check iframe_contains_title")
    def check_iframe_contains_title(self):
        frame = self.get_frame()
        heading = frame.get_by_role("heading", name="Album example")
        expect(heading).to_be_visible()
