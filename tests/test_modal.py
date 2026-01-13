import time

import allure
from playwright.sync_api import Page
from pages.modal_page import ModalPage


# ---------------- Launch button ----------------


@allure.feature("Pop-Ups")
@allure.story("Modal")
@allure.title("There should be a button named 'Launch Pop-Up'")
def test_launch_button_exists(page: Page):
    modal_page = ModalPage(page)
    modal_page.open()
    modal_page.check_launch_button_exists()


@allure.feature("Pop-Ups")
@allure.story("Modal")
@allure.title("Launch Pop-Up button opens the modal")
def test_launch_button_opens_modal(page: Page):
    modal_page = ModalPage(page)
    modal_page.open()
    modal_page.open_modal()
    modal_page.check_modal_opened()


# ---------------- Modal content ----------------


@allure.feature("Pop-Ups")
@allure.story("Modal")
@allure.title("Modal has correct title")
def test_modal_title(page: Page):
    modal_page = ModalPage(page)
    modal_page.open()
    modal_page.open_modal()
    modal_page.check_title("I am a Pop-Up")


@allure.feature("Pop-Ups")
@allure.story("Modal")
@allure.title("Modal has checkbox")
def test_modal_checkbox_exists(page: Page):
    modal_page = ModalPage(page)
    modal_page.open()
    modal_page.open_modal()
    modal_page.check_checkbox_exists()


@allure.feature("Pop-Ups")
@allure.story("Modal")
@allure.title("Modal has Cancel and Send buttons")
def test_modal_buttons_exist(page: Page):
    modal_page = ModalPage(page)
    modal_page.open()
    modal_page.open_modal()
    modal_page.check_send_button()
    modal_page.check_cancel_button()


# ---------------- Send behavior ----------------


@allure.feature("Pop-Ups")
@allure.story("Modal")
@allure.title("Selected checkbox value is displayed in Selected checkboxes section")
def test_sent_checkbox_value_is_displayed(page: Page):
    modal_page = ModalPage(page)
    modal_page.open()
    modal_page.open_modal()
    modal_page.select_checkbox()
    modal_page.click_send()
    modal_page.check_sent_value_is_displayed("select me or not")


@allure.feature("Pop-Ups")
@allure.story("Modal")
@allure.title("Selected checkboxes section appears only after sending")
def test_selected_section_appears_after_send(page: Page):
    modal_page = ModalPage(page)
    modal_page.open()
    modal_page.check_result_not_visible()
    modal_page.open_modal()
    modal_page.select_checkbox()
    modal_page.click_send()
    modal_page.check_result_visible()


# ---------------- Negative ----------------


@allure.feature("Pop-Ups")
@allure.story("Modal - Negative")
@allure.title("Close does not send checkbox value")
def test_cancel_does_not_send_value(page: Page):
    modal_page = ModalPage(page)
    modal_page.open()
    modal_page.open_modal()
    modal_page.close_modal()
    modal_page.check_result_not_visible()


@allure.feature("Pop-Ups")
@allure.story("Modal - Negative")
@allure.title("Close does with select checkbox value")
def test_cancel_does_not_send_value(page: Page):
    modal_page = ModalPage(page)
    modal_page.open()
    modal_page.open_modal()
    modal_page.select_checkbox()
    modal_page.close_modal()
    modal_page.check_result_not_visible()


@allure.feature("Pop-Ups")
@allure.story("Modal - Negative")
@allure.title("Send without selecting checkbox does not send value")
def test_send_without_checkbox(page: Page):
    modal_page = ModalPage(page)
    modal_page.open()
    modal_page.open_modal()
    modal_page.click_send()
    modal_page.check_sent_value_is_displayed("None")


@allure.feature("Pop-Ups")
@allure.story("Modal - Negative")
@allure.title("Selected section does not appear until Send is clicked")
def test_selecting_checkbox_does_not_show_result(page: Page):
    modal_page = ModalPage(page)
    modal_page.open()
    modal_page.open_modal()
    modal_page.select_checkbox()
    modal_page.check_result_not_visible()
