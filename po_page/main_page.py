import time

from selenium.webdriver.common.by import By
from test_selenium_po.po_page.base import Base
from test_selenium_po.po_page.adduser_page import AddUserPage
from test_selenium_po.po_page.addressbook_page import AddressBookPage


class MainPage(Base):
    _location_goto_member = (By.CSS_SELECTOR, ".ww_indexImg_AddMember")
    _location_cooperation = (By.XPATH, '//*[@id="menu_cooperation"]')

    def goto_add_member(self):
        """跳转到添加成员名
        :return:
        """
        # 解元祖操作，把元祖内的元素拆分作为不同d的参数传入
        self.find(self._location_goto_member).click()
        self.driver.implicitly_wait(5)
        return AddUserPage(self.driver)

    def goto_address(self):
        """跳转到通讯录页面
        :return:
        """
        self.find(By.ID, "menu_contacts").click()
        return AddressBookPage(self.driver)

    def goto_cooperation(self):
        self.find(self._location_cooperation).click()

    def application_management(self):
        pass

    def back_main(self):
        self.find(By.ID, "menu_index").click()
        self.find(By.CSS_SELECTOR, "a[node-type='cancel'").click()
