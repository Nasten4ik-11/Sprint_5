import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import uuid
from locators import LoginPageLocators, RegistrationPageLocators, MainPageLocators

class RegistrationTests(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 10)
        self.driver.get("https://qa-desk.stand.praktikum-services.ru/")

    def tearDown(self):
        self.driver.quit()

    def test_successful_registration(self):
        """Проверка успешной регистрации"""
        self.wait.until(EC.element_to_be_clickable(LoginPageLocators.КНОПКА_ВХОД)).click()
        self.wait.until(EC.element_to_be_clickable(RegistrationPageLocators.КНОПКА_НЕТ_АККАУНТА)).click()

        email = f"test_{uuid.uuid4().hex[:6]}@example.com"
        self.driver.find_element(*RegistrationPageLocators.ПОЛЕ_ИМЯ).send_keys("User")
        self.driver.find_element(*RegistrationPageLocators.ПОЛЕ_EMAIL).send_keys(email)
        self.driver.find_element(*RegistrationPageLocators.ПОЛЕ_ПАРОЛЬ).send_keys("123456")
        self.driver.find_element(*RegistrationPageLocators.ПОЛЕ_ПОДТВЕРЖДЕНИЕ_ПАРОЛЯ).send_keys("123456")

        self.driver.find_element(*RegistrationPageLocators.КНОПКА_СОЗДАТЬ_АККАУНТ).click()

        # Проверяем успешность регистрации по появлению кнопки размещения объявления
        self.wait.until(EC.visibility_of_element_located(MainPageLocators.КНОПКА_РАЗМЕСТИТЬ_ОБЪЯВЛЕНИЕ),
                       "Регистрация не удалась - кнопка 'Разместить объявление' не найдена")

    def test_invalid_email(self):
        """Проверка некорректного email"""
        self.wait.until(EC.element_to_be_clickable(LoginPageLocators.КНОПКА_ВХОД)).click()
        self.wait.until(EC.element_to_be_clickable(RegistrationPageLocators.КНОПКА_НЕТ_АККАУНТА)).click()

        self.driver.find_element(*RegistrationPageLocators.ПОЛЕ_EMAIL).send_keys("invalid-email")
        self.driver.find_element(*RegistrationPageLocators.КНОПКА_СОЗДАТЬ_АККАУНТ).click()

        error = self.wait.until(EC.visibility_of_element_located(RegistrationPageLocators.СООБЩЕНИЕ_ОШИБКИ),
                              "Сообщение об ошибке не отображается")
        self.assertTrue(error.is_displayed())

    def test_existing_user(self):
        """Проверка существующего пользователя"""
        self.wait.until(EC.element_to_be_clickable(LoginPageLocators.КНОПКА_ВХОД)).click()
        self.wait.until(EC.element_to_be_clickable(RegistrationPageLocators.КНОПКА_НЕТ_АККАУНТА)).click()

        self.driver.find_element(*RegistrationPageLocators.ПОЛЕ_ИМЯ).send_keys("User")
        self.driver.find_element(*RegistrationPageLocators.ПОЛЕ_EMAIL).send_keys("existing@example.com")
        self.driver.find_element(*RegistrationPageLocators.ПОЛЕ_ПАРОЛЬ).send_keys("123456")
        self.driver.find_element(*RegistrationPageLocators.ПОЛЕ_ПОДТВЕРЖДЕНИЕ_ПАРОЛЯ).send_keys("123456")

        self.driver.find_element(*RegistrationPageLocators.КНОПКА_СОЗДАТЬ_АККАУНТ).click()

        error = self.wait.until(EC.visibility_of_element_located(RegistrationPageLocators.СООБЩЕНИЕ_ОШИБКИ),
                              "Сообщение об ошибке не отображается")
        self.assertTrue(error.is_displayed())

if __name__ == "__main__":
    unittest.main()