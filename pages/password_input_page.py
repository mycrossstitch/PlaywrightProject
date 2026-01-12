from config.links import Links
from base.base_input_page import BaseInputPage


class PasswordInputPage(BaseInputPage):
    url = Links.PASSWORD_INPUTS_PAGE

    INPUT = "#id_password"
    ERROR1 = "#error_1_id_password"
