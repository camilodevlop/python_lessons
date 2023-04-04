numbers = range(10)
even_lst = []

# Creating a new list from the even numbers. The numbers are multiplied
# by themselves.

for number in numbers:
    if number % 2 == 0:
        even_lst.append(number*number)

print(f'\n\tList comprehensions.\n\tEven numbers: {even_lst}')


# Repeating the above exercise using list comprehensions.
# [ expression for var in collection if condition ]
# The instruction 'if' is optional.

even_lst = []
even_lst = [number*number for number in numbers if number % 2 == 0]
print(f'\tUsing list comprehensions: {even_lst}')

evens = [number for number in range(50) if number % 2 == 0 and number % 6 == 0]
print(f'\tEvens: {evens}')

# List comprehensions and if/else.
even_lst = []
odd_lst = []

[even_lst.append(number) if number % 2 == 0 else odd_lst.append(number) for number in range(10)]
print(f'\tEven list:{even_lst}')
print(f'\tOdd list: {odd_lst}')

#-------------------------------------------------------------------

# List comprehensions and list of lists.
list_lists = [[1,2,3], [5,6,7], [8,9,10, 11]]

simple_lst = [value
              for lst in list_lists
              for value in lst]

print(f'\tSimple list: {simple_lst}')


# Creating a new list from the even numbers. The numbers are extracted
# from the list of lists.

even_lst = []
for lst in list_lists:
    for value in lst:
        if value % 2 == 0:
            even_lst.append(value)

print(f'\n\tEven numbers: {even_lst}')

# Creating a new list from the even numbers using list comprehensions.
# The numbers are extracted from the list of lists.

even_lst = [value
            for lst in list_lists
            for value in lst 
            if value % 2 == 0]
print(f'\tEven numbers -list comprehensions-: {even_lst}')

#-------------------------------------------------------------------
