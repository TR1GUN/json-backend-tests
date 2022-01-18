# переписал - Настройки линий питания интерфейсов - переделал
import pytest

def test_DOut_read(UM40):
    """
    Тест на чтение данных

    :param UM40:
    :return:
    """

    print('\n-----ТЕСТЫ ID SMART ----->', id(UM40))

    # Получаем поле SIM
    Interface_DOut = UM40.Settings.DeviceSettings.Interface_DOut


    # Теперь спускаем его в тест на чтение
    from USPD.Settings.Read import Read

    Read_Settings = Read(USPD=Interface_DOut)

    result = Read_Settings.get_result()