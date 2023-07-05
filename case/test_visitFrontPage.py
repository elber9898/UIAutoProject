import pytest
import time
import step.Step
import module.logger
import step.Step as a

def test_visitFrontPage(driverControl):
    try:
        driver = driverControl
        feedback = a.Step.openHomePage(driver)
        time.sleep(1)
        assert feedback == 0
    except BaseException as e:
        print("Exception: ", repr(e))
        assert 0==1

    # driver = driverControl
    # feedback = a.Step.openHomePage(driver)
    # time.sleep(1)
    # assert feedback == 0

if __name__ == '__main__':
    # pytest.main()
    test_visitFrontPage()