import itertools
import re

def day1_1():
    with open('/Users/xinyue/Downloads/input.txt','r') as file:
        number_list = [int(i)for i in file.readlines()]
    if len(number_list)>1:
        for numbers in itertools.combinations(number_list, 2):
            if sum(numbers) == 2020:
                print(numbers)
                print(numbers[0]*numbers[1])


def day1_2():
    with open('/Users/xinyue/Downloads/input.txt','r') as file:
        number_list = [int(i)for i in file.readlines()]

    if len(number_list)>1:
        for numbers in itertools.combinations(number_list, 3):
            if sum(numbers) == 2020:
                print(numbers)
                print(numbers[0]*numbers[1]*numbers[2])


