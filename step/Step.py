from selenium import webdriver
import time
from selenium.webdriver.common.by import By

class Step:
    def openHomePage(self, driver):
        print("enter openHomePage()\n")
        # driver = webdriver.Edge()
        driver.get('http://47.109.26.120/frontPage.html')
        time.sleep(1)
        if driver.find_element(by=By.CLASS_NAME, value='website_title'):
            return 0
        else:
            return 1

    def gotoSuccessPage(self, driver):
        print("enter successPage()\n")
        driver.find_element(by=By.ID, value='my').click()
        time.sleep(1)
        if driver.find_element(by=By.XPATH, value='/html/body/a').is_displayed():
            return 0
        else:
            return 1

if __name__ == '__main__':
    t = Step()
    t.openHomePage()
