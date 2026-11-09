from selenium.webdriver.common.by import By

class ConstrPage:
    SOUS=(By.XPATH, "//span[contains(text(), 'Соусы')]") #кнопка "Соусы".
    SOUS_ACTIVE=(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')][.//span[contains(text(), 'Соусы')]]") #активная вкладка Соус.
    SOUSE_TITLE=(By.XPATH, "//h2[contains(text(), 'Соусы')]") #заголовок "Соусы".
    INSIDE=(By.XPATH, "//span[contains(text(), 'Начинки')]") #кнопка "Начинки".
    INSIDE_ACTIVE=(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')][.//span[contains(text(), 'Начинки')]]") #активная вкладка Начинки.
    INSIDE_TITLE=(By.XPATH, "//h2[contains(text(), 'Начинки')]") #заголовок "Начинки".
    BREAD=(By.XPATH, "//span[contains(text(), 'Булки')]") #кнопка "Булки".
    BREAD_ACTIVE=(By.XPATH, "//div[contains(@class, 'tab_tab_type_current')][.//span[contains(text(), 'Булки')]]") #активная вкладка Булки.
    BREAD_TITLE=(By.XPATH, "//h2[contains(text(), 'Булки')]") #заголовок "Булки".