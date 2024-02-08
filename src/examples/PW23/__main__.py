from random import randint
from src.open_tasks import open_it
import os


def first_task():
    s = list (input () )
    for c in s:
        if 'a' <= c <= 'z':
            n =ord('a') +(ord(c) - ord('a') +1) % 26
            print ( chr (n) , end='' )
        elif 'A' <= c <= 'Z':
            n =ord('A') +(ord(c) - ord('A') +1)% 26
            print ( chr (n), end='' )
    else:
        print ( c, end='' )

def second_task():
    intab = "aeiou"
    outtab ="12345"
    trantab = str.maketrans (intab, outtab)
    str = "this is string example .... wow !!! "
    print (str.translate (trantab))


def third_task():
    ALPHA = u'абвгґдеєжзиїїйклмнопрстуфхцчшщьюя'
    def encode(text, step):
        return text.translate(
         str.maketrans(ALPHA, ALPHA[step:] + ALPHA[:step]))

    def decode(text, step):
        return text.translate(
         str.maketrans( ALPHA[step:] + ALPHA[:step], ALPHA))

    a = input()
    print (encode(a, 1))

try:
    open_it(str(os.path.relpath(__file__)))
except Exception as e:
    print(f"У вас помилка: {e}")
