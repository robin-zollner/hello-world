import pandas as pd
import matplotlib.pyplot as plt
person = {
    'name': {
        'firstName': ['Rob', 'Dianne', 'George'],
        'lastName': ['Zollner','Fischer','Leopard'],
        },
    'age': [25, 78, 63],
    'occupation': {
        'jobTitle': ['engineer', 'programmer', 'manager'],
        'salary':[86000, 250000, 75000]
        },
    'interests': {
        'food':['kiwi', 'pizza', 'sushi'],
        'music':['rock', 'classical', 'vapor-wave']
        }
    }

person['id'] = [i for i in range(len(person['name']['firstName']))]
print(person)
