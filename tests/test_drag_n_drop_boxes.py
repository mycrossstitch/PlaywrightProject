import allure
from playwright.sync_api import Page
from pages.drag_n_drop_boxes_page import DragNDropBoxesPage


@allure.feature("Drag and Drop")
@allure.story("Drag and drop boxes")
@allure.title("Check that two squares are displayed on the page")
def test_check_two_squares_exist(page: Page):
    drag_n_drop_boxes_page = DragNDropBoxesPage(page)
    drag_n_drop_boxes_page.open()
    drag_n_drop_boxes_page.check_two_squares_exist()


@allure.feature("Drag and Drop")
@allure.story("Drag and drop boxes")
@allure.title("Check that bottom square is draggable")
def test_bottom_square_is_draggable(page: Page):
    drag_n_drop_boxes_page = DragNDropBoxesPage(page)
    drag_n_drop_boxes_page.open()
    drag_n_drop_boxes_page.check_bottom_square_is_draggable()


@allure.feature("Drag and Drop")
@allure.story("Drag and drop boxes")
@allure.title("Dragging bottom square to top shows 'Dropped!' text")
def test_drag_and_drop_shows_result(page: Page):
    drag_n_drop_boxes_page = DragNDropBoxesPage(page)
    drag_n_drop_boxes_page.open()
    drag_n_drop_boxes_page.drag_and_drop()
    drag_n_drop_boxes_page.check_result_text_is_("Dropped!")


@allure.feature("Drag and Drop")
@allure.story("Drag and drop boxes")
@allure.title("Bottom square can be dragged only once")
def test_bottom_square_can_be_dragged_only_once(page: Page):
    drag_n_drop_boxes_page = DragNDropBoxesPage(page)
    drag_n_drop_boxes_page.open()

    drag_n_drop_boxes_page.drag_and_drop()
    drag_n_drop_boxes_page.check_result_text_is_("Dropped!")

    drag_n_drop_boxes_page.try_drag_again_and_verify_no_effect()
