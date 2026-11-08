from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from url import BURGER_URL
from locators.constr_page import ConstrPage

class TestConstructor:
    #1 переход в конструкторе к соусам
    def test_konstruktor_skroll_to_sous(self, driver):
        driver.get(BURGER_URL)
        WebDriverWait(driver, 5).until(expected_conditions.element_to_be_clickable(ConstrPage.SOUS))
          
        driver.find_element(*ConstrPage.SOUS).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(ConstrPage.SOUS_ACTIVE))
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(ConstrPage.SOUSE_TITLE))
        assert 'Соусы' in driver.find_element(*ConstrPage.SOUSE_TITLE).text

    #2 переход в конструкторе к начинкам
    def test_konstruktor_skroll_to_insides(self, driver):
        driver.get(BURGER_URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(ConstrPage.INSIDE))
       
        driver.find_element(*ConstrPage.INSIDE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(ConstrPage.INSIDE_ACTIVE))
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(ConstrPage.INSIDE_TITLE))
        assert 'Начинки' in driver.find_element(*ConstrPage.INSIDE_TITLE).text

    #3 переход в конструкторе к булкам
    def test_konstruktor_skroll_to_bread(self, driver):
        driver.get(BURGER_URL)
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(ConstrPage.INSIDE))
        driver.find_element(*ConstrPage.INSIDE).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(ConstrPage.INSIDE_ACTIVE))

        driver.find_element(*ConstrPage.BREAD).click()
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(ConstrPage.BREAD_ACTIVE))
        WebDriverWait(driver, 5).until(expected_conditions.visibility_of_element_located(ConstrPage.BREAD_TITLE))
        assert 'Булки' in driver.find_element(*ConstrPage.BREAD_TITLE).text