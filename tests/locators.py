# locators.py
from selenium.webdriver.common.by import By

class LoginPageLocators:
    """Локаторы для страницы входа"""
    КНОПКА_ВХОД = (By.XPATH, "//button[contains(text(), 'Вход и регистрация')]")
    ПОЛЕ_EMAIL = (By.NAME, "email")
    ПОЛЕ_ПАРОЛЬ = (By.NAME, "password")
    КНОПКА_ВОЙТИ = (By.XPATH, "//button[contains(text(), 'Войти')]")
    ИМЯ_ПОЛЬЗОВАТЕЛЯ = (By.CSS_SELECTOR, "h3.profileText.name")
    АВАТАР = (By.CLASS_NAME, "avatarSmall")

class RegistrationPageLocators:
    """Локаторы для страницы регистрации"""
    КНОПКА_НЕТ_АККАУНТА = (By.XPATH, "//button[contains(., 'Нет аккаунта')]")
    ПОЛЕ_ИМЯ = (By.NAME, "name")
    ПОЛЕ_EMAIL = (By.NAME, "email")
    ПОЛЕ_ПАРОЛЬ = (By.NAME, "password")
    ПОЛЕ_ПОДТВЕРЖДЕНИЕ_ПАРОЛЯ = (By.NAME, "submitPassword")
    КНОПКА_СОЗДАТЬ_АККАУНТ = (By.XPATH, "//button[contains(., 'Создать аккаунт')]")
    СООБЩЕНИЕ_ОШИБКИ = (By.XPATH, "//span[contains(., 'Ошибка')]")

class MainPageLocators:
    """Локаторы главной страницы"""
    КНОПКА_РАЗМЕСТИТЬ_ОБЪЯВЛЕНИЕ = (By.XPATH, "//button[contains(text(), 'Разместить объявление')]")
    ЗАГОЛОВОК_МОДАЛКИ_АВТОРИЗАЦИИ = (By.XPATH, "//h1[contains(text(), 'Чтобы разместить объявление, авторизуйтесь')]")

class CreateAdPageLocators:
    """Локаторы для страницы создания объявления"""
    ПОЛЕ_НАЗВАНИЕ = (By.NAME, "name")
    ПОЛЕ_ОПИСАНИЕ = (By.CSS_SELECTOR, "textarea[name='description']")
    ПОЛЕ_ЦЕНА = (By.CSS_SELECTOR, "input[name='price']")
    ВЫПАДАЮЩИЙ_КАТЕГОРИИ = (By.XPATH, "//input[@name='category']/following-sibling::button")
    ОПЦИЯ_КАТЕГОРИИ = (By.XPATH, "//span[contains(text(), 'Книги')]")
    ВЫПАДАЮЩИЙ_ГОРОДА = (By.XPATH, "//input[@name='city']/following-sibling::button")
    ОПЦИЯ_ГОРОДА = (By.XPATH, "//span[contains(text(), 'Казань')]")
    РАДИО_Б_У = (By.XPATH, "//label[text()='Б/У']")
    КНОПКА_ОПУБЛИКОВАТЬ = (By.XPATH, "//button[contains(@class, 'buttonPrimary') and contains(text(), 'Опубликовать')]")

class ProfilePageLocators:
    """Локаторы для страницы профиля"""
    КАРТОЧКА_ОБЪЯВЛЕНИЯ = (By.CSS_SELECTOR, "div.card")
    ЗАГОЛОВОК_ОБЪЯВЛЕНИЯ = (By.CSS_SELECTOR, "h2.h2")
    КНОПКА_СЛЕДУЮЩАЯ_СТРАНИЦА = (By.CSS_SELECTOR, "button.arrowButton--right:not([disabled])")

class LogoutLocators:
    """Локаторы для выхода из системы"""
    КНОПКА_ВЫЙТИ = (By.XPATH, "//button[contains(text(), 'Выйти')]")