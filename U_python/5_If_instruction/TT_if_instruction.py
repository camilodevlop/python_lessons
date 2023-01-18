# Number to text conversion. 
print('\n\tNumber to text conversion.\n')
num = int(input('\tEnter a number between 1 and 3: '))

if (num == 1):
    num = 'One'
    print(f'\tThe number is: {num}')
elif (num == 2):
    num = 'Two'
    print(f'\tThe number is: {num}')
elif (num == 3):
    num = 'Three'
    print(f'\tThe number is: {num}')
else:
    print(f'\tThe number was not converted.')

#--------------------------------------------------------------------

# Calculating the year season.
print('\n\tCalculating the year season.')
month = int(input('\tEnter the month (1 and 12): '))

if (month==12 or month==1 or month==2):
    print(f'\tSeason: winter.')
elif (month==3 or month==4 or month==5):
    print(f'\tSeason: spring.')
elif (month==6 or month==7 or month==8):
    print(f'\tSeason: summer.')
elif (month==9 or month==10 or month==11):
    print(f'\tSeason: fall.')
else:
    print(f'\tThe month is not valid.')

#--------------------------------------------------------------------




#--------------------------------------------------------------------
