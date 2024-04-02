from selenium.webdriver.common.by import By
from test_selenium_po.po_page.base import Base


class AddressBookPage(Base):
    _location_member_list = (By.CSS_SELECTOR, ".member_colRight_memberTable_td:nth-child(2)")
    _location_goto_add_member = (By.CSS_SELECTOR, ".ww_operationBar .js_add_member")

    def goto_add_member(self):
        from test_selenium_po.po_page.adduser_page import AddUserPage

        self.wait_click(self._location_goto_add_member)
        self.find(self._location_goto_add_member).click()
        return AddUserPage(self.driver)

    def get_member_list(self):
        """
        获取成员列表
        :return:
        """
        ele_list = self.finds(*self._location_member_list)
        # 把元素列表 转换为名称列表，使用列表推导式（python-列表）
        member_list = [ele.text for ele in ele_list]
        # 成员的名称的列表
        return member_list
