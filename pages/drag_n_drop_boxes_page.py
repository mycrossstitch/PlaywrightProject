import re

import allure
from playwright.sync_api import expect
from base.base_page import BasePage
from config.links import Links


class DragNDropBoxesPage(BasePage):

    url = Links.DRAG_N_DROP_BOXES_PAGE

    DROP = "#rect-droppable"
    DRAG = "#rect-draggable"
    RESULT = "#text-droppable"

    # ---------------- Actions ----------------
    @allure.step("Drag bottom square to top square")
    def drag_and_drop(self):
        self.page.locator(self.DRAG).drag_to(self.page.locator(self.DROP))

    # ---------------- Assertions ----------------

    @allure.step("Check that two squares are present on the page")
    def check_two_squares_exist(self):
        expect(self.page.locator(self.DRAG)).to_be_visible()
        expect(self.page.locator(self.DROP)).to_be_visible()

    @allure.step("Check that bottom square is draggable")
    def check_bottom_square_is_draggable(self):
        draggable = self.page.locator(self.DRAG)
        expect(draggable).to_have_class(re.compile("ui-draggable"))

    @allure.step("Try to drag bottom square again and verify nothing changes")
    def try_drag_again_and_verify_no_effect(self):
        drop = self.page.locator(self.DROP)
        before = drop.inner_text()

        # пробуем перетащить снова
        self.page.locator(self.DRAG).drag_to(drop)

        after = drop.inner_text()
        assert before == after, "Bottom square was draggable more than once"

    @allure.step("Check that result text is '{text}'")
    def check_result_text_is_(self, text):
        result = self.page.locator(self.RESULT)
        expect(result).to_have_text(text)
