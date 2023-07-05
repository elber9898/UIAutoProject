import pytest
import time
import step.Step as a
from selenium.webdriver.common.by import By
import module.logger

def test_visitSuccessPage(driverControl):
    try:
        LOGGER = module.logger.init_log('test_visitSuccessPage')
        LOGGER.info('Logger create success!!!!!')

        driver = driverControl
        LOGGER.info('获取到Driver')
        a.Step().openHomePage(driver)
        LOGGER.info('进入HomePage')
        feedback = a.Step().gotoSuccessPage(driver)
        print("feedback=", feedback)
        LOGGER.info('进入SuccessPage')
        assert 0 == feedback

    except BaseException as e:
        print(repr(e))
        assert 0==1

if __name__ == '__main__':
    test_visitSuccessPage()
