from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep
from selenium.common import exceptions as selenium_exceptions

from config import *


# driver = webdriver.Firefox()
# driver.get('https://portal.visioniot.net/view/#/')
# assert "Twitter." in driver.title


class MXVision:
    def __init__(self, username: str, password: str):
        self.driver = webdriver.Firefox()

        # login info
        self.username = username
        self.password = password

    def login(self):
        # driver = self.driver
        self.driver.get('https://portal.visioniot.net/view/#/')
        un = self.driver.find_element(by=By.XPATH,
                                      value='//*[@id="root"]/div/div[3]/div/form/div/div[2]/div[1]/div/input')
        pw = self.driver.find_element(by=By.XPATH,
                                      value='//*[@id="root"]/div/div[3]/div/form/div/div[2]/div[2]/div/input')
        sb = self.driver.find_element(by=By.XPATH,
                                      value='//*[@id="root"]/div/div[3]/div/form/div/div[3]/div[1]/button/span[1]')
        # self.un = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/form/div/div[2]/div[1]/div/input')
        # self.pw = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/form/div/div[2]/div[2]/div/input')
        # self.sb = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/form/div/div[3]/div[1]/button/span[1]')
        un.send_keys(self.username)
        pw.send_keys(self.password)
        sb.click()

    def create_program(self):
        driver = self.driver
        sleep(5)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div/div[2]/ul/li[6]/a/div').click()
        sleep(2)
        driver.find_element_by_xpath(
            '/html/body/div[1]/div/div[2]/div[2]/div/div/a[1]/div/button/div[1]/span[1]').click()
        sleep(2)
        driver.find_element_by_xpath('/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/span[1]/button').click()
        sleep(2)
        # prg_name = driver.find_element_by_xpath('/html/body/div[5]/div/div[2]/div/div[2]/div[2]/div/div[1]/form/div[1]/div/div[2]/div/span/div/input')
        prg_name = driver.find_element_by_class_name('ant-input').send_keys('Test Program')
        prg_valid_from = driver.find_element_by_name('ValidFrom').send_keys('24-02-2022')
        prg_valid_to = driver.find_element_by_name('ValidTo').send_keys('31-03-2022')
        add = driver.find_element_by_css_selector('.ant-col-24 > button:nth-child(1)').click()

    def edit_program(self):
        # driver = self.driver
        # 1. click on program management
        try:
            sleep(30)
            self.driver.find_element(by=By.XPATH,
                                     value='/html/body/div[1]/div/div[1]/div[2]/div/div/div[2]/ul/li[5]/a/div').click()
            sleep(10)
            # 2. click on Programs
            self.driver.find_element(by=By.XPATH,
                                     value='/html/body/div[1]/div/div[2]/div[2]/div/div/a[1]/div/button/div[1]').click()
            # 3. Select one program by clicking on it (should be done as a loop later)
            sleep(20)
            self.driver.find_element(by=By.XPATH,
                                     value='/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/span/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div[5]/div[3]/div/span[2]/div').click()

            # 4. Click on Program Items
            sleep(3)
            self.driver.find_element(by=By.XPATH,
                                     value='/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/span[3]/span/button/span[1]').click()
            # 5. Select one program item by clicking on it (again should loop for all items)
            sleep(30)
            self.driver.find_element(by=By.XPATH,
                                     value='/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[2]/span/div/div/div[2]/div[1]/div[3]/div[2]/div/div/div[3]/div[3]').click()
            # 6. Click on Conformity Calculation
            sleep(3)
            self.driver.find_element(by=By.XPATH,
                                     value='/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div[1]/span[3]/span/button').click()
            # 7. Click on the dropdown that opens the list of all metrics
            sleep(10)
            self.driver.find_element(by=By.XPATH,
                                     value='/html/body/div[1]/div/div[2]/div[2]/div/div[2]/div/div/div[3]/div[1]/div[3]/div/div/div/div').click()
            # 8. Loop through the list of metrics
            # For each metric,
            # a. Click on actions button
            # b. Click Edit option
            # c. Find Metric Description. Copy the value in it.
            # d. Find Metric Name. Paste value of Metric Description
            # e. Find Save button. Click on it.
            # 9. Once entire list of metrics is done, Find global Save for all metrics and click on that.

        except selenium_exceptions.NoSuchElementException as e:
            print('Element not found')


session = MXVision(ZM_UN, ZM_PW)
session.login()
session.edit_program()

"""
try:
    # els = driver.find_elements(By.TAG_NAME, 'input')
    un = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/form/div/div[2]/div[1]/div/input')
    pw = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/form/div/div[2]/div[2]/div/input')
    un.send_keys(MX_UN)
    pw.send_keys(MX_PW)
    sb = driver.find_element_by_xpath('//*[@id="root"]/div/div[3]/div/form/div/div[3]/div[1]/button/span[1]').click()
    # sb.send_keys(Keys.RETURN)

    with open('page.html', 'w') as pg:
        pg.write(driver.page_source)


except Exception as e:
    print(e)

"""

# el.clear()
# el.send_keys('pycon')
# el.send_keys(Keys.RETURN)
# assert "No Results Found" not in driver.page_source
# driver.close()
