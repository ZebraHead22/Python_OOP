class DataTypeError(TypeError):
    def __init__(self, data):
        self.data = data
        super().__init__(f"Data must be list with int numbers!")

class KeyDataError(TypeError):
    def __init__(self, key):
        self.key = key
        super().__init__(f"Key must be INT!")

class SafeVector:
    __slots__ = ('_data', '_size')

    @staticmethod
    def data_validate(data):
        if not isinstance(data, list) or not all (isinstance(x ,int) for x in data):
            raise DataTypeError(data)
        return data

    @staticmethod
    def value_validate(value):
        if not isinstance(value, int):
            raise TypeError(f"Value must be int!")

        return value
    
    def key_validate(self, key):
        if not isinstance(key, int):
            raise KeyDataError(key)
        if key >= self._size:
            raise IndexError(f"Key must be less than size of data!")
        
        return key


    def __init__(self, data : list = None):
        self._data = self.data_validate(data)
        self._size = len(self._data)

    def __getitem__(self, key):
        return self._data[self.key_validate(key)]
    
    def __setitem__(self, key, value):
        self._data[self.key_validate(key)] = self.value_validate(value)

    def append(self, value):
        self._data.append(self.value_validate(value))
        self._size = len(self._data)


try:
    sf = SafeVector([1, 2, 3])
    sf[2] = '3'
except TypeError as e:
    print(e)
except IndexError as e:
    print(e)
except DataTypeError as e:
    print(e)
except KeyDataError as e:
    print(e)