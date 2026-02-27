
# class ShoppingCart:

#     count = 0

#     def __init__(self):
#         self.items = list()
#         self._total = 0
#         self.__add_count = 0
#         ShoppingCart.count += 1
#         self.__id = ShoppingCart.count
#         print(f"Create new shopping cart...\nID = {self.__id}")

#     @staticmethod
#     def item_name_validate(name):
#         if not isinstance(name, str):
#             raise TypeError("Item name must be str type!")
#         return name
    
#     @staticmethod
#     def price_validate(price):
#         if not isinstance(price, (int, float)):
#             raise TypeError("Price must be float or int type!")
#         if price <= 0:
#             raise ValueError("Price should be positive...") 
#         return price    
    
#     def add_item(self, name, price, item_count):
#         try:
#             self.items.append(
#                 {
#                     "Item" : self.item_name_validate(name),
#                     "Price" : self.price_validate(price),
#                     "Count": self.price_validate(item_count)
#                 }
#             )
#             self._total += price * item_count
#             self.__add_count += item_count
#             print(f"Add new item to cart {self.__id}:\n-Name: {name}\n-Price: {price}\n-Count: {item_count}")
#         except Exception as e:
#             print(f"R u ok?? U have some Error: {e}")

        

#     def get_total(self):
#         print(f"Total for cart {self.__id}: {self._total}")

#     @classmethod
#     def get_count(cls):
#         print(f"Shopping cart number: {cls.count}")

# cart_1 = ShoppingCart()
# # cart_2 = ShoppingCart()
# # cart_3 = ShoppingCart()
# # cart_4 = ShoppingCart()
# # cart_5 = ShoppingCart()

# cart_1.add_item("Bounty Trio", 94, "24")
# # cart_1.add_item("Oil", 50, 4)

# # cart_2.add_item("potato", 5, 10)
# # cart_2.add_item("cucumber", 500000, 1)
# print()
# cart_1.get_total()
# # print()
# # cart_2.get_total()
# # print()
# # ShoppingCart.get_count()

# # print(cart_1.items)


class BankAccount:

    accounts = 0

    def __init__(self, owner, phone_number):
        self._balance = 0
        BankAccount.accounts += 1
        self.__id = BankAccount.accounts
        self.owner = self.owner_val(owner)
        self.phone_number = "+7" + str(self.phone_number_val(phone_number))
        print(f"Create new bank account:\n-Owner is {self.owner}\n-ID = {self.__id}\n-Balance = {self._balance}\n-Phone: {self.phone_number}")
        print("---")

    @staticmethod
    def phone_number_val(phone_number):
        if not isinstance(phone_number, int):
            raise TypeError("Phone_number must be str!")
        if not len(str(phone_number)) == 10:
            raise ValueError("Phone_number shoud contain all digits...")
        return phone_number 
    
    @staticmethod
    def owner_val(name):
        if not isinstance(name, str):
            raise TypeError("Name must be str!")
        if not len(name.split()) >= 2:
            raise ValueError("Name shoud contain all name...")
        return name
    
    @staticmethod
    def amount_val(amount):
        if not isinstance(amount, (int, float)):
            raise TypeError("Amount must be int or float!")
        if amount < 0:
            raise ValueError("Amount must be positive!")
        return amount

    @property
    def balance(self):
        return self._balance

    @balance.deleter
    def balance(self):
        self._balance = None
        self.owner = None
        print(f"Delete account:\n Name: {self.owner}\nBalance: {self._balance}")

    
    def deposit(self, amount):
        self._balance += self.amount_val(amount)
        print(f"New balance of {self.owner} is {self._balance}")


    def withdraw(self, amount):
        if self.amount_val(amount) > self._balance:
            raise ValueError("Balance must be more than amount!")
        self._balance -= self.amount_val(amount)
        print(f"New balance of {self.owner} is {self._balance}")


try:
    acc = BankAccount("Dasha Sergeeva", 9112230951)
    acc.deposit(1231445)
    acc.withdraw(456)

except Exception as e:
    print(f"EEEERRRROOOOOOOOOOOOOOR: {e}")
    
        