from locators import *
from settings import *

def test_pass_recovery_page(browser):
    browser.find_element(*AutoPageLoc.LOCATOR_FORGOT_PASSWORD).click()

    assert browser.find_element(*PassRecLoc.LOCATOR_PassRec_FIELD).text == 'Восстановление пароля'
    print("\nПереход на страницу восстановления прошел - Успешно ")
    print("\nТест - Пройден")

def test_recovery_by_phone(browser_PasRec_page):
    browser_PasRec_page.find_element(*PassRecLoc.LOCATOR_PHONE_FIELD).send_keys(valid_phone)
    browser_PasRec_page.find_element(*PassRecLoc.LOCATOR_BUTTON_CONTINUE).click()

    assert browser_PasRec_page.find_element(*PassRecLoc.LOCATOR_CODE_FIELD).text == 'Восстановление пароля'
    print("\nКод подтверждения отправлен на номер мобильного телефона")
    print("\nТест - Пройден")

def test_recovery_by_mail(browser_PasRec_page):
    browser_PasRec_page.find_element(*PassRecLoc.LOCATOR_MAIL_FIELD).click()
    browser_PasRec_page.find_element(*PassRecLoc.LOCATOR_MAIL_FIELD).send_keys(valid_email)
    browser_PasRec_page.find_element(*PassRecLoc.LOCATOR_BUTTON_CONTINUE).click()

    assert browser.find_element(*PassRecLoc.LOCATOR_CODE_FIELD).text == 'Восстановление пароля'
    print("\n Код подтверждения отправлен на адрес электронной почты")
    print("\nТест - Пройден")
