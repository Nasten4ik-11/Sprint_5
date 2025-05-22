# locators.py
from selenium.webdriver.common.by import By

class LoginPageLocators:
    """Login page locators"""
    LOGIN_BUTTON = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    SUBMIT_BUTTON = (By.XPATH, "//button[contains(text(), 'Войти')]")
    USERNAME = (By.CSS_SELECTOR, "h3.profileText.name")
    AVATAR = (By.CLASS_NAME, "avatarSmall")

class RegistrationPageLocators:
    """Registration page locators"""
    NO_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(., 'Нет аккаунта')]")
    NAME_FIELD = (By.NAME, "name")
    EMAIL_FIELD = (By.NAME, "email")
    PASSWORD_FIELD = (By.NAME, "password")
    CONFIRM_PASSWORD_FIELD = (By.NAME, "submitPassword")
    CREATE_ACCOUNT_BUTTON = (By.XPATH, "//button[contains(., 'Создать аккаунт')]")
    ERROR_MESSAGE = (By.XPATH, "//span[contains(., 'Ошибка')]")

class MainPageLocators:
    """Main page locators"""
    CREATE_AD_BUTTON = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")
    AUTH_MODAL_TITLE = (By.XPATH, "//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]")

class CreateAdPageLocators:
    """Create ad page locators"""
    TITLE_FIELD = (By.NAME, "name")
    DESCRIPTION_FIELD = (By.CSS_SELECTOR, "textarea[name='description']")
    PRICE_FIELD = (By.CSS_SELECTOR, "input[name='price']")
    CATEGORY_DROPDOWN = (By.XPATH, "//input[@name='category']/following-sibling::button")
    CATEGORY_OPTION = (By.XPATH, "//span[contains(text(), 'Книги')]")
    CITY_DROPDOWN = (By.XPATH, "//input[@name='city']/following-sibling::button")
    CITY_OPTION = (By.XPATH, "//span[contains(text(), 'Казань')]")
    USED_CONDITION_RADIO = (By.XPATH, "//label[text()='Б/У']")
    PUBLISH_BUTTON = (By.XPATH, "//button[contains(@class, 'buttonPrimary') and contains(text(), 'Опубликовать')]")

class ProfilePageLocators:
    """Profile page locators"""
    AD_CARD = (By.CSS_SELECTOR, "div.card")
    AD_TITLE = (By.CSS_SELECTOR, "h2.h2")
    NEXT_PAGE_BUTTON = (By.CSS_SELECTOR, "button.arrowButton--right:not([disabled])")

class LogoutLocators:
    """Logout locators"""
    LOGOUT_BUTTON = (By.XPATH, "//button[contains(text(), 'Выйти')]")