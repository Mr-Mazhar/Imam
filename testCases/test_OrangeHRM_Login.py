import time

from selenium import webdriver
from selenium.webdriver.common.by import By

from pageObjects.Login_Page import LoginPage_Class
from utilities.readConfigFile import ReadConfig_Class


class Test_OrangeHRM_Login:
    Username = ReadConfig_Class.getUsername()
    Password = ReadConfig_Class.getPassword()

    def test_OrangeHRM_url_001(self, setup):
        self.driver = setup
        print("driver.title-->" + self.driver.title)
        if self.driver.title == "OrangeHRM":
            time.sleep(2)
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_url_001_pass.png")
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_url_001_fail.png")
            assert False
        self.driver.quit()

    def test_OrangeHRM_Login_002(self, setup):
        self.driver = setup
        self.lp = LoginPage_Class(self.driver)
        time.sleep(4)
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Username']").send_keys("Admin")
        print("Username-->" + self.Username)
        print("Password-->" + self.Password)
        self.lp.Enter_UserName(self.Username)
        # self.driver.find_element(By.XPATH, "//input[@placeholder='Password']").send_keys("admin123")
        self.lp.Enter_Password(self.Password)
        # self.driver.find_element(By.XPATH, "//button[normalize-space()='Login']").click()
        self.lp.Click_LoginButton()
        if self.lp.Validate_Login_Stauts() == "LoginPass":
            time.sleep(2)
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_002_pass.png")
            self.lp.Click_Menu_Button()
            self.lp.Click_Logout_Button()
            assert True
        else:
            self.driver.save_screenshot(".\\Screenshots\\test_OrangeHRM_Login_002_fail.png")
            assert False

        self.driver.quit()

# Pytest -v -s --html=HTMLReports/myreport.html --allure="AllureReports" -n=4 -m -k
# generally in automation  as a tester we have to capture screenshots for fail case

# screenshots in other ways--> assignment , specific area portion screenshot capture
