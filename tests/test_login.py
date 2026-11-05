from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#1 вход по кнопке "Войти в аккаунт" на главной странице
def test_authorisation_with_button_voiti_v_akk_on_main_page(registration):
    new_user=registration
    driver=new_user["driver"]
    email=new_user["email"]
    password=new_user["password"]

    driver.find_element(By.XPATH, "//button[text()='Войти в аккаунт']").click()
    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Войти']")))

    driver.find_element(By.XPATH, "//input[@name='name']").send_keys(email)
    driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()
    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Оформить заказ']")))

#2 вход через кнопку "Личный кабинет" на главной странице
def test_authorisation_with_button_LK_on_main_page(registration):
    new_user=registration
    driver=new_user["driver"]
    email=new_user["email"]
    password=new_user["password"]

    driver.find_element(By.XPATH, ".//div[@id='root']/div/header/nav/a/p").click()
    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Войти']")))

    driver.find_element(By.XPATH, "//input[@name='name']").send_keys(email)
    driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()
    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Оформить заказ']")))

#3 вход через кнопку "Войти" в форме регистрации
def test_authorisation_with_button_voiti_on_registration_page(registration):
    new_user=registration
    driver=new_user["driver"]
    email=new_user["email"]
    password=new_user["password"]

    driver.find_element(By.XPATH, ".//div[@id='root']/div/header/nav/a/p").click()
    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[@href='/register']")))
    driver.find_element(By.XPATH, "//a[@href='/register']").click()
    WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//button[text()='Зарегистрироваться']")))

    driver.find_element(By.XPATH, "//a[@href='/login']").click()
    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Войти']")))

    driver.find_element(By.XPATH, "//input[@name='name']").send_keys(email)
    driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()
    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Оформить заказ']")))

#4 вход через кнопку "Войти" в форме восстановления пароля
def test_authorisation_with_button_voiti_on_forgotpass_page(registration):
    new_user=registration
    driver=new_user["driver"]
    email=new_user["email"]
    password=new_user["password"]

    driver.find_element(By.XPATH, ".//div[@id='root']/div/header/nav/a/p").click()
    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, "//a[@href='/forgot-password']")))
    driver.find_element(By.XPATH, "//a[@href='/forgot-password']").click()
    WebDriverWait(driver, 5).until(expected_conditions. element_to_be_clickable((By.XPATH, "//a[@href='/login']")))

    driver.find_element(By.XPATH, "//a[@href='/login']").click()
    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Войти']")))

    driver.find_element(By.XPATH, "//input[@name='name']").send_keys(email)
    driver.find_element(By.XPATH, "//input[@name='Пароль']").send_keys(password)
    driver.find_element(By.XPATH, "//button[text()='Войти']").click()
    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Оформить заказ']")))
