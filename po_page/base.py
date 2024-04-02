import keyword
import logging
import pytest
import requests
import yaml
from selenium import webdriver
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class Base:
    __url="https://work.weixin.qq.com/wework_admin/frame#index"
    def __init__(self, base_driver=None):
        base_driver: WebDriver
        if base_driver is None:
            self.driver = webdriver.Firefox()
            self.driver.get("https://work.weixin.qq.com/wework_admin/loginpage_wx?")
            self.__cookie_login()

        else:
            self.driver = base_driver
        self.driver.implicitly_wait(3)


    # 从文件中读取cookie
    def __cookie_login(self):
        with open("../data_resource/cookies.yaml", encoding="UTF-8") as f:
            cookies_data = yaml.safe_load(f)
            for cookie in cookies_data:
                self.driver.add_cookie(cookie)
            self.driver.get(self.__url)
    def find(self, by, value=None):
        if value is None:
            return self.driver.find_element(*by)
        else:
            return self.driver.find_element(by=by, value=value)

    def finds(self, by, value=None):
        if value is None:
            # 如果传入的是一个元祖，则进行解包元祖传参
            return self.driver.find_elements(*by)
        else:
            # 如果传入的是正常的定位信息，则正常传参
            return self.driver.find_elements(by=by, value=value)

    def back_start_page(self):
        """
        回退到用例开始的页面。
        :return:
        """
        self.driver.get('https://work.weixin.qq.com/wework_admin/frame#contacts')

    def wait_click(self, locator):
        return WebDriverWait(self.driver, 9).until(expected_conditions.element_to_be_clickable(locator))

    def quit(self):
        self.driver.close()
#
# if __name__ == '__main__':
#    A = Basepage()