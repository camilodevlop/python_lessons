# Exceptions in Python.

from TT_exception_equal import Equal_Number_Exception


result = None

try:
    a = int(input('\n\tType the first number: '))
    b = int(input('\tType the second number: '))

    if a == b:
        raise Equal_Number_Exception(' equal numbers.\n')

    result = a / b

except ZeroDivisionError as e:
    print(f'\n\tZeroDivisionError - Something went wrong: {e}, {type(e)}\n')
except TypeError as e:
    print(f'\n\tTypeError - Something went wrong: {e}, {type(e)}\n')
except Exception as e:
    print(f'\n\tException - Something went wrong: {e}, {type(e)}\n')
except BaseException as e:
    print(f'\n\tBaseException - Something went wrong: {e}, {type(e)}\n')
else:
    print(f'\n\telse: this block is activated when no exception is caught.')
finally:
    print(f'\tfinally: this block always is activated.')

print(f'\n\tResult: {result}\n\tContinue...\n')

#-------------------------------------------------------------------
