from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

#1 переход в конструкторе к соусам
def test_konstruktor_skroll_to_sous():
    driver = webdriver.Chrome()
    try:
        driver.get("https://qa-stellarburgers.education-services.ru/")
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Соусы')]")))

        driver.find_element(By.XPATH, "//span[contains(text(), 'Соусы')]").click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt='Соус традиционный галактический']")))
        assert driver.find_element(By.XPATH, "//img[@alt='Соус традиционный галактический']").is_displayed()
    finally: 
            driver.quit()

#2 переход в конструкторе к начинкам
def test_konstruktor_skroll_to_insides():
    driver = webdriver.Chrome()
    try:
        driver.get("https://qa-stellarburgers.education-services.ru/")
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Начинки')]")))

        driver.find_element(By.XPATH, "//span[contains(text(), 'Начинки')]").click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt='Хрустящие минеральные кольца']")))
        assert driver.find_element(By.XPATH, "//img[@alt='Хрустящие минеральные кольца']").is_displayed()
    finally: 
            driver.quit()

#3 переход в конструкторе к булкам
def test_konstruktor_skroll_to_bread():
    driver = webdriver.Chrome()
    try:
        driver.get("https://qa-stellarburgers.education-services.ru/")
        WebDriverWait(driver, 10).until(expected_conditions.element_to_be_clickable((By.XPATH, "//span[contains(text(), 'Соусы')]")))

        driver.find_element(By.XPATH, "//span[contains(text(), 'Соусы')]").click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt='Соус традиционный галактический']")))
        driver.find_element(By.XPATH, "//span[contains(text(), 'Булки')]").click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, "//img[@alt='Краторная булка N-200i']")))
        assert driver.find_element(By.XPATH, "//img[@alt='Краторная булка N-200i']").is_displayed()
    finally: 
            driver.quit()
