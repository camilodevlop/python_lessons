# Use of 'with' in Python. 'with' opens and closes the files
# automatically.

from file_management import File_Management

#with open('mydata', 'r', encoding = 'utf8') as file:
with File_Management('mydata') as file:
    print(file.read())

#-------------------------------------------------------------------
