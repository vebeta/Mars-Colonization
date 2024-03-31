from requests import get, delete, post
from pprint import pprint


# pprint(get('http://localhost:5000/api/v2/users').json())
# print('-------------------------------------------------')
# pprint(get('http://localhost:5000/api/v2/users/1').json())
# print('-------------------------------------------------')
# pprint(get('http://localhost:5000/api/v2/users/999').json())
# print('-------------------------------------------------')
# #pprint(get('http://localhost:5000/api/v2/users/q').json())
#
# pprint(delete('http://localhost:5000/api/v2/users/2').json())
# print('-------------------------------------------------')
# pprint(get('http://localhost:5000/api/v2/users/2').json())

dat = {
       'name': 'Albert ',
       'surname': 'Einstein',
       'age': 76,
       'position': 'black holes expert',
       'speciality': 'just jenius',
       'address': 'sdfgsdfg',
       'email': 'albrt_gegdfgs@space.com',
       'hashed_pas': 'sdfgsdfg'}

pprint(post('http://localhost:5000/api/v2/users', json=dat).json())
print('-------------------------------------------------')
#pprint(get('http://localhost:5000/api/v2/users/5').json())
