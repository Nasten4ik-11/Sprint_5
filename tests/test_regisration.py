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
        self.wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(RegistrationPageLocators.NO_ACCOUNT_BUTTON)).click()

        email = f"test_{uuid.uuid4().hex[:6]}@example.com"
        self.driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys("User")
        self.driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys(email)
        self.driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys("123456")
        self.driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_FIELD).send_keys("123456")

        self.driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        button = self.wait.until(EC.visibility_of_element_located(MainPageLocators.CREATE_AD_BUTTON))
        self.assertTrue(button.is_displayed(), "Регистрация не удалась - кнопка 'Разместить объявление' не найдена")

    def test_invalid_email(self):
        """Проверка некорректного email"""
        self.wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(RegistrationPageLocators.NO_ACCOUNT_BUTTON)).click()

        self.driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys("invalid-email")
        self.driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        error = self.wait.until(EC.visibility_of_element_located(RegistrationPageLocators.ERROR_MESSAGE))
        self.assertTrue(error.is_displayed())

    def test_existing_user(self):
        """Проверка существующего пользователя"""
        self.wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)).click()
        self.wait.until(EC.element_to_be_clickable(RegistrationPageLocators.NO_ACCOUNT_BUTTON)).click()

        self.driver.find_element(*RegistrationPageLocators.NAME_FIELD).send_keys("User")
        self.driver.find_element(*RegistrationPageLocators.EMAIL_FIELD).send_keys("existing@example.com")
        self.driver.find_element(*RegistrationPageLocators.PASSWORD_FIELD).send_keys("123456")
        self.driver.find_element(*RegistrationPageLocators.CONFIRM_PASSWORD_FIELD).send_keys("123456")

        self.driver.find_element(*RegistrationPageLocators.CREATE_ACCOUNT_BUTTON).click()

        error = self.wait.until(EC.visibility_of_element_located(RegistrationPageLocators.ERROR_MESSAGE))
        self.assertTrue(error.is_displayed())

if __name__ == "__main__":
    unittest.main()