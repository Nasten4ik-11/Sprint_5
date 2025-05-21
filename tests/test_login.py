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

        wait.until(EC.element_to_be_clickable(LoginPageLocators.LOGIN_BUTTON)).click()
        wait.until(EC.visibility_of_element_located(LoginPageLocators.EMAIL_FIELD)).send_keys("besit@example.com")
        driver.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys("123456besit")
        driver.find_element(*LoginPageLocators.SUBMIT_BUTTON).click()

        # Проверка авторизации
        user_name = wait.until(EC.visibility_of_element_located(LoginPageLocators.USERNAME)).text
        self.assertEqual(user_name, "User.")
        avatar = driver.find_element(*LoginPageLocators.AVATAR)
        self.assertTrue(avatar.is_displayed())

if __name__ == "__main__":
    unittest.main()