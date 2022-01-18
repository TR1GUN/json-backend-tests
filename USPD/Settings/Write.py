# ------------------------------------------------------------------------------------------------------------------
#                            Простой тестовый класс который выполняет ТЕСТ на ЗаписьЭлемента - Это важно
# ------------------------------------------------------------------------------------------------------------------
class Write:
    # ТЭГ в котором лежат какие то данные
    """
    Стандартный тест на чтение для настроек , где есть поле Settings - запрос POST
    """

    Data_TAG = 'Settings'
    Result = None

    # ТЕКСТ ОШИБКИ если мы получили не тот ответ что ожидали :
    # Если результат не 200 ок
    error_string_200 = 'Error code in not 200 OK '
    # Ксли у нас что то не записалось
    error_string_not_write_data = 'Not write data :  '

    def __init__(self, USPD, JSON):
        """
                Тестовый класс для того чтоб выполнить тест на запись

        :param USPD: Класс УСПД который должен прочитаться
        :param JSON: JSON что отправляем на запись
        """
        self.Result = None
        # Отправляем на запись
        self.Result = self._Write(USPD=USPD, JSON=JSON)

        # ТЕПЕРЬ пойдет жаришка - считываем наши данные , что должны были записаться

        data = self._Read(USPD=USPD)
        # И теперь проверяем корректность того что мы записали
        self.Result = self._CheckUP(answer=data, data_to_write=JSON)

    def _Write(self, USPD, JSON):
        """
        Метод для записи , Вызывает метод write_settings для экземпляра класса
        :param USPD: Класс УСПД который должен прочитаться
        :param JSON: JSON что отправляем на запись
        :return:
        """
        result = USPD.write_settings(data=JSON)

        # Теперь проверяем что у нас все корректно пришло
        code = result.get('code')

        # Проверка на то что код состояния нормальный
        assert code == 200, self.error_string_200 + '\n' + str(result)

        return True

    def _Read(self, USPD):
        """
        Метод для чтения , Вызывает метод read_settings для экземпляра класса
        :param USPD:
        :return:
        """
        # Считываем данные
        from USPD.Settings.Read import Read

        ReadData = Read(USPD=USPD)

        data = ReadData.get_result()

        return data

    def _CheckUP(self, answer, data_to_write):
        """
        Здесь проверяем Что записали
        :param answer: Ответ от УСПД что есть
        :param data_to_write: Данные что отправляли на запись
        :return:
        """
        result = False
        # Пункт первый - Если data_to_write пустота , то и нечего проверять
        if data_to_write is None:
            result = False

        # Теперь получаем у обоих JSON поле Settings
        answer_settings = answer.get(self.Data_TAG)
        data_to_write_settings = data_to_write.get(self.Data_TAG)

        # Проверяем - точно ли все ок
        assert (answer_settings is not None) or (data_to_write_settings is not None)

        # ТЕПЕРЬ ПЕРЕБИРАЕМ ВСЕ элементы в data_to_write_settings и ищем их в том что запросили
        # ЕСЛИ не находим , то Добавляем в список
        not_write = []
        # Эта переменная необходима чтоб удалять те элементы что нашли - Защита от дублей
        To_delete_element = None

        for element_to_write in data_to_write_settings:
            # маркер того что нашли
            search = False
            for element_to_answer in answer_settings:
                # выкатываем все ключи в ответе
                keys_to_answer = list(element_to_answer.keys())

                # Составляем два списка
                answer_list = []
                to_write_list = []
                # пихаем их туда
                for key in keys_to_answer:
                    answer_list.append(element_to_answer.get(key))

                    to_write_list.append(element_to_write.get(key))

                # ТЕПЕРЬ очень важный момент - сравниваем эти два списка
                if answer_list == to_write_list:
                    # ставим что мы нашли
                    search = True

                    # Защита от дублей -
                    To_delete_element = element_to_answer
                    # И выходим
                    break

            # ЕСЛИ НИЧЕГО НЕ НАШЛИ , добавляем это в список
            if search is False:
                not_write.append(element_to_write)

            # ЕСЛИ нашли - Удаляем элемент что нашли
            if search is True:
                answer_settings.remove(To_delete_element)
                To_delete_element = None

        # В конце этой вакханалии мы проверяем что У НАС НИЧЕГО НЕ записалась в список не записанного

        assert len(not_write) == 0, self.error_string_not_write_data + '\n' + str(not_write)

        return True

    def get_result(self):
        """
        Возвращаем наше поле data из ответа
        :return:
        """
        return self.Result
