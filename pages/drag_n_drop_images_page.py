import allure
from playwright.sync_api import expect
from base.base_page import BasePage
from config.links import Links


class DragNDropImagesPage(BasePage):

    url = Links.DRAG_N_DROP_IMAGES_PAGE

    DROP1 = "#rect-droppable1"
    DROP2 = "#rect-droppable2"
    IMAGE = ".ui-draggable-handle"

    # ---------------- Helpers ----------------

    def _drop1(self):
        return self.page.locator(self.DROP1)

    def _drop2(self):
        return self.page.locator(self.DROP2)

    def _image(self):
        return self.page.locator(self.IMAGE)

    # ---------------- Actions ----------------

    @allure.step("Drag smiley to square 1")
    def drag_to_square1(self):
        self._image().drag_to(self._drop1())

    @allure.step("Drag smiley to square 2")
    def drag_to_square2(self):
        self._image().drag_to(self._drop2())

    # ---------------- Assertions ----------------

    @allure.step("Check that two squares exist")
    def check_two_squares_exist(self):
        expect(self._drop1()).to_be_visible()
        expect(self._drop2()).to_be_visible()

    @allure.step("Check that smiley exists")
    def check_smiley_exists(self):
        expect(self._image()).to_be_visible()

    @allure.step("Check that square {index} contains smiley")
    def check_square_contains_smiley(self, index: int):
        square = self._drop1() if index == 1 else self._drop2()
        expect(square.locator(self.IMAGE)).to_be_visible()

    def check_square_empty(self, index: int):
        square = self._drop1() if index == 1 else self._drop2()
        # Проверяем, что смайлика нет
        expect(square.locator(self.IMAGE)).to_have_count(0)
        # Проверяем, что текст невидим
        text_locator = square.locator(".text-droppable")
        expect(text_locator).not_to_be_visible()

    @allure.step("Check that square {index} shows Dropped!")
    def check_square_shows_dropped(self, index: int):
        square = self._drop1() if index == 1 else self._drop2()
        text_locator = square.locator(".text-droppable")
        expect(text_locator).to_be_visible()
        expect(text_locator).to_have_text("Dropped!")
