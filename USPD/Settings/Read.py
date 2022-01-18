# ------------------------------------------------------------------------------------------------------------------
#                            Простой тестовый класс который выполняет ТЕСТ на чтение Элемента - Это важно
# ------------------------------------------------------------------------------------------------------------------
class Read:
    # ТЭГ в котором лежат какие то данные
    """
    Стандартный тест на чтение для настроек , где есть поле Settings - запрос GET
    """

    Data_TAG = 'Settings'
    Result = None

    # ТЕКСТ ОШИБКИ если мы получили не тот ответ что ожидали :
    # Если результат не 200 ок
    error_string_200 = 'Error code in not 200 OK '
    # ЕСли Поле data не словарь - ЭТО ВАЖНО
    error_string_data_is_not_dict = 'Field data is not dict '
    # Поле дата пустое
    error_string_data = 'Field data is void '
    # Поля с искомым нашим дата тагом не существует
    error_string_data_tag = 'Field ' + Data_TAG + ' is void '

    def __init__(self, USPD):
        """
        Тестовый класс для того чтоб выполнить тест на чтение

        :param USPD: Класс УСПД который должен прочитаться
        """
        self.Result = None
        self.Result = self._Read(USPD=USPD)

    def _Read(self, USPD):
        """
        Метод для чтения , Вызывает метод read_settings для экземпляра класса
        :param USPD:
        :return:
        """
        result = USPD.read_settings()

        # Теперь проверяем что у нас все корректно пришло
        code = result.get('code')

        # Проверка на то что код состояния нормальный
        assert code == 200, self.error_string_200 + '\n' + str(result)
        # Теперь проверим на коректность возвращаемого ответа
        data = result.get('data')
        # Проверка на то что Поле дата есть
        assert data is not None, self.error_string_data + '\n' + str(result)

        # И теперь смотрим ЧТО ЕСТЬ поле Settings и оно не None
        # Тут Необходимо быть аккуратнее - Так как поле data может быть не JSON ,
        # поэтому проверяем что у нас словарь, а не строка
        assert type(data) is dict, self.error_string_data_is_not_dict + '\n' + str(result)

        # Если успешно - вытаскиваем наш дата таг
        Settings = data.get(self.Data_TAG)
        # Проверка на то что Поле с дата тагом существует
        assert Settings is not None, self.error_string_data_tag + '\n' + str(result)

        # возвращаем нашу переменную
        return data

    def get_result(self):
        """
        Возвращаем наше поле data из ответа
        :return:
        """
        return self.Result
