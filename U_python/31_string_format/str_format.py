# Advanced study of the strings' format.

# Formatting a string.

name = 'Jack'
age = 28
format_msg = 'My name is %s and I am %d years old.' %(name, age)
print(format_msg)

#-------------------------------------------------------------------

person = ('Karla', 'Gomez', 5000.00)
#format_msg = 'Hello %s %s. Your salary is %.2f' %person
#format_msg = 'Hello %s %s. Your salary is %.2f' %(person[0], person[1], person[2])
format_msg = 'Hello %s %s. Your salary is %.2f'
print(format_msg%person)

#-------------------------------------------------------------------

name = 'Jack'
age = 28
salary = 3000.00
format_msg = 'Name: {} Age: {} Salary: {:.2f}'.format(name, age, salary)
print(format_msg)

#-------------------------------------------------------------------

# Formatting a string using indices.
format_msg = 'Name {0} Age {1} Salary {2:.2f}'.format(name, age, salary)
print(format_msg)

# You can change the order.
format_msg = 'Salary {2:.2f} Age {1} Name {0}'.format(name, age, salary)
print(format_msg)

#-------------------------------------------------------------------

# Formatting a string using names.
format_msg = 'Age {a} Name {n} Salary {s:.2f}'.format(n = name, a = age, s = salary)
print(format_msg)

#-------------------------------------------------------------------

# Formatting a string using dictionaries.
dictionary = {'Name':'Camilo', 'Age': 35, 'Salary': 8000.00}
format_msg = 'Age {person[Age]} Name {person[Name]} Salary {person[Salary]:.2f}'.format(person = dictionary)
print(format_msg)

#-------------------------------------------------------------------

# Formatting a string using f-string.
format_msg = f'Name: {name} Age: {age} Salary: {salary:.2f}'
print(format_msg)

#-------------------------------------------------------------------

# Print method.
print(name, age, salary, sep = '.....')

#-------------------------------------------------------------------
