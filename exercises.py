# Exercise 1: Create a list, tuple, float, integer, decimal, and dictionary.

from decimal import Decimal

my_list = ['Microsoft', 'Samsung', 'Sony', 'Apple', 'HP']
my_tuple = ('alfa', 'beta', 'gamma', 'delta')
my_float = 3.14
my_integer = 47
my_decimal = Decimal(1.3)
my_dictionary = {'first': 'ONE', 'second': 'TWO', 'third': 'THREE'}

print(f'Exercise 1\t{my_list}\n\t\t\t{my_tuple}\n\t\t\t{my_float}\n\t\t\t{my_integer}\n\t\t\t{my_decimal}\n\t\t\t{my_dictionary}\n')



# Exercise 2: Round your float up.

import math

rounded_float = math.ceil(my_float)

print(f'Exercise 2:\t{rounded_float}\n')



# Exercise 3: Get the square root of your float.

square_root = math.sqrt(my_float)

print(f'Exercise 3:\t{square_root}\n')



# Exercise 4: Select the first element from your dictionary.

first_element = list(my_dictionary.items())[0]

print(f'Exercise 4:\t{first_element}\n')



# Exercise 5: Select the second element from your tuple.

second_element = my_tuple[1]

print(f'Exercise 5:\t{second_element}\n')



# Exercise 6: Add an element to the end of your list.

my_list.append('Asus')

print(f'Exercise 6:\t{my_list}\n')



# Exercise 7: Replace the first element in your list.

my_list[0] = 'Lenovo'

print(f'Exercise 7:\t{my_list}\n')



# Exercise 8: Sort your list alphabetically.

my_list.sort()

print(f'Exercise 8:\t{my_list}\n')



# Exercise 9: Use reassignment to add an element to your tuple.

my_tuple += ('epsilon',)

print(f'Exercise 9:\t{my_tuple}')