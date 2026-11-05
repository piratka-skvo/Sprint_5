from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#1 переход в конструктор из ЛК по кнопке "Конструктор"
def test_move_to_constructor_with_constr_button(registration):
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

    driver.find_element(By.XPATH, ".//div[@id='root']/div/header/nav/a/p").click()
    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']")))

    driver.find_element(By.XPATH, "//p[text()='Конструктор']").click()
    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Оформить заказ']")))

#2 переход в конструктор из ЛК по кнопке с логотипом
def test_move_to_constructor_with_burger_button(registration):
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

    driver.find_element(By.XPATH, ".//div[@id='root']/div/header/nav/a/p").click()
    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Сохранить']")))

    driver.find_element(By.CSS_SELECTOR, "header svg").click()
    WebDriverWait(driver, 15).until(expected_conditions.element_to_be_clickable((By.XPATH, "//button[text()='Оформить заказ']")))
