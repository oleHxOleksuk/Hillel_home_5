import keyword
import string
from operator import index

name = input('Введіть імя змінної: ')

if name in keyword.kwlist:
    print(False)
elif name[0].isdigit():
    print(False)
elif string.punctuation in index(name):
    print('klhklh')
else:
    print(True)