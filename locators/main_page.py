from selenium.webdriver.common.by import By

class MainPage:
    LK_BUTTON=(By.XPATH, ".//div[@id='root']/div/header/nav/a/p") #кнопка "Личный кабинет" на главной странице.
    COME_IN_ACC_BUTTON=(By.XPATH, "//button[text()='Войти в аккаунт']") #кнопка "Войти в аккаунт" на гл. странице.
    ORDER_BUTTON=(By.XPATH, "//button[text()='Оформить заказ']") #кнопка "Оформить заказ" на гл. странице для авторизованного пользователя.