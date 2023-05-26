from incorrect import Incorrect

import string

#Данные для авторизации
valid_firstname = 'Дмитрий'
valid_lastname = 'Смит'
valid_email = 'dmitrysmit@mail.ru'
valid_pass = 'raLtIm'
valid_phone = '+79523333333'
valid_login = 'Dmitry-Smit'
valid_ls = '530189975611'

from locators import AutoPageLoc

#Некорректные данные авторизации
#Данные на русском
wrong_ru = Incorrect('ru_RU')
wrong_firstname = wrong_ru.first_name()
wrong_lastname = wrong_ru.last_name()
wrong_phone = wrong_ru.phone_number()

#Данные на английском
wrong = Incorrect('en-US')
wrong_firstname_en = wrong.first_name()
wrong_lastname_en = wrong.last_name()
wrong_password = wrong.password()
wrong_email = wrong.email()
wrong_login = wrong.user_name()
invalid_ls = '411287902571'
region = 'Новосибирская область'
