# Stages of life by age.
print('\n\tStages of life by age.\n')
age = int(input('\tEnter the age: '))
prompt = ''

if (age>=0 and age<10):
    prompt = 'the childhood is beautiful.'
elif (age>=10 and age<20):
    prompt = 'many changes and study.'
elif (age>=20 and age<30):
    prompt = 'love appears and work begins.'
else:
    prompt = 'The age is not valid.'

print(f'\tAge {age}: {prompt}')

#-------------------------------------------------------------------

# Rating system.
print('\n\tRating system.\n')
rating = float(input('\tPlease enter the rating: '))
prompt2 = ''

if (rating>=9 and rating<=10):
    prompt2 = 'A'
elif (rating>=8 and rating<9):
    prompt2 = 'B'
elif (rating>=7 and rating<8):
    prompt2 = 'C'
elif (rating>=6 and rating<7):
    prompt2 = 'D'
elif (rating>=0 and rating<6):
    prompt2 = 'F'
else:
    prompt2 = 'The value is not valid.'

print(f'\tRating {rating}-> {prompt2}')

#-------------------------------------------------------------------
