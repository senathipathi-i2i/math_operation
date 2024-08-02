import os

set_flag = os.environ.get('flag')

def add(a, b):
    if set_flag:
        return a + b
    else:
        print('Missing authentication token')
