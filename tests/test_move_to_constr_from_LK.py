from new_user_function import new_user
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from url import BURGER_URL
from locators.main_page import MainPage
from locators.login_page import LoginPage
from locators.registr_page import RegistrPage
from locators.lk_page import LkPage

class TestMoveToConstr:
    #1 переход в конструктор из ЛК по кнопке "Конструктор"
    def test_move_to_constructor_with_constr_button(self, driver):
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
        driver.find_element(*LoginPage.EMAIL_STRING).send_keys(melog)
        driver.find_element(*LoginPage.PASS_STRING).send_keys(mepass)
        driver.find_element(*LoginPage.COMEIN_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(MainPage.ORDER_BUTTON))

        driver.find_element(*MainPage.LK_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(LkPage.SAVE_BUTTON))
    
        driver.find_element(*LkPage.CONSTR_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(MainPage.ORDER_BUTTON))
        assert 'Оформить заказ' == driver.find_element(*MainPage.ORDER_BUTTON).text

    #2 переход в конструктор из ЛК по кнопке с логотипом
    def test_move_to_constructor_with_burger_button(self, driver):
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
        driver.find_element(*LoginPage.EMAIL_STRING).send_keys(melog)
        driver.find_element(*LoginPage.PASS_STRING).send_keys(mepass)
        driver.find_element(*LoginPage.COMEIN_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(MainPage.ORDER_BUTTON))
        
        driver.find_element(*MainPage.LK_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(LkPage.SAVE_BUTTON))

        driver.find_element(*LkPage.BURGER_BUTTON).click()
        WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable(MainPage.ORDER_BUTTON))
        assert 'Оформить заказ' == driver.find_element(*MainPage.ORDER_BUTTON).text