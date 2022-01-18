# Здесь расположим наши фикстуры
import pytest


# Фикстура которая делает Элемент класса для взаимодействия с УМ 40 СМАРТ
# Делаем ее МОДУЛЬНОЙ чтоб мы брали один и тот же экземпляр класса

@pytest.fixture(scope="session")
def UM40():
    """
    Формируем фикстуру - класс конекта к УМ-40 СМАРТ
    :return:
    """
    from JSON_Backend_framework import USPD

    # Machine_IP = '192.168.202.143'
    # Login = 'admin'
    # Password = 'admin'

    # Наши параметры берем из конфига
    from Service.config import Machine_IP, Login, Password

    SMART40 = USPD.UM_40_Smart(ip_address=Machine_IP)

    print('\n----- ID SMART ----->', id(SMART40))

    return SMART40
