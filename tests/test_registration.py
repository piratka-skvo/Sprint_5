import random

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

driver = webdriver.Chrome()
driver.get("https://qa-stellarburgers.education-services.ru/")

driver.find_element(By.CLASS_NAME, "AppHeader_header__link__3D_hX").click()
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.XPATH, ".//div [@id='root']/div/header/nav/a/p")))

driver.find_element(By.XPATH, ".//div[@id='root']/div/header/nav/a/p").click()
WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Зарегистрироваться")))

driver.find_element(By.XPATH, ".//a[@href='/register']").click()
WebDriverWait(driver, 10).until(expected_conditions.visibility_of_element_located((By.XPATH, "//*[@id='root']/div/main/div/h2")))
driver.find_element(By.XPATH, ".//fieldset[1]/div/div/input").send_keys("MElvira")
melog=f"Elvira_Magsumova_57_{random.randint(100, 999)}@yandex.ru"
mepass={random.randint(100000, 999999)}
driver.find_element(By.XPATH, ".//fieldset[2]/div/div/input").send_keys(melog)
driver.find_element(By.XPATH, ".//fieldset[3]/div/div/input").send_keys(str(mepass))
driver.find_element(By.XPATH, "//*[@id='root']/div/main/div/form/button").click()

WebDriverWait(driver, 3).until(expected_conditions.visibility_of_element_located((By.LINK_TEXT, "Вход")))

driver.quit()
