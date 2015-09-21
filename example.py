#! coding: utf-8
import random
from random import randint


def gen_random_numbers(n=100000, min_value=0, max_value=100):
    # random_numbers = []
    # for i in range(10):
    #     random_numbers.append(randint(min_value, max_value))
    random_numbers = [randint(min_value, max_value) for i in range(n)]
    return random_numbers

def sum_numbers(*numbers):
    negative_sum = 0
    positive_sum = 0
    for number in numbers:
        if number > 0:
            positive_sum += number
        else:
            negative_sum += number
    return sum(numbers), negative_sum, positive_sum

def sum_numbers_in_list(numbers):
    my_sum = 0
    for number in numbers:
        my_sum += number
    return my_sum

random_numbers = [1, 2, 3, 4]

kwargs = {'min_value': -1000, 'max_value': 1000}

numbers = gen_random_numbers(100000, **kwargs)
total_sum, negative_sum, positive_sum = sum_numbers(*numbers)
my_string = 'Visa suma: %d    neigiami: %d    teigiami: %d' % tuple([total_sum, negative_sum, positive_sum])
a_number = -123.734

# print(int(a_number))
# print(-7 / 3)
# svekųjų=-3 + liekana=2        -3 -3 -3 + 2 = 7

# python2   int / int -> sveikoji dalis
# python2   int % int -> liekana
# python2   float(int) / int -> sveikoji dalis
# python3   int / int ~ float(int) / float(int)    (sveikųjų skaičių dalyba)
# python3   int // int -> sveikoji dalis


def square_numbers_if_given(my_number=None):
    '''Return square of given number and None if number is not given'''
    if my_number is not None:
        return my_number**2
    return None

    # bool(''), bool("") == False

    # if numbers:  # numbers - listas
    #     # False if None
    #     # False if no elements
    #     return sum(numbers)


print(square_numbers_if_given(0))


