# Exercise: recursive functions.
print('\n\tPrint a number in descending order.')
def number_descending(num):
    if (num >= 1):
        print(f'\t{num}')
        number_descending(num-1)

number_descending(5)

#-------------------------------------------------------------------

# Tax calculator.
print('\n\n\tTax calculator.')
def tax_calculator(tfp = 0, t = 0):
    return tfp + tfp * (t/100)

tax_free_payment = float(input('\n\tEnter the tax-free payment: '))
tax = float(input('\tEnter the tax: '))

print(f'\tPayment(including taxes): {tax_calculator(tax_free_payment, tax)}')

#-------------------------------------------------------------------

# Temperature converter.
print('\n\tTemperature converter.')

def celsius_fahrenheit(temp = 0.0):
    if temp >= -273:
        return (temp*1.8) + 32
    else:
        return '\n\tThe temperature is invalid.'

def fahrenheit_celsius(temp = -32.0):
    if temp >= -459:
        return (temp-32) / 1.8
    else:
        return '\n\tThe temperature is invalid.'

celsius = float(input('\n\tInput the temp - Celsius degrees: '))
print(f'\tCelsius = {celsius} to Fahrenheit = {celsius_fahrenheit(celsius)}')

fahrenheit = float(input('\tInput the temp - Fahrenheit degrees: '))
print(f'\tFahrenheit = {fahrenheit} to Celsius = {fahrenheit_celsius(fahrenheit):.2f}\n')

#-------------------------------------------------------------------
