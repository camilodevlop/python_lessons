# The underscore indicates that a variable is temporary or unimportant.

for _ in range(3):
    print(f'Hello... {_}')

# It is useful to process tuples.
values = ('Camilo', 'Castillo', 36)
name, _, age = values
print(name)
print(age)
print(_)

# it is useful as a temporary var.
_ = list()
_.append(1)
_.append(2)
_.append(3)
_.append(4)
_.append(5)
print(_)

#-------------------------------------------------------------------



#-------------------------------------------------------------------
