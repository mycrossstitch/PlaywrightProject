import allure
from playwright.sync_api import Page
from pages.drag_n_drop_images_page import DragNDropImagesPage
import time


@allure.feature("Drag and Drop")
@allure.story("Drag images between squares")
@allure.title("Two squares exist")
def test_two_squares_and_smiley_exist(page: Page):
    drag_n_drop_images_page = DragNDropImagesPage(page)
    drag_n_drop_images_page.open()
    drag_n_drop_images_page.check_two_squares_exist()

@allure.feature("Drag and Drop")
@allure.story("Drag images between squares")
@allure.title("Smiley exist")
def test_smiley_exist(page: Page):
    drag_n_drop_images_page = DragNDropImagesPage(page)
    drag_n_drop_images_page.open()
    drag_n_drop_images_page.check_smiley_exists()

@allure.feature("Drag and Drop")
@allure.story("Drag images between squares")
@allure.title("Smiley can be dragged infinitely between squares")
def test_smiley_can_be_dragged_many_times(page: Page):
    drag_n_drop_images_page = DragNDropImagesPage(page)
    drag_n_drop_images_page.open()
    drag_n_drop_images_page.drag_to_square2()
    drag_n_drop_images_page.check_square_shows_dropped(2)
    drag_n_drop_images_page.drag_to_square1()
    drag_n_drop_images_page.check_square_shows_dropped(1)
    drag_n_drop_images_page.drag_to_square2()
    drag_n_drop_images_page.check_square_shows_dropped(2)


@allure.feature("Drag and Drop")
@allure.story("Drag images between squares")
@allure.title("Dropping smiley into square 2 shows result end empty square 1")
def test_drop_into_square1(page: Page):
    drag_n_drop_images_page = DragNDropImagesPage(page)
    drag_n_drop_images_page.open()
    drag_n_drop_images_page.drag_to_square2()
    drag_n_drop_images_page.check_square_shows_dropped(2)
    drag_n_drop_images_page.check_square_empty(1)


@allure.feature("Drag and Drop")
@allure.story("Drag images between squares")
@allure.title("Dropping smiley into square 1 shows result end empty square 2")
def test_drop_into_square2(page: Page):
    drag_n_drop_images_page = DragNDropImagesPage(page)
    drag_n_drop_images_page.open()
    drag_n_drop_images_page.drag_to_square2()
    drag_n_drop_images_page.drag_to_square1()
    drag_n_drop_images_page.check_square_shows_dropped(1)
    drag_n_drop_images_page.check_square_empty(2)


