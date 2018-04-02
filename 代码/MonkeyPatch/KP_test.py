# coding=utf-8

from KP_test01 import Person
from KP_test02 import get_score

def monkeypaych():
    Person.get_score = get_score

monkeypaych()

if __name__ == '__main__':
    print(Person().get_score())