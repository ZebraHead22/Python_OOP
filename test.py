```python
class SortFilterDecorator:
    """
    Декоратор-класс для сортировки и фильтрации списка перед выводом через join.
    
    Параметры:
        reverse (bool): если True, сортировка в обратном порядке, иначе в прямом.
        numeric_only (bool): если True, оставляет в списке только числовые элементы (int, float),
                             иначе сортирует все элементы без фильтрации.
    """
    def __init__(self, reverse=False, numeric_only=False):
        self.reverse = reverse
        self.numeric_only = numeric_only

    def __call__(self, func):
        def wrapper(lst, *args, **kwargs):
            # Работаем с копией, чтобы не изменять исходный список
            processed = lst.copy()

            if self.numeric_only:
                # Оставляем только числа
                processed = [x for x in processed if isinstance(x, (int, float))]

            # Сортируем
            processed.sort(reverse=self.reverse)

            # Вызываем исходную функцию с обработанным списком
            return func(processed, *args, **kwargs)
        return wrapper


# Пример использования
@SortFilterDecorator(reverse=True, numeric_only=True)
def list_to_joined_string(lst):
    return ', '.join(str(item) for item in lst)


# Тестирование
data = [1, 'hello', 3.5, 'world', 2, 7, 'abc']
print(list_to_joined_string(data))  # Вывод: 7, 3.5, 2, 1

# Без фильтрации (сортировка всех элементов)
@SortFilterDecorator(reverse=False, numeric_only=False)
def list_to_joined_string2(lst):
    return ', '.join(str(item) for item in lst)

data2 = ['banana', 'apple', 'cherry']
print(list_to_joined_string2(data2))  # Вывод: apple, banana, cherry
```