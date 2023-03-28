# Lambda function: it is anonymous, unnamed and one line.
# Reserved word 'return' is not required.

my_lambda_funct = lambda a, b: a + b
result = my_lambda_funct(4, 6)
print(f'\n\tResult of the lambda function: {result}')

# Lambda functions doesn't require arguments.
my_lambda_funct = lambda : 'Function without arguments.'
print(f'\n\tCalling the lambda function without arguments: {my_lambda_funct()}')

# Lambda functions with default arguments.
my_lambda_funct = lambda a = 2, b = 3: a + b
print(f'\n\tResult of the default arguments: {my_lambda_funct()}')

# Lambda functions with variable arguments *args and **kwards.
my_lambda_funct = lambda *args, **kwargs : len(args) + len(kwargs)
print(f'\n\tResult of the default arguments: {my_lambda_funct()}')
print(f'\n\tResult of variable arguments: {my_lambda_funct(3, 2, 1, a = 12, b = 10)}')

# Lambda functions with args, variable args and default arguments.
my_lambda_funct = lambda a, b, c= 3, *args, **kwargs: a + b + c + len(args) + len(kwargs)
print(f'\n\tResult: {my_lambda_funct(3, 2, 3, 2, 1, e = 12, f = 10)}')

#-------------------------------------------------------------------

# Closure.

'''
def operation(a, b):
    def add():
        return a + b

    return add

my_func_closure = operation(5, 8)
# print(f'\n\tResult of closure function: {my_func_closure()}')
print(f'\n\tResult of closure function: {operation(5, 8)()}')
'''

# Closure and lambda functions.

def operation(a, b):
    return lambda: a + b

my_func_closure = operation(5, 8)
print(f'\n\tResult of closure - lambda: {my_func_closure()}')

#-------------------------------------------------------------------
