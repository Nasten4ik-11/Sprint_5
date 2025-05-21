from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
import time
from locators import LoginPageLocators, CreateAdPageLocators, ProfilePageLocators, MainPageLocators

class CreateListingTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_create_listing_unauthorized_user(self):
        driver = self.driver
        wait = self.wait
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        post_ad_button = wait.until(EC.element_to_be_clickable(MainPageLocators.CREATE_AD_BUTTON))
        post_ad_button.click()

        modal_title = wait.until(EC.visibility_of_element_located(MainPageLocators.AUTH_MODAL_TITLE))
        self.assertEqual(modal_title.text.strip(), "Чтобы разместить объявление, авторизуйтесь")

    def test_create_listing_authorized_user(self):
        driver = self.driver
        wait = self.wait

        # Авторизация
        driver.get("https://qa-desk.stand.praktikum-services.ru/login")
        wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD)).send_keys("besit@example.com")
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys("123456besit")
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

        wait.until(EC.visibility_of_element_located(LoginPageLocators.AVATAR))

        # Создание объявления
        ad_title = f"Тестовый товар {int(time.time())}"
        driver.get("https://qa-desk.stand.praktikum-services.ru/create-lisiting")

        wait.until(EC.presence_of_element_located(CreateAdPageLocators.TITLE_FIELD)).send_keys(ad_title)
        driver.find_element(*CreateAdPageLocators.DESCRIPTION_FIELD).send_keys("Описание тестового товара")
        driver.find_element(*CreateAdPageLocators.PRICE_FIELD).send_keys("999")

        # Выбор категории
        driver.find_element(*CreateAdPageLocators.CATEGORY_DROPDOWN).click()
        wait.until(EC.element_to_be_clickable(CreateAdPageLocators.CATEGORY_OPTION)).click()

        # Выбор города
        driver.find_element(*CreateAdPageLocators.CITY_DROPDOWN).click()
        wait.until(EC.element_to_be_clickable(CreateAdPageLocators.CITY_OPTION)).click()

        # Выбор состояния
        wait.until(EC.element_to_be_clickable(CreateAdPageLocators.USED_CONDITION_RADIO)).click()

        # Публикация
        wait.until(EC.element_to_be_clickable(CreateAdPageLocators.PUBLISH_BUTTON)).click()

        # Переход в профиль
        driver.get("https://qa-desk.stand.praktikum-services.ru/profile")

        while True:
            try:
                next_btn = wait.until(EC.element_to_be_clickable(ProfilePageLocators.NEXT_PAGE_BUTTON))
                driver.execute_script("arguments[0].scrollIntoView();", next_btn)
                next_btn.click()
            except:
                break  

        # Проверка наличия нового объявления
        wait.until(EC.presence_of_element_located(ProfilePageLocators.AD_CARD))
        ad_titles = driver.find_elements(*ProfilePageLocators.AD_TITLE)
        titles = [title.text.strip() for title in ad_titles]

        self.assertIn(ad_title, titles, f"Объявление '{ad_title}' не найдено в профиле")

if __name__ == "__main__":
    unittest.main()