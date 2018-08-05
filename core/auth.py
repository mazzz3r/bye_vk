import configparser
from getpass import getpass

import vk_api


def auth_handler():
    """ При двухфакторной аутентификации вызывается эта функция.
    """

    # Код двухфакторной аутентификации
    key = input("Enter authentication code: ")
    # Если: True - сохранить, False - не сохранять.
    remember_device = True

    return key, remember_device


def get_session():
    config = configparser.ConfigParser()
    config.read('credentials.ini')
    section = config['DEFAULT']

    if 'Login' in section and 'Password' in section and \
            section['Login'] and section['Password']:
        login = section['Login']
        password = section['Password']
    else:
        login = input('Login: ')
        password = getpass()

    vk_session = vk_api.VkApi(
        login, password,
        auth_handler=auth_handler  # функция для обработки двухфакторной аутентификации
    )
    # vk_session = vk_api.VkApi(login, password)
    return vk_session
