# Reading a file in Python.

file = open('mydata', 'r', encoding = 'utf8')

#print(file.read())         # Reading all the file.

#print(file.read(5))        # Reading parts of the file.
#print(file.read(10))

#print(file.readline())     # Reading lines of the file.
#print(file.readline())
#print(file.readline())

''' Printing characters separately.
for line in file:
    #print(line)
    for char in line:
        print(char, end = ' ')
'''

#print(file.readlines())        # Reading lines
#print(file.readlines()[0:2])    #Accessing a line in the list.

# New file: 'a' append information.
file2 = open('mydata2', 'a', encoding = 'utf8')
for line in file:
    for char in line:
        file2.write(f'{char}   ')

# file2.write(file.read())

file.close()
file2.close()

#-------------------------------------------------------------------
