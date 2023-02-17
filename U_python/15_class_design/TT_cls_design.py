
from cls_design_product import Product
from cls_design_order import Order

product1 = Product('Shirt', 100.00) 
product2 = Product('Pants', 150.00) 
product3 = Product('Socks', 50.00)
product4 = Product('T-Shirt', 70.00)
product5 = Product('Shoes', 200.00)

products1 = [product1, product2]
products2 = [product3, product4]

order1 = Order(products1)
print('\n',order1)
order1.add_product(product5)
print('\n',order1)

order2 = Order(products2)
print('\n',order2)

#-------------------------------------------------------------------
