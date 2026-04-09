# Шаблон для решения
class LazyProperty:
    def __init__(self, func):
        self.func = func
        self.name = func.__name__

    def __get__(self, obj, objtype=None):
        if obj is None:
            return self
        value = self.func(obj)
        # Заменяем дескриптор на обычный атрибут (кэшируем)
        obj.__dict__[self.name] = value
        return value

# Проверка
class Data:
    def __init__(self, data):
        self.data = data
    
    @Logger
    @LazyProperty
    def processed(self):
        print("Вычисляем processed...")
        return [x * 2 for x in self.data]

d = Data([x**2 for x in range (1000000)])
print(d.processed)   # Вычисляем processed... [2, 4, 6]
print(d.processed)   # [2, 4, 6] (без повторного вычисления)