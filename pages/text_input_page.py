from config.links import Links
from base.base_input_page import BaseInputPage


class TextInputPage(BaseInputPage):
    url = Links.INPUTS_PAGE

    INPUT = "#id_text_string"
    ERROR1 = "#error_1_id_text_string"
    ERROR2 = "#error_2_id_text_string"
