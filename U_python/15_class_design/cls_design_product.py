# Class design: Product.

class Product:
    product_counter = 0

    def __init__(self, name = '', price = 0.0) -> None:
        self._id_product = Product._increment_product_counter()
        self._name = name
        self._price = price

    @property
    def id_product(self):
        return self._id_product

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, price):
        self._price = price

    @classmethod
    def _increment_product_counter(cls):
        cls.product_counter += 1
        return cls.product_counter

    def __str__(self) -> str:
        return f'\tID: {self._id_product} Product: {self._name} Price: {self._price}'

#-------------------------------------------------------------------

if __name__ == '__main__':
   print('\n\tProducts\n')
   product1 = Product('Shirt', 100.00) 
   print(product1)

   product2 = Product('Pants', 150.00) 
   print(product2)

#-------------------------------------------------------------------
