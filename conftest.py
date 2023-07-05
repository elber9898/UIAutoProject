import pytest
import step.Step as step
import module.getDriver as getDriver

@pytest.fixture
def driverControl():
    driver = getDriver.GetWebdriver().getWebdriver()
    yield driver
    getDriver.GetWebdriver().destroyDriver(driver)