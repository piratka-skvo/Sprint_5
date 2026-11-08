from selenium.webdriver.common.by import By

class RegistrPage:
    REGISTR_TITLE=(By.XPATH, "//*[@id='root']/div/main/div/h2") #надпись "Регистрация" на странице входа в лк над формой регистрации.
    NAME_STRING=(By.XPATH, ".//fieldset[1]/div/div/input") #поле "Имя" в форме регистрации.
    EMAIL_STRING=(By.XPATH, ".//fieldset[2]/div/div/input") #поле "Email" в форме регистрации.
    PASS_STRING=(By.XPATH, ".//fieldset[3]/div/div/input") #поле "Пароль" в форме регистрации.
    REGISTR_BUTTON=(By.XPATH, "//button[text()='Зарегистрироваться']") #кнопка "Зарегистрироваться" под формой регистрации.
    ERROR_PASS=(By.CLASS_NAME, "input__error") #надпись об ошибке под строкой с паролем в форме регистрации.
    COME_IN_BUTTON=(By.XPATH, ".//a[@href='/login']") #кнопка "Войти" под формой регистрации.