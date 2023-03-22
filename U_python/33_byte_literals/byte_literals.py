from urllib import urlopen

# Byte characters.

print('\n\tByte characters.')
byte_chars = b'Hello World.'
print(f'\t{byte_chars}')

message = b'Python University.'
print(f'\t{message[0]}, {chr(message[0])}')

chars_list = message.split()
print(f'\t{chars_list}')

#-------------------------------------------------------------------

# Str to Bytes convertion.

print('\n\tStr to Bytes convertion.')
string = 'Python programming'
print('\tOriginal string: ', string)
byte = string.encode('UTF-8')
print(f'\tEncoded byte: ', byte)

# Bytes to Str convertion.

print('\n\tBytes to Str convertion.')
string2 = byte.decode('UTF-8')
print(f'\tDecoded string: ', string2)

#-------------------------------------------------------------------

# Reading online content.

print('\n\tReading online content.')

#-------------------------------------------------------------------
