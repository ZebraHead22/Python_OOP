# 1 Logger

# Шаблон для решения
import datetime
import time

class Logger:

    def __init__(self, filename, mode='w', encoding='utf-8'):
        self.filename = filename
        self.mode = mode
        self.encoding = encoding
        self.file = None

    def __enter__(self):
        # открыть файл, записать время входа
        print(f"🟢 Открываем файл {self.filename}")
        self.file = open(self.filename, self.mode, encoding=self.encoding)
        now = datetime.datetime.now()
        formatted = now.strftime('%Y-%m-%d %H:%M:%S\n')

        self.file.write(f'[ВХОД] {formatted}')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        # записать время выхода или информацию об исключении
        # не забыть закрыть файл
        
        if self.file:
            if exc_type is not None:
                print(f"⚠️ Исключение: {exc_type.__name__}: {exc_val}")
                self.file.write(f'[ИСКЛЮЧЕНИЕ] {exc_type.__name__}: {exc_val}\n')
        
        now = datetime.datetime.now()
        formatted = now.strftime('%Y-%m-%d %H:%M:%S')
        self.file.write(f'[ВЫХОД] {formatted}\n')
        self.file.close()
        print(f"🔴 Закрываем файл {self.filename}")
        return False

# Проверка
with Logger('test_log.txt'):
    print("Работа без ошибок", end=' ', flush=True)
    
    # Прогресс-бар на 3 секунды
    total = 10
    for i in range(1, total + 1):
        filled = '█' * i
        empty = '░' * (total - i)
        print(f'\r[{filled}{empty}] {i}/{total}', end='', flush=True)
        time.sleep(1)
    print()  # переводим строку после завершения бара
    
    raise ValueError("Ой!")

# 2 Limitedclass