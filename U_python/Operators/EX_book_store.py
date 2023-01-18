# Book_store.
print('\n\tEnter book information:')
name = input('\tEnter the name: ')
ID = int(input('\tEnter the ID: '))
price = float(input('\tEnter the price: '))
shipping = input('\tFree shipping (True/False): ')

if (shipping == 'True'): shipping = True
elif (shipping == 'False'): shipping = False
else: shipping = 'Invalid value'

print('\n\tBook Information:')
print(f'''
      Name: {name}
      ID: {ID}
      Price: {price}
      Shipping: {shipping}
      ''')

#--------------------------------------------------------------------
