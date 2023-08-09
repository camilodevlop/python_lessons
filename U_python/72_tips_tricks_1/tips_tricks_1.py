
#-------------------------------------------------------------------

# Assertions help us to debug errors that cause program termination.

# Example 1. Reviewing division by zero.
def division(a, b):
    assert b != 0, 'Division by Zero.'
    print(f'Division Result: {a/b}')

# Example 2. Qualification average.
def qualification_average(qualifications):
    assert len(qualifications) != 0, 'Empty qualification list.'
    print(f'Qualification average: {sum(qualifications)/len(qualifications)}')

# Example 3. Product discounts.
def product_discount(products, discount):
    price_discount = products['price'] * (1.0 - discount)
    assert 0 <= price_discount <= products['price'], 'Invalid discount.'
    print(f'Price including discount: {price_discount}')

#-------------------------------------------------------------------

if __name__ == '__main__':

    # Assertions.

    # Example 1:
    division(3,1)
    # division(3,0)

    # Example 2:
    qualifications = [1, 2, 3, 4, 5]
    qualification_average(qualifications)
    # qualification_average([])

    # Example 3:
    products = { 'name: ' : 'Shirt', 'price' : 1500 }
    product_discount(products, 0.1)
    # product_discount(products, 1.1)

#-------------------------------------------------------------------
