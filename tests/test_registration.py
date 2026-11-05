import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#1 тест успешная регистрация с корректными данными
def test_registration_successful(registration):
    new_user=registration
    driver=new_user["driver"]
    email=new_user["email"]
    password=new_user["password"]

    driver.get("https://qa-stellarburgers.education-services.ru/")
    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Войти в аккаунт']")))
    driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Войти']")))

    driver.find_element(By.XPATH, "//input[@name='name']").send_keys(email)
    driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()
    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Оформить заказ']")))



#2 тест ошибки регистрации с некорректным паролем
def test_registration_error_password():
    driver = webdriver.Chrome()
    driver.get("https://qa-stellarburgers.education-services.ru/")

    driver.find_element(By.CLASS_NAME, "AppHeader_header__link__3D_hX").click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div[@id='root']/div/header/nav/a/p")))

    driver.find_element(By.XPATH, ".//div[@id='root']/div/header/nav/a/p").click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Зарегистрироваться")))

    driver.find_element(By.XPATH, ".//a[@href='/register']").click()
    WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/main/div/h2")))
    driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("MElvira")
    melog=f"Elvira_Magsumova_57_{random.randint(100, 999)}@yandex.ru"
    driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(melog)
    driver.find_element(By.XPATH, ".//fieldset[3]/div/div/input").send_keys("123")
    driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/button").click()

    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.CLASS_NAME, "input__error")))

    driver.quit()