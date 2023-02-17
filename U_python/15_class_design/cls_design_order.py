# Class design: Order.

from cls_design_product import Product

class Order:
    order_counter = 0
    
    def __init__(self, products) -> None:
        self._id_order = Order._increment_order_counter()
        self._products = list(products)
    
    @classmethod
    def _increment_order_counter(cls):
        cls.order_counter += 1
        return cls.order_counter
   
    def add_product(self, product):
        self._products.append(product)

    def total_price(self):
        total = 0
        for product in self._products:
            total += product.price

        return total

    def __str__(self) -> str:
        str_product = '\n\t'
        for product in self._products:
           str_product += product.__str__() + '\n\t'

        return f'\tID Order: {self._id_order} Total: {self.total_price()}\n\tDetails: {str_product}\n'
        
#-------------------------------------------------------------------

if __name__ == '__main__':
   product1 = Product('Shirt', 100.00) 
   product2 = Product('Pants', 150.00) 
   products = [product1, product2]

   order1 = Order(products)
   print('\n',order1)

   order2 = Order(products)
   print('\n',order2)

#-------------------------------------------------------------------
