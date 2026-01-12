from config.links import Links
from base.base_checkbox_page import BaseCheckboxPage


class ThreeCheckboxPage(BaseCheckboxPage):
    url = Links.MULT_CHECKBOX_PAGE

    CHECKBOX1 = "#id_checkboxes_0"
    CHECKBOX2 = "#id_checkboxes_1"
    CHECKBOX3 = "#id_checkboxes_2"

    LABEL1 = "label[for='id_checkboxes_0']"
    LABEL2 = "label[for='id_checkboxes_1']"
    LABEL3 = "label[for='id_checkboxes_2']"
