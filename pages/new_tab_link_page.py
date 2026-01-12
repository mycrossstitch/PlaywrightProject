from config.links import Links
from base.base_tab_page import NewTabPage


class NewTabLinkPage(NewTabPage):

    url = Links.NEW_TAB_LINK_PAGE

    LINK_OR_BUTTON = "#new-page-link"
