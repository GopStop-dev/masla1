"""class Product:
    def __init__(self, name: str, price: int, discount: int):
        self.__name = name
        self.__price = price
        self.__discount = discount

    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price):
        self.__price = price - (price * self.__discount / 100)

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, discount):
        if discount > 0 or discount < 50:
            self.__discount = discount

obj = Product("Laptop", 1000000, 10)
print(obj.price)

obj.discount = 20
print(obj.price)

obj.price = 2000000
print(obj.price)"""

class Product:
    def __init__(self, name: str, price: int, discount: int):
        self.__name = name
        self.__original_price = price
        self.__discount = discount

    @property
    def price(self):
        return self.__original_price - (self.__original_price * self.__discount / 100)

    @property
    def discount(self):
        return self.__discount

    @discount.setter
    def discount(self, discount):
        if 0 < discount < 50: 
            self.__discount = discount

    @property
    def original_price(self):
        return self.__original_price

    @original_price.setter
    def original_price(self, price):
        self.__original_price = price  

# Usage
obj = Product("Laptop", 1000000, 10)
print(obj.price) 

obj.discount = 20
print(obj.price) 

obj.original_price = 2000000 
print(obj.price)  
