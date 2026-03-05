class AlarmClock:
    """
    Класс будильника.
    Хранит текущее время и установленное время срабатывания.
    Позволяет устанавливать время, будильник, проверять совпадение,
    откладывать будильник (snooze) и вести историю срабатываний.
    """

    def __init__(self, time_str: str, alarm_str: str = "OFF"):
        """
        Инициализация будильника.
        :param time_str: текущее время в формате ЧЧ:ММ (например, "08:30")
        :param alarm_str: время будильника в формате ЧЧ:ММ или "OFF" (по умолчанию выключен)
        """
        self._time_minutes = self._parse_time_str(time_str)  # внутреннее хранение времени в минутах
        self._alarm_minutes = None                           # минуты будильника или None, если выключен
        self._alarm_enabled = False
        self._snooze_count = 0                               # счётчик срабатываний будильника
        self._history = []                                    # история срабатываний

        if alarm_str != "OFF":
            self.set_alarm(alarm_str)                         # установка будильника через метод (включает проверку)

        print(f"Создан новый будильник: время = {self.time}, будильник = {self.alarm}")

    @staticmethod
    def _parse_time_str(time_str: str) -> int:
        """
        Преобразует строку времени в формате ЧЧ:ММ в количество минут от полуночи.
        Выполняет валидацию формата и диапазона.
        """
        if not isinstance(time_str, str):
            raise TypeError("Время должно быть строкой в формате ЧЧ:ММ")

        parts = time_str.split(':')
        if len(parts) != 2:
            raise ValueError("Неверный формат времени. Используйте ЧЧ:ММ")

        try:
            hours = int(parts[0])
            minutes = int(parts[1])
        except ValueError:
            raise ValueError("Часы и минуты должны быть целыми числами")

        if not (0 <= hours <= 23):
            raise ValueError("Часы должны быть в диапазоне 0-23")
        if not (0 <= minutes <= 59):
            raise ValueError("Минуты должны быть в диапазоне 0-59")

        return hours * 60 + minutes

    @staticmethod
    def _minutes_to_time_str(minutes: int) -> str:
        """Преобразует минуты от полуночи в строку формата ЧЧ:ММ с ведущими нулями."""
        hours = minutes // 60
        mins = minutes % 60
        return f"{hours:02d}:{mins:02d}"

    @property
    def time(self) -> str:
        """Текущее время в формате ЧЧ:ММ (свойство только для чтения)."""
        return self._minutes_to_time_str(self._time_minutes)

    @property
    def alarm(self) -> str:
        """
        Время будильника в формате ЧЧ:ММ или "OFF", если будильник выключен.
        Свойство только для чтения.
        """
        if not self._alarm_enabled:
            return "OFF"
        return self._minutes_to_time_str(self._alarm_minutes)

    def set_time(self, time_str: str) -> None:
        """Устанавливает новое текущее время."""
        self._time_minutes = self._parse_time_str(time_str)
        print(f"Установлено новое время: {self.time}")

    def set_alarm(self, alarm_str: str) -> None:
        """
        Устанавливает время будильника.
        Если передана строка "OFF", будильник выключается.
        """
        if alarm_str == "OFF":
            self._alarm_enabled = False
            self._alarm_minutes = None
            print("Будильник выключен")
        else:
            minutes = self._parse_time_str(alarm_str)
            self._alarm_minutes = minutes
            self._alarm_enabled = True
            print(f"Установлен будильник на {self.alarm}")

    def disable_alarm(self) -> None:
        """Отключает будильник (устанавливает в 'OFF')."""
        self.set_alarm("OFF")

    def check_alarm(self) -> bool:
        """
        Проверяет, совпадает ли текущее время с временем будильника.
        Если будильник включён и время совпадает:
          - увеличивает счётчик срабатываний,
          - добавляет запись в историю,
          - выводит сообщение и возвращает True.
        В противном случае возвращает False.
        """
        if not self._alarm_enabled:
            print("Будильник выключен, можно спать дальше")
            return False

        if self._time_minutes == self._alarm_minutes:
            self._snooze_count += 1
            self._history.append({
                'snooze_number': self._snooze_count,
                'alarm_time': self.alarm,
                'triggered_at': self.time
            })
            print("🛎️  Будильник! Пора вставать!")
            return True
        else:
            print("Можно спать дальше")
            return False

    def set_snooze(self, minutes_to_add: int) -> None:
        """
        Откладывает будильник на указанное количество минут.
        Если будильник выключен, выводит предупреждение и ничего не делает.
        """
        if not self._alarm_enabled:
            print("Будильник выключен, невозможно отложить")
            return

        if not isinstance(minutes_to_add, int) or minutes_to_add <= 0:
            raise ValueError("Количество минут для откладывания должно быть положительным целым числом")

        new_minutes = self._alarm_minutes + minutes_to_add
        # Циклический переход через полночь
        new_minutes %= 24 * 60  # 1440 минут в сутках

        self._alarm_minutes = new_minutes
        print(f"Будильник отложен на {minutes_to_add} мин. Новое время: {self.alarm}")

    def get_stats(self) -> None:
        """Выводит историю срабатываний будильника."""
        if not self._history:
            print("История пуста")
        else:
            print("=== История срабатываний ===")
            for record in self._history:
                print(f"#{record['snooze_number']}: будильник {record['alarm_time']} сработал в {record['triggered_at']}")

    @property
    def snooze_count(self) -> int:
        """Количество срабатываний будильника (свойство только для чтения)."""
        return self._snooze_count

    def __str__(self) -> str:
        return f"AlarmClock(time={self.time}, alarm={self.alarm})"

    def __repr__(self) -> str:
        return self.__str__()


# Пример использования
if __name__ == "__main__":
    clock = AlarmClock("00:00")
    clock.set_time("15:26")
    clock.set_alarm("14:30")
    clock.check_alarm()          # Можно спать дальше
    clock.set_snooze(56)          # Будильник отложен на 56 мин. Новое время: 15:26
    clock.check_alarm()           # 🛎️  Будильник! Пора вставать!
    clock.check_alarm()           # Можно спать дальше (уже не совпадает, если время не изменилось)
    clock.get_stats()
    clock.disable_alarm()
    print(clock)