import unittest
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import LoginPageLocators

class LoginTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_login_user(self):
        driver = self.driver
        wait = self.wait
        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        wait.until(EC.element_to_be_clickable(LoginPageLocators.КНОПКА_ВХОД)).click()
        wait.until(EC.visibility_of_element_located(LoginPageLocators.ПОЛЕ_EMAIL)).send_keys("besit@example.com")
        driver.find_element(*LoginPageLocators.ПОЛЕ_ПАРОЛЬ).send_keys("123456besit")
        driver.find_element(*LoginPageLocators.КНОПКА_ВОЙТИ).click()

        # Проверка авторизации
        user_name = wait.until(EC.visibility_of_element_located(LoginPageLocators.ИМЯ_ПОЛЬЗОВАТЕЛЯ)).text
        self.assertEqual(user_name, "User.")
        avatar = driver.find_element(*LoginPageLocators.АВАТАР)
        self.assertTrue(avatar.is_displayed())

if __name__ == "__main__":
    unittest.main()