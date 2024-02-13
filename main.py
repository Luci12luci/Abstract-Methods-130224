# from abc import ABC, abstractmethod
#
# class Zviera(ABC):
#     @abstractmethod
#     def zvuk(self):
#         pass
#
# class Pes(Zviera):
#     def zvuk(self):
#         return "Haf"
#
# class Macka(Zviera):
#     def zvuk(self):
#         return "Mnau"
#
# moj_pes = Pes()
# print(moj_pes.zvuk())
#
# moja_macka = Macka()
# print(moja_macka.zvuk())


# SOLID PRINCIPY
# MVC PATTERN

class ShoeController:
    def __init__ (self, id, gender_type, color, price, brand, size):
        self.id = id
        self.gender_type = gender_type
        self.color = color
        self.price = price
        self.brand = brand
        self.size = size
        self.is_completed = False

    def complete(self):
        self.is_completed = True

class TaskModel:
    def __init__(self):
        self.shoes = None
        self.task = []

    def add_shoes_model(self, shoes):
        self.shoes.append(shoes)

    def get_shoes_model(self, shoes):
        return self.shoes

class TaskView:
    def display_shoes(self, shoes):



