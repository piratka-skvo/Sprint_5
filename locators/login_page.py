from selenium.webdriver.common.by import By

class LoginPage:
    LK_BUTTON=(By.XPATH, ".//div[@id='root']/div/header/nav/a/p") #кнопка "Личный кабинет" на странице входа.
    REGISTR_BUTTON=(By.XPATH, ".//a[@href='/register']") #кнопка "Зарегистрироваться" на странице входа в лк под формой входа.
    COMEIN_TITLE=(By.XPATH, ".//h2") #надпись "Вход" на странице входа над формой.
    COMEIN_BUTTON=(By.XPATH, "//button[text()='Войти']") #кнопка "Войти" под формой входа.
    EMAIL_STRING=(By.XPATH, "//input[@name='name']") #строка ввода email.
    PASS_STRING=(By.XPATH, "//input[@name='Пароль']") #строка ввода пароля.
    FORGOT_BUTTON=(By.XPATH, ".//a[@href='/forgot-password']") #кнопка "Восстановить пароль" под формой входа.