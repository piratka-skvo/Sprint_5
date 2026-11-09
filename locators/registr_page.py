from selenium.webdriver.common.by import By

class RegistrPage:
    REGISTR_TITLE=(By.XPATH,"//div[contains(@class, 'Auth_login__3hAey')][.//h2[contains(text(), 'Регистрация')]]") #надпись "Регистрация" на странице входа в лк над формой регистрации.
    NAME_STRING=(By.XPATH, "//fieldset[.//label[contains(text(), 'Имя')]]//input") #поле "Имя" в форме регистрации.
    EMAIL_STRING=(By.XPATH, "//fieldset[.//label[contains(text(), 'Email')]]//input") #поле "Email" в форме регистрации.
    PASS_STRING=(By.XPATH, "//fieldset[.//label[contains(text(), 'Пароль')]]//input") #поле "Пароль" в форме регистрации.
    REGISTR_BUTTON=(By.XPATH, "//button[text()='Зарегистрироваться']") #кнопка "Зарегистрироваться" под формой регистрации.
    ERROR_PASS=(By.CLASS_NAME, "input__error") #надпись об ошибке под строкой с паролем в форме регистрации.
    COME_IN_BUTTON=(By.XPATH, ".//a[@href='/login']") #кнопка "Войти" под формой регистрации.
