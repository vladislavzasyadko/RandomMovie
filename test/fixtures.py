import pytest
from appium import webdriver
import constants as cnst

desired_caps = {
  "deviceName": "emulator-5554",
  "platformName": "Android",
  "appPackage": cnst.APP_PACKAGE,
  "appActivity": cnst.APP_ACTIVITY,
  "noReset": True
}

@pytest.fixture(scope="session")
def driver():
    driver = webdriver.Remote(cnst.WEBDRIVER_LOCALHOST, desired_caps)

    yield driver
