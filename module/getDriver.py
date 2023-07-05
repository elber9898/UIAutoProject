from selenium import webdriver
import time

class GetWebdriver:
    def getWebdriver(self):
        driver = webdriver.Edge()
        print("\n返回driver")
        return driver

    def destroyDriver(self, driver):
        print("\n销毁driver")
        driver.quit()

if __name__ == "__main__":
    g = GetWebdriver()
    driver = g.getWebdriver()
    g.destroyDriver(driver)