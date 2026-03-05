class ShoppingCart:
    """Класс для управления корзиной покупок."""
    _total_carts = 0  # защищённый счётчик созданных корзин

    def __init__(self):
        self.items = []          # список товаров
        self._total = 0.0         # общая стоимость (защищённый атрибут)
        self._item_count = 0      # общее количество предметов (защищённый)
        ShoppingCart._total_carts += 1
        self._id = ShoppingCart._total_carts
        print(f"Создана новая корзина. ID = {self._id}")

    @staticmethod
    def _validate_item_name(name):
        """Проверяет, что название товара — строка."""
        if not isinstance(name, str):
            raise TypeError("Название товара должно быть строкой")
        return name.strip()

    @staticmethod
    def _validate_price(price):
        """Проверяет, что цена — положительное число (int или float)."""
        if not isinstance(price, (int, float)):
            raise TypeError("Цена должна быть числом (int или float)")
        if price <= 0:
            raise ValueError("Цена должна быть положительной")
        return float(price)

    @staticmethod
    def _validate_count(count):
        """Проверяет, что количество — целое положительное число."""
        if not isinstance(count, int):
            raise TypeError("Количество должно быть целым числом")
        if count <= 0:
            raise ValueError("Количество должно быть положительным")
        return count

    def add_item(self, name, price, count):
        """Добавляет товар в корзину."""
        name = self._validate_item_name(name)
        price = self._validate_price(price)
        count = self._validate_count(count)

        self.items.append({
            "item": name,
            "price": price,
            "count": count
        })
        self._total += price * count
        self._item_count += count
        print(f"Товар добавлен в корзину {self._id}: {name}, цена={price}, количество={count}")

    def remove_item(self, name):
        """Удаляет все вхождения товара с указанным именем."""
        initial_count = len(self.items)
        self.items = [item for item in self.items if item["item"] != name]
        removed = initial_count - len(self.items)
        if removed:
            # пересчитываем общую стоимость и количество
            self._recalculate()
            print(f"Удалено {removed} записей товара '{name}' из корзины {self._id}")
        else:
            print(f"Товар '{name}' не найден в корзине {self._id}")

    def _recalculate(self):
        """Пересчитывает общую стоимость и количество предметов."""
        self._total = sum(item["price"] * item["count"] for item in self.items)
        self._item_count = sum(item["count"] for item in self.items)

    @property
    def total(self):
        """Возвращает общую стоимость товаров в корзине."""
        return self._total

    @property
    def item_count(self):
        """Возвращает общее количество предметов в корзине."""
        return self._item_count

    @classmethod
    def total_carts(cls):
        """Возвращает количество созданных корзин."""
        return cls._total_carts

    def __str__(self):
        return f"ShoppingCart(id={self._id}, items={len(self.items)}, total={self._total:.2f})"

    def __repr__(self):
        return self.__str__()


# Пример использования
if __name__ == "__main__":
    cart1 = ShoppingCart()
    cart1.add_item("Bounty Trio", 94, 2)
    cart1.add_item("Milk", 65.5, 1)
    print(cart1)
    print(f"Общая стоимость: {cart1.total}")
    print(f"Всего предметов: {cart1.item_count}")
    cart1.remove_item("Bounty Trio")
    print(cart1)



class BankAccount:
    """Класс банковского счёта."""
    _total_accounts = 0

    def __init__(self, owner, phone_number):
        self._balance = 0.0
        BankAccount._total_accounts += 1
        self._id = BankAccount._total_accounts
        self.owner = self._validate_owner(owner)
        self.phone_number = self._validate_phone(phone_number)
        print(f"Создан новый счёт:\n  Владелец: {self.owner}\n  ID: {self._id}\n  Баланс: {self._balance}\n  Телефон: {self.phone_number}\n---")

    @staticmethod
    def _validate_owner(name):
        """Проверяет, что имя владельца содержит хотя бы два слова."""
        if not isinstance(name, str):
            raise TypeError("Имя владельца должно быть строкой")
        if len(name.split()) < 2:
            raise ValueError("Имя владельца должно содержать имя и фамилию")
        return name.strip()

    @staticmethod
    def _validate_phone(phone):
        """Проверяет, что номер телефона состоит из 10 цифр, и возвращает в формате +7XXXXXXXXXX."""
        if not isinstance(phone, str):
            raise TypeError("Номер телефона должен быть строкой")
        # Удаляем возможные пробелы, скобки, дефисы
        cleaned = ''.join(filter(str.isdigit, phone))
        if len(cleaned) != 10:
            raise ValueError("Номер телефона должен содержать ровно 10 цифр")
        return f"+7{cleaned}"

    @staticmethod
    def _validate_amount(amount):
        """Проверяет, что сумма — неотрицательное число."""
        if not isinstance(amount, (int, float)):
            raise TypeError("Сумма должна быть числом")
        if amount < 0:
            raise ValueError("Сумма не может быть отрицательной")
        return float(amount)

    @property
    def balance(self):
        """Текущий баланс счёта."""
        return self._balance

    def deposit(self, amount):
        """Внесение средств на счёт. Возвращает новый баланс."""
        amount = self._validate_amount(amount)
        self._balance += amount
        print(f"Внесено {amount:.2f}. Новый баланс счёта {self.owner}: {self._balance:.2f}")
        return self._balance

    def withdraw(self, amount):
        """Снятие средств со счёта. Возвращает новый баланс."""
        amount = self._validate_amount(amount)
        if amount > self._balance:
            raise ValueError("Недостаточно средств на счёте")
        self._balance -= amount
        print(f"Снято {amount:.2f}. Новый баланс счёта {self.owner}: {self._balance:.2f}")
        return self._balance

    def close_account(self):
        """Закрытие счёта (обнуление данных)."""
        print(f"Счёт {self._id} ({self.owner}) закрыт. Финальный баланс: {self._balance:.2f}")
        self._balance = None
        self.owner = None
        self.phone_number = None

    @classmethod
    def total_accounts(cls):
        """Возвращает общее количество созданных счетов."""
        return cls._total_accounts

    def __str__(self):
        return f"BankAccount(id={self._id}, owner={self.owner}, balance={self._balance:.2f})"

    def __repr__(self):
        return self.__str__()


# Пример использования
if __name__ == "__main__":
    try:
        acc = BankAccount("Дарья Сергеева", "9112230951")
        acc.deposit(1231445)
        acc.withdraw(456)
        print(acc)
        acc.close_account()
    except Exception as e:
        print(f"Ошибка: {e}")