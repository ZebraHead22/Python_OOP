class Config:

    _allowed_keys = ['user', 'theme', 'language']

    def __init__(self):
        self.config = dict()
        print('Create new file for config...')

    @staticmethod
    def _settings_validate(settings):
        if not isinstance(settings, dict):
            raise TypeError('Settings must be upload in dictionary.')
        
        for key in settings.keys():
            key = Config._key_validate(key)
        return settings

    @staticmethod
    def _key_validate(key):
        if key not in Config._allowed_keys:
                raise ValueError(f'Invalid key.\nAllowed keys store in {Config._allowed_keys}')

        return key

    def load(self, settings):

        settings = self._settings_validate(settings)

        if 'user' not in settings.keys():
            self.config = settings
            self.config['user'] = None

        if 'theme' not in settings.keys():
            self.config = settings
            self.config['theme'] = 'light'

        if 'language' not in settings.keys():
            self.config = settings
            self.config['language'] = 'EN'

        else:
            self.config = settings

        print(self.config)

    def __call__(self, key):
        key = self._key_validate(key)
        return self.config[key]
    
    def __getitem__(self, key):
        key = self._key_validate(key)
        return self.config[key]
    
    def __setitem__(self, key, value):
        key = self._key_validate(key)
        self.config[key] = value

try:
    config = Config()   
    config.load({"name": "Alina"})

    print(config("theme"))     # "dark" - через вызов
    print(config["language"])  # "ru" - через индексацию

    # config["theme"] = "light"  # Изменение значения
    # print(config("theme"))     # "light"
except Exception as e:
    print(f'ERROR: {e}')



class Calculator:

    _OPERATORS = ['+', '-', '*', '/']

    def __init__(self):
        self.history = []

    @staticmethod
    def validate(a, b):
        if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
            raise TypeError('A & B must be INT or FLOAT type!')
        return a, b
    
    def __call__(self, a, operator, b):
        a, b = self.validate(a, b)
        if hasattr(self, '_OPERATORS') and operator not in self._OPERATORS:
            raise ValueError(f'Invalid operator.\nAllow operators store in {self._OPERATORS}')
        
        if operator == '+':
            self.history.append(f'{a} + {b} = {a + b}')
            return a + b
        
        if operator == '-':
            self.history.append(f'{a} - {b} = {a - b}')
            return a - b
        
        if operator == '*':
            self.history.append(f'{a} * {b} = {a * b}')
            return a * b
        
        if operator == '/':
            if b == 0:
                raise ZeroDivisionError('Divide by zero!')
            self.history.append(f'{a} / {b} = {round(a / b, 2)}')
            return float(round(a / b, 2))


    def show_history(self):
        print('History:')
        print('--> '+'\n--> '.join(self.history))

    def __len__(self):
        return len(self.history)
    


import numpy as np
import math
from matplotlib import pyplot as plt

class Differential:
    def __init__(self, func):
        self.func = func
    
    
    def __call__(self, f, x, y, num=1000, eps=1e-4):
        
        def deriative(x):
            return (f(x + eps) - f(x - eps)) / (2 * eps)

        self.func(deriative, x, y, num=1000)

class Differential2:
    def __init__(self, func):
        self.func = func
    
    
    def __call__(self, f, x, y, num=1000, eps=1e-6):
        
        def deriative(x):
            return (f(x + eps) - 2*f(x)+ f(x - eps)) / (eps**2)

        self.func(deriative, x, y, num=1000)

def func(x):
    return np.arctan(x) ** 2

@Differential
@Differential
@Differential
@Differential
@Differential
@Differential
@Differential
@Differential
@Differential
@Differential
@Differential
@Differential
@Differential
@Differential
@Differential
@Differential
@Differential
@Differential
@Differential
@Differential
def plot(f, x, y, num=1000):
    X = np.linspace(x,y, num)
    Y = f(X)
    plt.plot(X, Y)
    plt.grid()
    plt.xlabel('a.u.')
    plt.ylabel('a.u.')
    plt.title('Graph')
    plt.show()

plot(func, -10,  10)