from new_user_function import new_user
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from url import BURGER_URL
from locators.main_page import MainPage
from locators.login_page import LoginPage
from locators.registr_page import RegistrPage

class TestRegistration:
#1 тест успешная регистрация с корректными данными
    def test_registration_successful(self, driver):
        driver.get(BURGER_URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPage.LK_BUTTON))
        driver.find_element(*MainPage.LK_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPage.REGISTR_BUTTON))
    
        driver.find_element(*LoginPage.REGISTR_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(RegistrPage.REGISTR_TITLE))
        driver.find_element(*RegistrPage.NAME_STRING).send_keys("MElvira")
        melog, mepass=new_user()
        driver.find_element(*RegistrPage.EMAIL_STRING).send_keys(melog)
        driver.find_element(*RegistrPage.PASS_STRING).send_keys(mepass)
        driver.find_element(*RegistrPage.REGISTR_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LoginPage.COMEIN_TITLE))
    
        driver.get(BURGER_URL)
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(MainPage.COME_IN_ACC_BUTTON))
        driver.find_element(*MainPage.COME_IN_ACC_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(LoginPage.COMEIN_BUTTON))

        driver.find_element(*LoginPage.EMAIL_STRING).send_keys(melog)
        driver.find_element(*LoginPage.PASS_STRING).send_keys(mepass)
        driver.find_element(*LoginPage.COMEIN_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(MainPage.ORDER_BUTTON))
        assert 'Оформить заказ' == driver.find_element(*MainPage.ORDER_BUTTON).text


    #2 тест ошибки регистрации с некорректным паролем
    def test_registration_error_password(self, driver):
        driver.get(BURGER_URL)

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPage.LK_BUTTON))
        driver.find_element(*MainPage.LK_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPage.REGISTR_BUTTON))
        
        driver.find_element(*LoginPage.REGISTR_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(RegistrPage.REGISTR_TITLE))
        driver.find_element(*RegistrPage.NAME_STRING).send_keys("MElvira")
        melog, mepass=new_user()
        driver.find_element(*RegistrPage.EMAIL_STRING).send_keys(melog)
        driver.find_element(*RegistrPage.PASS_STRING).send_keys("123")
        driver.find_element(*RegistrPage.REGISTR_BUTTON).click()

        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(RegistrPage.ERROR_PASS))
        assert 'Некорректный пароль' == driver.find_element(*RegistrPage.ERROR_PASS).text