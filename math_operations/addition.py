import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def add(a, b):
    # Retrieve the 'flag' environment variable
    set_flag = os.environ.get('flag')

    if set_flag == 'True':
        return a + b
    else:
        print('Missing authentication token')
