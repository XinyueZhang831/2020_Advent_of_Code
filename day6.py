import itertools
import re

def day6_1():
    with open('/Users/xinyue/Downloads/day6_1.txt', 'r') as file:
        file = file.read()

    counter = 0
    for each_group in file.split('\n\n'):
        yes_set = set()
        for each_letter in each_group:
            if each_letter != '\n':
                yes_set.add(each_letter)
        counter +=len(yes_set)
    print(counter)


def day6_2():
    with open('/Users/xinyue/Downloads/day6_1.txt', 'r') as file:
        file = file.read()

    counter = 0
    for each_group in file.split('\n\n'):
        yes_set = {}
        for each_person in each_group.split('\n'):
            for each_anwser in each_person:
                if each_anwser in yes_set.keys():
                    yes_set[each_anwser] +=1
                else:
                    yes_set[each_anwser] = 1
        clean_list = each_group.split('\n')
        
        try:
            clean_list.remove('')
        except:
            pass

        for k,v in yes_set.items():
            if v == len(clean_list):
                counter+=1
    print(counter)
