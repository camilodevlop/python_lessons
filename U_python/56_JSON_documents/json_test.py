# Reading JSON files. 
# JavaScript Object Notation (JSON).

import urllib.request
import json

'''
rqst = urllib.request.Request(
    'http://globalmentoring.com.mx/api/personas.json',
    data = None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
    )

answer = urllib.request.urlopen(rqst)
print(answer)
resp_rqst = answer.read()
print(resp_rqst)

# Processing the response.
json_answer = json.loads(resp_rqst.decode('utf-8'))
print('\n\n\t', json_answer, '\n\n')

# JSON is converted to lists and dictionaries in Python.
for person in json_answer['personas']:
    print(f'\tPersona: {person["nombre"]} {person["edad"]}')

# Accessing the independent variables.
print(json_answer['total'])
print(json_answer['mensaje'])
'''
#-------------------------------------------------------------------

# Requesting the weather.

weather_st = urllib.request.Request(
    'http://globalmentoring.com.mx/api/clima.json',
    data = None,
    headers={
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'
    }
    )

weather = urllib.request.urlopen(weather_st)
print(weather)
wthr = weather.read()
print(wthr)

# Processing the response.
json_weather = json.loads(wthr.decode('utf-8'))
print('\n\n\t', json_weather, '\n\n')

# Retrieving the weather description list.
weather_dict = json_weather['clima'][0]
print('\n\tWeather:\n\tDescription:', weather_dict.get('descripcion'))
# Retrieving the main data.
data_dict = json_weather['principal']
print('\ttemp_min:', data_dict.get('temp_min'), '\ttemp_max:', data_dict.get('temp_max'))

#-------------------------------------------------------------------
