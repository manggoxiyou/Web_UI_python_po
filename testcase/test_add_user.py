import pytest
import yaml
from test_selenium_po.po_page.main_page import MainPage

class TestAddUser:
    def setup_class(self):
        self.main = MainPage()

    def test_add_user(self):
        res = self.main.goto_add_member().add_user().get_member_list()
        assert "sdf1" in res

