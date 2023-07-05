import pytest
import time
from selenium.webdriver.common.by import By
import module.logger

def test_testConftest(driverControl):
    try:
        LOGGER = module.logger.init_log('test_testConftest')
        LOGGER.info('Logger create success!!!!!')

        driver = driverControl
        driver.get("https://cn.bing.com/")
        time.sleep(1)
        # driver.find_element(By.CLASS_NAME,'sb_form_q').send_keys('hello')
        assert driver.find_element(By.CLASS_NAME, 'ms_text').is_displayed()

        # driver = driverControl
        # driver.get('http://47.109.26.120/frontPage.html')
        # time.sleep(1)
        # driver.find_element(by=By.ID, value='my').click()
        # time.sleep(1)
        # driver.find_element(by=By.XPATH, value='/html/body/a').is_displayed()
    except BaseException as e:
        print(repr(e))
        assert 0==1

if __name__ == '__main__':
    test_testConftest()
