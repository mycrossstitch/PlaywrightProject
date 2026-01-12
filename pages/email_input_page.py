from config.links import Links
from base.base_input_page import BaseInputPage


class EmailInputPage(BaseInputPage):
    url = Links.EMAIL_INPUTS_PAGE

    INPUT = "#id_email"
    ERROR1 = "#error_1_id_email"
