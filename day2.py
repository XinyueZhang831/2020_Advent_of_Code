import itertools
import re

def day2_1():
    with open('/Users/xinyue/Downloads/day2_1.txt', 'r') as file:
        password_list = [i for i in file.readlines()]
    counter = 0
    for i in password_list:
        min_req = int(i.split('-')[0])
        max_req = int(i.split('-')[1].split(' ')[0])
        letter_req = i.split('-')[1].split(' ')[1].split(':')[0]
        password = i.split(':')[1]
        if (min_req<= password.count(letter_req)) and (max_req>= password.count(letter_req)):
            counter +=1
    print(counter)


def day2_2():
    with open('/Users/xinyue/Downloads/day2_1.txt', 'r') as file:
        password_list = [i for i in file.readlines()]
    counter = 0
    for i in password_list:
        numbers = [int(n) for n in re.findall(r'\b\d+\b',i)]
        letters = re.findall("[a-zA-Z]+", i)
        if letters[1][numbers[0]-1]!= letters[1][numbers[1]-1]:
            if ((letters[1][numbers[0]-1] == letters[0]) or (letters[1][numbers[1]-1] == letters[0])):
                counter += 1
    print(counter)
