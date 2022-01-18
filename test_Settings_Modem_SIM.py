# переписал - Настройки СИМ Карты - переделал
import pytest


set_data_Settings_Modem_SIM = [
    None,
{'Settings': [{'id': 1, 'pin': '', 'addr': '', 'auth': False, 'login': '', 'password': '', 'enable': False}, {'id': 2, 'pin': '', 'addr': '', 'auth': False, 'login': '', 'password': '', 'enable': False}]}
]



# import conftest


# def test_SIM(UM40):
#     # from JSON_Backend_framework import USPD
#     #
#     # Machine_IP = '192.168.202.143'
#     # Login = 'admin'
#     # Password = 'admin'
#     # SMART40 = USPD.UM_40_Smart(ip_address=Machine_IP)
#
#     print('---------->', id(UM40))
#     result = UM40.Settings.Modem.SIM.read_settings()
#     print(result)

def test_SIM_read(UM40):
    """
    Тест на чтение данных

    :param UM40:
    :return:
    """

    print('\n-----ТЕСТЫ ID SMART ----->', id(UM40))

    # Получаем поле SIM
    SIM = UM40.Settings.Modem.SIM


    # Теперь спускаем его в тест на чтение
    from USPD.Settings.Read import Read

    Read_Settings = Read(USPD=SIM)

    result = Read_Settings.get_result()


@pytest.mark.parametrize("JSON_param", set_data_Settings_Modem_SIM)
def test_SIM_write(UM40, JSON_param):
    """
    Тест на запись данных
    :param UM40:
    :return:
    """

    print('\n-----ТЕСТЫ ID SMART ----->', id(UM40))

    # Здесь отправдляем наши данные
    result = UM40.Settings.Modem.SIM.write_settings(data=JSON_param)

    # Теперь смотрим - правильно ли записалось все это
    code = result.get('code')
    error_string_200 = 'Error code in not 200 OK '
    assert code == 200, error_string_200 + '\n' + str(result)
    # Теперь запрашиваем данные

    print(result)
    # settings = UM40.Settings.Modem.SIM.read_settings()
    # # проверяем
    # code = result.get('code')
    # assert settings == 200, error_string_200 + '\n' + str(settings)

    # далее смотримс что пришло


def test_SIM_rewrite(UM40):
    """
    Тест на перезапись данных
    :param UM40:
    :return:
    """
    print('\n-----ТЕСТЫ ID SMART ----->', id(UM40))
    result = UM40.Settings.Modem.SIM.read_settings()
    print(result)


def test_SIM_delete(UM40):
    """
    Тест на перезапись данных
    :param UM40:
    :return:
    """
    print('\n-----ТЕСТЫ ID SMART ----->', id(UM40))
    result = UM40.Settings.Modem.SIM.read_settings()
    print(result)
