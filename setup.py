from setuptools import setup, find_packages

setup(
    name='math_operations',
    version='0.1',
    packages=find_packages(),
    description='A package for basic arithmetic operations',
    author='senathipathi',
    author_email='senathipathi.vinayagam@ideas2it.com',
    url='https://github.com/senathipathi-i2i/math_operation',
    install_requires=[
        'python-dotenv',  # Required to load the .env file
    ],
    classifiers=[
        'Programming Language :: Python :: 3',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.6',
)
