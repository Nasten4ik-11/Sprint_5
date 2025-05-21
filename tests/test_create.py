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

        post_ad_button = wait.until(EC.element_to_be_clickable(MainPageLocators.КНОПКА_РАЗМЕСТИТЬ_ОБЪЯВЛЕНИЕ))
        post_ad_button.click()

        modal_title = wait.until(EC.visibility_of_element_located(MainPageLocators.ЗАГОЛОВОК_МОДАЛКИ_АВТОРИЗАЦИИ))
        self.assertEqual(modal_title.text.strip(), "Чтобы разместить объявление, авторизуйтесь")

    def test_create_listing_authorized_user(self):
        driver = self.driver
        wait = self.wait

        # Авторизация
        driver.get("https://qa-desk.stand.praktikum-services.ru/login")
        email_input = wait.until(EC.visibility_of_element_located(LoginPageLocators.ПОЛЕ_EMAIL))
        email_input.send_keys("besit@example.com")
        driver.find_element(*LoginPageLocators.ПОЛЕ_ПАРОЛЬ).send_keys("123456besit")
        driver.find_element(*LoginPageLocators.КНОПКА_ВОЙТИ).click()
        wait.until(EC.url_to_be("https://qa-desk.stand.praktikum-services.ru/login"))
        time.sleep(2)

        # Создание объявления
        ad_title = f"Тестовый товар {int(time.time())}"
        print(f"Создаем объявление с названием: {ad_title}")

        driver.get("https://qa-desk.stand.praktikum-services.ru/create-lisiting")
        wait.until(EC.presence_of_element_located(CreateAdPageLocators.ПОЛЕ_НАЗВАНИЕ))
        driver.find_element(*CreateAdPageLocators.ПОЛЕ_НАЗВАНИЕ).send_keys(ad_title)
        driver.find_element(*CreateAdPageLocators.ПОЛЕ_ОПИСАНИЕ).send_keys("Описание тестового товара")
        driver.find_element(*CreateAdPageLocators.ПОЛЕ_ЦЕНА).send_keys("999")

        # Выбор категории
        category_dropdown_button = driver.find_element(*CreateAdPageLocators.ВЫПАДАЮЩИЙ_КАТЕГОРИИ)
        category_dropdown_button.click()
        wait.until(EC.visibility_of_element_located(CreateAdPageLocators.ОПЦИЯ_КАТЕГОРИИ)).click()

        # Выбор города
        city_dropdown_button = driver.find_element(*CreateAdPageLocators.ВЫПАДАЮЩИЙ_ГОРОДА)
        city_dropdown_button.click()
        wait.until(EC.visibility_of_element_located(CreateAdPageLocators.ОПЦИЯ_ГОРОДА)).click()

        # Выбор состояния товара
        used_condition_radio = wait.until(EC.element_to_be_clickable(CreateAdPageLocators.РАДИО_Б_У))
        used_condition_radio.click()

        publish_button = wait.until(EC.element_to_be_clickable(CreateAdPageLocators.КНОПКА_ОПУБЛИКОВАТЬ))
        publish_button.click()

        # Переход в профиль
        driver.get("https://qa-desk.stand.praktikum-services.ru/profile")
        time.sleep(3)

        # Поиск объявления
        found = False
        for page in range(1, 11):
            print(f"\nПроверяем страницу {page}")
            cards = driver.find_elements(*ProfilePageLocators.КАРТОЧКА_ОБЪЯВЛЕНИЯ)
            for card in cards:
                try:
                    if card.find_element(*ProfilePageLocators.ЗАГОЛОВОК_ОБЪЯВЛЕНИЯ).text == ad_title:
                        print("Объявление найдено!")
                        found = True
                        break
                except:
                    continue
            if found:
                break

            try:
                next_btn = driver.find_element(*ProfilePageLocators.КНОПКА_СЛЕДУЮЩАЯ_СТРАНИЦА)
                driver.execute_script("arguments[0].scrollIntoView();", next_btn)
                next_btn.click()
                time.sleep(2)
            except:
                print("Нет кнопки 'вперёд' или она неактивна.")
                break

        self.assertTrue(found, f"Объявление '{ad_title}' не найдено после 10 страниц")

if __name__ == "__main__":
    unittest.main()