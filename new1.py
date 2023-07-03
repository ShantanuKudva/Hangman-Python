import logging


# def outer():
#     count = 0
#     def inner():
#         nonlocal count
#         count+=1
#         return count
#
#     return inner
#
# inner_func=outer()
# print(inner_func())
# print(inner_func())
# print(inner_func())
# print(inner_func())
import argparse
#
# parser = argparse.ArgumentParser(
#     # description="This program lets me print the name of my dogs"
# )
#
# parser.add_argument('-c', '--color', metavar='color', required=True, choices=['red', 'yellow'])
#
# args = parser.parse_args()
#
#
# print(args.color)

# lambda num: num*2
# from functools import reduce
#
# numbers = [1,2,3,4,6,7,3]
# exp = [
#     ('car', 20, 'expense1', 10000),
#     ('car', 20, 'expense2', 10000),
#     ('car', 20, 'expense2', 10000),
#     ('car', 20, 'expense2', 10000),
# ]
#
# multiplied = list(map(lambda a: a*2, numbers))
#
# isEven = list(filter(lambda a: a%2==0, numbers))
#
# reduced = (reduce(lambda a,b:a+b[3], exp, 0))
#
# print(reduced, isEven, multiplied, numbers)
#
# def factorial(n):
#     if n==1: return 1
#     return n * factorial(n-1)
#
# print(factorial(3))

# def fib(n):
#     sequence = [0,1]
#     while len(sequence)<=n:
#         next_sequence = sequence[-1]+sequence[-2]
#         sequence.append(next_sequence)
#     return sequence
#
# print(fib(10))

def greet(fx):
    def mfx(*args, **kwargs):
        print("Good morning!")
        logging.info(f"calling funtion {fx.__name__} with args={args} and kwargs = {kwargs}")
        fx(*args, **kwargs)
        print("Have a good day")
    return mfx


#
@greet
def sum(a,b):
    print(a+b)

# def printWord(text):
#     print(text)
#
# greet(printWord)("text")
# sum(1,2)
#

def print_person_details(**kwargs):
    print(list(kwargs.values()), list(kwargs.keys()))
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_person_details(name="Alice", age=25, city="New York")


