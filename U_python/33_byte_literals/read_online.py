from urllib.request import urlopen, Request

print('\n\tReading online content.')

# Adding the User-Agent header to the request.
request = Request('http://globalmentoring.com.mx/recursos/GlobalMentoring.txt')
request.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.71 Safari/537.36')

message  = urlopen(request)
content = message.read().decode('UTF-8')

print('\tCounting the occurrences of \'Universidad\':', content.count('Universidad'))
print('\tConverting the text to uppercase:\n\t', content.count('Universidad'))

print(content.upper(), '\n\t')
print(content, '\n\t')
print(content.lower(), '\n\t')

# Searching a string.
print('\n\tSearching \'python\': ', 'python' in content)

# startswith
print('\n\tstartswith method: ', content.startswith('En GlobalMentoring.com.mx'))

# endswith
print('\n\tendswith method: ', content.endswith('Fundador de GlobalMentoring.com.mx'))

message = 'Hello World'
print(message.islower())
print(message.lower().islower())
print(message.isupper())
print(message.upper().isupper())

'''
# Recovering the words.
words = []
for line in message:
    words_per_line = line.decode('UTF-8').split()
    for word in words_per_line:
        words.append(word)

print(words)
'''

#-------------------------------------------------------------------

# Saving the content in a file.
#with open('new_file.txt', 'w', encoding = 'UTF-8') as file:
#    file.write(content)

#-------------------------------------------------------------------
