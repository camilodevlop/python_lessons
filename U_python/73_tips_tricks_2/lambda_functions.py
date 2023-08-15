# Lambda functions allow us to declare anonymous functions in a
# single line of code.

# Example: normal function.
def sum(a, b):
    return a + b

print(sum(4, 5))

# Example: lambda function.
lambda_sum = lambda a, b: a + b
print(lambda_sum(4, 7))

# Using a single line of code.
print((lambda a, b: a + b)(9, 7))

#-------------------------------------------------------------------

# A lambda function is recommended in case a concrete function is 
# required. Example: ordering a list of tuples.
tuples_list = [(1, 'b'), (2, 'f'), (5 , 'a'),(4, 'c')]
ordered_tuples_list = sorted(tuples_list, key = lambda tpl: tpl[0], reverse = False)
print(ordered_tuples_list)

ordered_tuples_list = sorted(tuples_list, key = lambda tpl: tpl[1], reverse = False)
print(ordered_tuples_list)

# Another example of sorting using lambda functions.
print(list(range(-3, 4)))
ordered_list = sorted(range(-3, 4), key = lambda value: value*value)
print(ordered_list)

#-------------------------------------------------------------------

# Closure and lambda functions.
def show(degree):
    return lambda message: degree + '. ' + message

test_1 = show('Engineer')
print(test_1('Camilo Castillo'))

#-------------------------------------------------------------------

# Cases in which the use of lambda functions is not appropriate.
# Example 1.
class Test:
    show = lambda self: print('Show Function.')
    greet = lambda self: print('Greet function.')

test = Test()
test.show()
test.greet()

# Example 2.
pair_list = list(filter(lambda value: value % 2  == 0, range(-10, 10)))
print(pair_list)

# Using list comprehensions.
modified_pair_list = [value for value in range(-10, 10) if value % 2 == 0]
print(modified_pair_list)

#-------------------------------------------------------------------
