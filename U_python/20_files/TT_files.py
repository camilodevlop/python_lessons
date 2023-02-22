# File management in Python.

try:
   file = open('mydata', 'w', encoding = 'utf8') 
   file.write('\n\tCamilo\n\tAlejandro\n\tInformación.\n')
except Exception as e:
    print(e)
finally:
    file.close()

#-------------------------------------------------------------------
