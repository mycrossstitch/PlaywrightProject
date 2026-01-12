from config.links import Links
from base.base_checkbox_page import BaseCheckboxPage


class OneCheckboxPage(BaseCheckboxPage):
    url = Links.SINGLE_CHECKBOX_PAGE

    CHECKBOX1 = "#id_checkbox_0"
    LABEL1 = "label[for='id_checkbox_0']"
