from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import unittest
from locators import LoginPageLocators, LogoutLocators

class LogoutTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.wait = WebDriverWait(self.driver, 20)

    def tearDown(self):
        self.driver.quit()

    def test_logout_user(self):
        driver = self.driver
        wait = self.wait

        driver.get("https://qa-desk.stand.praktikum-services.ru/")

        # Вход
        wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD)).send_keys("besit@example.com")
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys("123456besit")
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

        wait.until(EC.visibility_of_element_located(LoginPageLocators.AVATAR))

        # Выход
        wait.until(EC.element_to_be_clickable(LogoutLocators.LOGOUT_BUTTON)).click()

        wait.until(EC.invisibility_of_element_located(LoginPageLocators.USERNAME))

        avatar_elements = driver.find_elements(*LoginPageLocators.AVATAR)
        name_elements = driver.find_elements(*LoginPageLocators.USERNAME)

        self.assertEqual(len(avatar_elements), 0, "Аватар не должен отображаться после выхода")
        self.assertEqual(len(name_elements), 0, "Имя не должно отображаться после выхода")

        login_button = wait.until(EC.visibility_of_element_located(LoginPageLocators.LOGIN_BUTTON))
        self.assertTrue(login_button.is_displayed())

if __name__ == "__main__":
    unittest.main()