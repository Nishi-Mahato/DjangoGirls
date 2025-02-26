import unittest
import time

from pkg_resources.extern import names
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException
import names


class Blog_ATS(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        user = "instructor"
        pwd = "instructor1a"
        newuser = names.get_first_name()
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)

        try:
            # attempt to find the plus button - if found, logged in
            elem = driver.find_element_by_xpath("//*[@id='content-main']/div[1]/table/tbody/tr[2]/td[1]/a")
            elem.click()
            elem = driver.find_element_by_id("id_username")
            elem.send_keys(newuser)
            elem = driver.find_element_by_id("id_password1")
            elem.send_keys('pwd12345')
            elem = driver.find_element_by_id("id_password2")
            elem.send_keys('pwd12345')
            elem.send_keys(Keys.RETURN)
            elem1 = driver.find_element_by_xpath("// *[ @ id = 'container'] / ul / li").text
            print('User ' + newuser + ' is added with a message -> ' + elem1)

            assert True
        except NoSuchElementException:
            self.fail("User could not be added")
            assert False

        time.sleep(3)

    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()
