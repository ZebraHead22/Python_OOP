# class ShoppingCart():

#     def __init__(self):
#         self.order_list = list()
#         self._total = 0
#         self.__add_count = 0

#     @staticmethod
#     def item_validate(value):
#         if not isinstance(value, str):
#             raise TypeError("Order peace must be string type!")
#         return value

#     @staticmethod
#     def price_validate(value):
#         if not isinstance(value, (int, float)):
#             raise TypeError("Price peace must be float or int type!")
#         return value

#     def add_item(self, item, price):
#         self.order_list.append(self.item_validate(item))
#         self._total += self.price_validate(price)
#         # self._total += price
#         self.__add_count += 1
#         print(
#             f"Add new item to shopping cart:\n Item: {item}\n Price: {price}\n Total: {self._total}")

#     # def get_total(self):
#     #     print(
#     #         f"Your shopping cart is:\n Items: {self.order_list}\n Total: {self._total}")

#     @property
#     def total(self):
#         return self._total

# test = ShoppingCart()
# # print(test.get_total())
# test.add_item('apple', 4)
# test.add_item('rasberry', 5)
# print(test.total)

class Thermometer:

    def __init__(self, temp):
        self.__temp = self.validate_temp(temp)
        print(f"Temperature is {self.__temp} C")

    @staticmethod
    def validate_temp(value):
        if not isinstance(value, (int, float)):
            raise TypeError("Temperature must be int!")
        return value

    @property
    def temp(self):
        return self.__temp
    
    @temp.setter
    def temp(self, value):
        self.__temp = self.validate_temp(value)


    def to_fahrenheit(self):
        return self.__temp * 9/5 + 32


t1 = Thermometer(36.6)
t1.temp = 38
print(t1.temp)
new_temp = t1.to_fahrenheit()
print(new_temp)