# import  typing
#
# class Product:
#     """
#     This is definition of this class
#     """
#     product_count = 0
#     __price_average = 0
#
#     def __init__(self, name, price):
#         Product.product_count += 1
#         Product.__price_average = ((Product.__price_average + Product.product_count) + price)/ (Product.product_count + 1 )
#         self.name = name
#         self.price = price
#         self.__attrs = {'name': self.name, 'price': self.price}
#
#     # __ makes private _ makes protected
#     def __calculate_discount(self, discount_rate):
#         return self.price - self.price* discount_rate
#
#     def simulate_discount(self, discount_rate: float) -> float:
#         """asdsad"""
#         return self.__calculate_discount(discount_rate)
#
#     @staticmethod
#     def get_average_price():
#         return Product.__price_average
#
#     def __lt__(self, other):
#         return self.price < other.price
#
#     def __getitem__(self, item):
#         return  self.__attrs.get(item)
#
#
# crowbar = Product('levye', 100)
#
# print(crowbar.name, crowbar.price)
# # print(crowbar.simulate_discount(0.3))
#
# crowbar.__calculate_discount = 5
# print(crowbar.__calculate_discount)
# print(crowbar.simulate_discount(0.3))
# print(crowbar.__calculate_discount)
#
# hamer = Product('çekiç', 150)
# print(hamer.product_count)
#
#
# print('Average:', Product.get_average_price())
#
#
# print(crowbar < hamer)
# print(hamer < crowbar)
#
# print(hamer['None'])
# print(hamer['price'])
# print(hamer['name'])





# Inheritance  Abstraction
from abc import ABC, abstractmethod

class DBClass(ABC):
    def __init__(self, _id):
        self._id = _id
    @abstractmethod
    def print_obj(self):
        print(f'fid: {self._id}')

    @property
    def id(self):
        return self._id

class Category(DBClass):
    def print_obj(self):
        super(Category, self).print_obj()
        print(self.name)

    def __init__(self, _id,name):
        super(Category, self).__init__(_id)
        self.name = name

    def __repr__(self):
        return str({'id:': self.id, 'name:': self.name})


computer = Category(1, 'computer')
print({'name': computer.name, 'id':computer.id})
computer.print_obj()
print(computer)