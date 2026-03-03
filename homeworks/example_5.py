# class Animal:

#     def __init__(self, name, breed):
#         self.name = name
#         self.breed = breed
#         print("Run __init__ in Animal...")

#     def make_sound(self):
#         print("Some generic sound")


# class Dog(Animal):

#     def __init__(self, name, breed, color):
#         print("Run __init__ in Dog...")
#         super().__init__(name, breed)
#         self.color = color

#     def make_sound(self):
#         print("Woof!")


# class Cat(Animal):

#     def __init__(self, name, breed, tongue=True):
#         super().__init__(name, breed)
#         self.tongue = tongue

#     def make_sound(self):
#         print("Meow!")


# animals = [Dog("Rex", "Taksa", "red"), Cat("Whiskers", "Nevskiy")]
# for animal in animals:
#     print(f"{animal.name}: ", end="")
#     animal.make_sound()



# class Vehicle:

#     brands = ["Opel", "BMW", "Skoda", "Audi", "Porshe"]

#     def __init__(self, brand, year):
#         self.brand = self.brand_validate(brand)
#         self.year = year

#     def display_info(self):
#         print(f"Brand: {self.brand}\nYear: {self.year}")

#     @staticmethod
#     def brand_validate(brand):
#         if not isinstance(brand, str):
#             raise TypeError("Brand must be srt type!")
#         if brand not in Vehicle.brands:
#             raise ValueError("Brand must be Deutsche")
#         return brand
        
#     @staticmethod
#     def num_doors_validate(num_doors):
#         if not isinstance(num_doors, int):
#             raise TypeError("Number of doors must be int type")
#         if num_doors < 3 or num_doors > 5:
#             raise ValueError("Check doors")
#         return num_doors


# class Car(Vehicle):

#     def __init__(self, brand, year, num_doors):
#         super().__init__(brand, year)
#         self.num_doors = self.num_doors_validate(num_doors)

#     def display_info(self):
#         print(f"Brand: {self.brand}\nYear: {self.year}\nNumber of doors: {self.num_doors}")

# v = Vehicle("Opel", 2013)
# c = Car("Audi", 2018, 7)

# v.display_info()
# c.display_info()


class Writer:
    def create(self):
        return "Writing a novel"

class Painter:
    def create(self):
        return "Painting a picture"

class Musician:
    def create(self):
        return "Composing a song"

def show_creativity(person):
    # Вызываем метод create, если он существует (утиная типизация)
    print(person.create())

# Демонстрация утиной типизации
if __name__ == "__main__":
    writer = Writer()
    painter = Painter()
    musician = Musician()

    # Все объекты имеют метод create, поэтому функция работает с каждым
    show_creativity(writer)   # Writing a novel
    show_creativity(painter)  # Painting a picture
    show_creativity(musician) # Composing a song