# test for successful blog post
import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException


class Blog_ATS(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_blog(self):
        continue_test = False
        # replace ID and PW with a valid test username and password
        user = "nishimahato"
        pwd = "HaveFun@8"
        driver = self.driver
        driver.maximize_window()
        driver.get("http://127.0.0.1:8000/admin")
        elem = driver.find_element_by_id("id_username")
        elem.send_keys(user)
        elem = driver.find_element_by_id("id_password")
        elem.send_keys(pwd)
        elem.send_keys(Keys.RETURN)
        driver.get("http://127.0.0.1:8000")
        time.sleep(3)

        # attempt to find and click the plus button - if found,
        # user is logged in and test may continue
        # if not found
        # user is not logged in and test must fail
        try:
            elem = driver.find_element_by_xpath("/html/body/div[1]/a/span").click()
            continue_test = True
        except NoSuchElementException:
            self.fail("Login of user was not successful and test must exit")
            assert False

        if continue_test:
            time.sleep(3)
            elem = driver.find_element_by_id("id_title")
            elem.send_keys("This is a test post with Selenium")
            elem = driver.find_element_by_id("id_text")
            elem.send_keys("This is a test post of text with Selenium")
            time.sleep(3)
            elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/form/button").click()
            try:
                # find the 'edit' pencil icon - if post added, edit pate is displayed
                elem = driver.find_element_by_xpath("/html/body/div[2]/div/div/div/a/span")
                assert True
            except NoSuchElementException:
                self.fail("Add post NOT successful")
                assert False


    def tearDown(self):
        self.driver.close()


if __name__ == "__main__":
    unittest.main()

