import time

from selenium.webdriver.common.by import By
from test_selenium_po.po_page.base import Base
from test_selenium_po.po_page.addressbook_page import AddressBookPage
from test_selenium_po.po_page.dataparse import DataParse

class AddUserPage(Base):
    # 添加页面内部元素
    _location_username = (By.ID, "username")
    _location_acctid = (By.ID, "memberAdd_acctid")
    _location_Add_phone = (By.ID, "memberAdd_phone")

    def add_user(self):
        """
        添加成员功能
        ，添加成功后返回通讯录页面
        """
        # 问题： driver实例化了多次，影响用例的执行
        # 解决方案： 让driver 只实例化一次
        # self.driver.find_element(By.ID, "username").send_keys("金克斯3")
        # self.driver.find_element(*self._location_username).send_keys("babu")
        # self.driver.find_element(*self._location_acctid).send_keys("020")
        # self.driver.find_element(*self._location_Add_phone).send_keys("13177778882")
        # self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()
        ##use yaml to add userdata
        userinfo = DataParse()
        uname = userinfo.read_and_parse_data()['userconf']['uname']
        actid = userinfo.read_and_parse_data()['userconf']['actid']
        phone = userinfo.read_and_parse_data()['userconf']['phone']
        print(uname,actid,phone)
        time.sleep(5)
        self.find(*self._location_username).send_keys(uname)
        self.find(*self._location_acctid).send_keys(actid)
        self.find(*self._location_Add_phone).send_keys(phone)
        self.driver.find_element(By.CSS_SELECTOR, ".js_btn_save").click()

        return AddressBookPage(self.driver)

    def add_user_fail_operation(self, accid, phone):
        self.driver.find_element(*self._location_username).send_keys("babu")
        self.find(By.ID, "memberAdd_acctid").send_keys(accid)
        self.find(By.ID, "memberAdd_phone").send_keys(phone)
        self.find(By.CSS_SELECTOR, ".js_btn_save").click()
        eles = self.find(By.CSS_SELECTOR, ".ww_inputWithTips_tips")
        error_list = [ele.text for ele in eles]
        return error_list
