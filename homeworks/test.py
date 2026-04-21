# class BankAccount:

#     def __init__(self):
#         self.__balance = 0

#     @staticmethod
#     def val(amount):
#         if not isinstance(amount, (int, float)):
#             raise TypeError("asdasd")
#         if amount <= 0:
#             raise ValueError("Amount must be more than 0!")
#         return amount

#     def deposit(self, amount):
#         self.__balance += self.val(amount)

#     def withdraw(self, amount):
#         self.val(amount)
#         if amount > self.__balance:
#             raise ValueError("Amount must be less than balance!")
#         self.__balance -= amount

#     @property
#     def balance(self):
#         return self.__balance

#     @balance.setter
#     def balance(self, value):
#         raise AttributeError("Invalid operation")


# acc = BankAccount()
# acc.deposit("1000")
# acc.withdraw("300")
# print(acc.balance)   # 700
# acc.balance = 0      # AttributeError


# class Typed:

#     def __init__(self, exp_type, name):
#         self.exp_type = exp_type
#         self.name = name

#     def __get__(self, instance, owner):
#         return instance.__dict__.get(self.name)

#     def __set__(self, instance, value):
#         if not isinstance(value, self.exp_type):
#             raise TypeError("ERROR")
#         instance.__dict__[self.name] = value


# class Person:

#     name = Typed(str, "name")
#     age = Typed(int, "age")

# p = Person()
# p.name = "Alice"   # OK
# p.age = 30         # OK
# # p.age = "тридцать" # TypeError


# class Logger:

#     def __init__(self, function):
#         self.function = function

#     def __call__(self, *args, **kwds):
#         return f"Вызов функции {self.function.__name__} c аргументами {args} -> {self.function(*args, **kwds)}"
      

# @Logger
# def add(a, b):
#     return a + b








# print(add(3, 5))   # Вызов функции add с аргументами (3, 5) -> 8


# class TempGlobal:

#     def __init__(self, name, value):
#         self.name = name
#         self.value = value
#         self._old_value = None

#     def __enter__(self):
#         self._old_value = globals().get(self.name)
#         # self.value = globals()[self.name]
#         globals()[self.name] = self.value
#         return self
    
#     def __exit__(self, exc_type, exc, tb):
#         globals()[self.name] = self._old_value


# x = 10
# with TempGlobal("x", 100):
#     print(x)   # 100
# print(x)       # 10
        

# class Database:

#     _instance = None
#     call_count = 0

#     def __new__(cls):
#         cls.call_count += 1
#         if cls._instance is None:
#             cls._instance = super().__new__(cls)
#             print("Создано соединение")
#         else:
#             print("Используем существующее")

#         return cls._instance
    
#     def __init__(self):
#         if not hasattr(self, "connected"):
#             self.connected = True

# db1 = Database()   # Создано соединение
# db2 = Database()   # Используем существующее
# print(db1 is db2)  # True
# print(Database.call_count)  # 2


# class Shape:

#     def __init__(self, color):
#         if not isinstance(color, str):
#             raise TypeError("TE!")
#         self._color = color

#     def get_color(self):
#         return self._color
    
#     def set_color(self, color):
#         if not isinstance(color, str):
#             raise TypeError("TE!")
#         self._color = color


# class Circle(Shape):

#     def __init__(self, color, radius):
#         super().__init__(color)
#         self.__radius = radius

#     @property
#     def area(self):
#         import math
#         return math.pi * (self.__radius**2)
    
#     def __str__(self):
#         return super().__str__(f"Circle: sraduis = {self.__radius}")
    
#     def _protected_method(self):
#         print("PROTECTED METHOD")


# c = Circle("red", 5)
# print(c.get_color())   # red
# print(c.area)          # 78.5398...
# c._protected_method()  # сработает, но IDE предупредит
# print(c.__radius)    # AttributeError


# class AddAttr:

#     def __init__(self, name, value):
#         self.name = name
#         self.value = value

#     def __call__(self, cls,  *args, **kwds):
#         setattr(cls, self.name, self.value)
#         return cls
        


# @AddAttr("version", 1.0)
# class MyClass:
#     pass

# print(MyClass.version)   # 1.0


# class Range:

#     def __init__(self, name, min_val=-273.15, max_val=1000):
#         self.name = name
#         self.min_val = min_val
#         self.max_val = max_val

#     def __get__(self, instance, owner):
#         return instance.__dict__.get(self.name)
    
#     def __set__(self, instance, value):
#         if not self.max_val >= value >= self.min_val:
#             raise ValueError("VA!")
        
#         print("OK")
#         instance.__dict__[self.name] = value


# class Temperature:

#     celsius = Range("celsius")    

# t = Temperature()
# t.celsius = 25        # OK
# t.celsius = -300      # ValueError


class CachedFunction:

    # __cache = {}

    # def __new__(cls, name):
    #     if name not in cls.__cache:
    #         instance = super.__new__(cls)
    #         cls.__cache[name] = instance
    #         return cls.__cache[name] if cls.__cache else None
        
    #     return cls.__cache[name]

    def __init__(self, func):
        self.func = func
        self.cache = {}
        

    def __call__(self, *args, **kwds):
        if args not in self.cache:
            result = self.func(*args, **kwds)
            self.cache[args] = result
            return self.cache[args] if self.cache else None
        
        return self.cache[args]



@CachedFunction
def slow_square(x):
    import time
    time.sleep(1)
    return x * x

print(slow_square(4))   # вычисляем -> 16 (задержка)
print(slow_square(4))   # из кэша -> 16 (мгновенно)