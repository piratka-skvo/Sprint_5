from new_user_function import new_user
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from url import BURGER_URL
from locators.main_page import MainPage
from locators.login_page import LoginPage
from locators.registr_page import RegistrPage
from locators.forgot_page import ForgotPage

class TestLogIn:
    #1 вход по кнопке "Войти в аккаунт" на главной странице
    def test_authorisation_with_button_voiti_v_akk_on_main_page(self, driver):
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
        driver.find_element(*LoginPage.EMAIL_STRING).send_keys(melog)
        driver.find_element(*LoginPage.PASS_STRING).send_keys(mepass)
        driver.find_element(*LoginPage.COMEIN_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(MainPage.ORDER_BUTTON))
        assert 'Оформить заказ' == driver.find_element(*MainPage.ORDER_BUTTON).text

    #2 вход через кнопку "Личный кабинет" на главной странице
    def test_authorisation_with_button_LK_on_main_page(self, driver):
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
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LoginPage.COMEIN_BUTTON))
        #
        driver.get(BURGER_URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(MainPage.LK_BUTTON))
        driver.find_element(*MainPage.LK_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(LoginPage.EMAIL_STRING))

        driver.find_element(*LoginPage.EMAIL_STRING).send_keys(melog)
        driver.find_element(*LoginPage.PASS_STRING).send_keys(mepass)
        driver.find_element(*LoginPage.COMEIN_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(MainPage.ORDER_BUTTON))
        assert 'Оформить заказ' == driver.find_element(*MainPage.ORDER_BUTTON).text

    #3 вход через кнопку "Войти" в форме регистрации
    def test_authorisation_with_button_voiti_on_registration_page(self, driver):
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
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LoginPage.COMEIN_BUTTON))
        #
        driver.find_element(*LoginPage.REGISTR_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(RegistrPage.COME_IN_BUTTON))
        driver.find_element(*RegistrPage.COME_IN_BUTTON).click()
        WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located(LoginPage.COMEIN_BUTTON))

        driver.find_element(*LoginPage.EMAIL_STRING).send_keys(melog)
        driver.find_element(*LoginPage.PASS_STRING).send_keys(mepass)
        driver.find_element(*LoginPage.COMEIN_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(MainPage.ORDER_BUTTON))
        assert 'Оформить заказ' == driver.find_element(*MainPage.ORDER_BUTTON).text
        

    #4 вход через кнопку "Войти" в форме восстановления пароля
    def test_authorisation_with_button_voiti_on_forgotpass_page(self, driver):
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
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable(LoginPage.FORGOT_BUTTON))
        #
        driver.find_element(*LoginPage.FORGOT_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(ForgotPage.COME_IN_BUTTON))
        driver.find_element(*ForgotPage.COME_IN_BUTTON).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(LoginPage.EMAIL_STRING))
        
        driver.find_element(*LoginPage.EMAIL_STRING).send_keys(melog)
        driver.find_element(*LoginPage.PASS_STRING).send_keys(mepass)
        driver.find_element(*LoginPage.COMEIN_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(MainPage.ORDER_BUTTON))
        assert 'Оформить заказ' == driver.find_element(*MainPage.ORDER_BUTTON).text
