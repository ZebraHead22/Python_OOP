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
    
    
    
    class Worker:
    """
    Простой класс Worker, демонстрирующий использование __new__.
    """
    _instance_counter = 0

    def __new__(cls, *args, **kwargs):
        """
        Переопределённый __new__ для отслеживания создания экземпляров.
        """
        instance = super().__new__(cls)
        cls._instance_counter += 1
        instance._id = cls._instance_counter
        print(f"Создан Worker #{instance._id}")
        return instance

    def __init__(self):
        # Состояние Worker'а (может быть сброшено при возврате в пул)
        self._busy = False

    def reset(self):
        """Сброс состояния Worker'а перед повторным использованием."""
        self._busy = False
        print(f"Worker #{self._id} сброшен")

    def __repr__(self):
        return f"<Worker #{self._id}>"


class Pool:
    """
    Пул объектов Worker с ограниченным размером.
    """
    def __init__(self, max_size):
        self.max_size = max_size
        self._available = []      # список свободных Worker'ов
        self._created_count = 0   # общее количество созданных Worker'ов

    def get(self):
        """
        Возвращает Worker из пула.
        Если есть свободный – возвращает его.
        Иначе, если лимит не превышен – создаёт новый Worker.
        Если лимит достигнут – возвращает None.
        """
        if self._available:
            worker = self._available.pop()
            print(f"Выдан существующий {worker}")
            return worker

        if self._created_count < self.max_size:
            worker = Worker()
            self._created_count += 1
            print(f"Выдан новый {worker}")
            return worker

        print("Пул пуст, лимит достигнут, возвращаем None")
        return None

    def release(self, worker):
        """
        Возвращает Worker обратно в пул.
        Перед возвратом сбрасывает его состояние (опционально).
        """
        if worker is None:
            return
        worker.reset()
        self._available.append(worker)
        print(f"{worker} возвращён в пул")


# Пример использования
if __name__ == "__main__":
    pool = Pool(max_size=2)

    w1 = pool.get()   # создаётся новый Worker #1
    w2 = pool.get()   # создаётся новый Worker #2
    w3 = pool.get()   # лимит достигнут -> None

    print(f"w1 = {w1}, w2 = {w2}, w3 = {w3}")

    pool.release(w2)  # возвращаем w2 в пул
    w3 = pool.get()   # теперь получаем w2 снова
    print(f"w3 после release = {w3}")
    
    