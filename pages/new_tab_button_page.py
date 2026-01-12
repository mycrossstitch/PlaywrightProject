from config.links import Links
from base.base_tab_page import NewTabPage


class NewTabButtonPage(NewTabPage):

    url = Links.NEW_TAB_BUTTON_PAGE

    LINK_OR_BUTTON = "#new-page-button"
