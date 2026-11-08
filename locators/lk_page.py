from selenium.webdriver.common.by import By

class LkPage:
    SAVE_BUTTON=(By.XPATH, "//button[text()='Сохранить']") #кнопка "Сохранить" на этой странице.
    CONSTR_BUTTON=(By.XPATH, "//p[text()='Конструктор']") #кнопка "Конструктор".
    BURGER_BUTTON=(By.CSS_SELECTOR, "header svg") #кнопка перехода на гл. страницу с логотипом.
    LOG_OUT_BUTTON=(By.XPATH, "//button[text()='Выход']") #кнопка "Выход".