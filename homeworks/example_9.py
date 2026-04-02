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

    @staticmethod
    def now(template = '%Y-%m-%d %H:%M:%S\n'):
        now = datetime.datetime.now()
        formatted = now.strftime(template)
        return formatted

    def __enter__(self):
        # открыть файл, записать время входа
        print(f"🟢 Открываем файл {self.filename}")
        self.file = open(self.filename, self.mode, encoding=self.encoding)

        self.file.write(f'[ВХОД] {self.now('%d-%m-%Y %H:%M:%S\n')}')
        return self.file

    def __exit__(self, exc_type, exc_val, exc_tb):
        # записать время выхода или информацию об исключении
        # не забыть закрыть файл
        
        if self.file:
            if exc_type is not None:
                print(f"⚠️ Исключение: {exc_type.__name__}: {exc_val}")
                self.file.write(f'[ИСКЛЮЧЕНИЕ] {exc_type.__name__}: {exc_val}\n')

            self.file.write(f'[ВЫХОД] {self.now()}\n')
            self.file.close()
            print(f"🔴 Закрываем файл {self.filename}")
            return True

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
    
    # raise ValueError("Ой!")

# 2 Limitedclass
# Шаблон для решения
class LimitedInstances:
    _count = 0

    def __new__(cls, *args, **kwargs):
        
        if '_count' not in cls.__dict__:
            cls._count = 0

        max_insts = getattr(cls, 'max_instances', None)

        if cls._count >= max_insts and max_insts is not None:
            raise RuntimeError(f"Too many instances.\nMax number of the instances is {max_insts}")
        
        cls._count += 1 
        instance = super().__new__(cls)
        return instance

                  

# Реализуйте дочерний класс
class MyClass(LimitedInstances):
    max_instances = 2
    
    def __init__(self, x):
        self.x = x
        


# Проверка
try:
    a = MyClass(2)
    b = MyClass(2)
    c = MyClass(2)
except RuntimeError as e:
    print(f"Ошибка: {e}")