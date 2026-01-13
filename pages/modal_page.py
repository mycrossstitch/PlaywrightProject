import allure
from playwright.sync_api import expect
from base.base_modal_page import BaseModalPage
from config.links import Links


class ModalPage(BaseModalPage):

    url = Links.MODAL_POPUP_PAGE

    CHECKBOX = "#id_checkbox_0"
    SEND = "#exampleModal button:has-text('Send')"


    # ---------- Actions ----------

    @allure.step("Select checkbox")
    def select_checkbox(self):
        self.page.locator(self.CHECKBOX).check()

    @allure.step("Click Send")
    def click_send(self):
        self.page.locator(self.SEND).click()

    # ---------- Assertions ----------




    @allure.step("Check checkbox exists")
    def check_checkbox_exists(self):
        expect(self.page.locator(self.CHECKBOX)).to_be_visible()

    @allure.step("Check Send button exists")
    def check_send_button(self):
        expect(self.page.locator(self.SEND)).to_be_visible()



    @allure.step("Check Cancel button exists")
    def check_cancel_button(self):
        expect(self.page.locator(self.CANCEL)).to_be_visible()




