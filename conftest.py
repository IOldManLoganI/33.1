import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By

BASE_URL = 'https://b2c.passport.rt.ru'

@pytest.fixture(autouse=True)
def browser():

    pytest.driver = webdriver.Chrome(D:\chromedriver.exe)
    pytest.driver.implicitly_wait(5)
    pytest.driver.maximize_window()
    pytest.driver.get(BASE_URL)

    yield

    print('END')
    pytest.driver.quit()

@pytest.fixture(autouse=True)
def browser_reg_page():

    pytest.driver = webdriver.Chrome(D:\chromedriver.exe)
    pytest.driver.implicitly_wait(5)
    pytest.driver.maximize_window()
    pytest.driver.get(BASE_URL)
    pytest.driver.find_element(By.ID, 'kc-register').click()

    yield

    print('END')
    pytest.driver.quit()


@pytest.fixture(autouse=True)
def browser_PasRec_page():

    pytest.driver = webdriver.Chrome(D:\chromedriver.exe)
    pytest.driver.implicitly_wait(5)
    pytest.driver.maximize_window()
    pytest.driver.get(BASE_URL)
    pytest.driver.find_element(By.ID, 'forgot_password').click()

    yield

    print('END')
    pytest.driver.quit()
