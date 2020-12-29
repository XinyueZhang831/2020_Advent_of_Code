''' day15_3 is a more efficient method than day15_2, credit to anthonywritescode '''
''' day15_2 runs 8.5 mins, day15_3 runs 31.355s '''

import itertools
import re
import collections

def day15_1():
    input_list = [0,8,15,2,12,1,4]
    number_dic = {}
    for i in range(0,len(input_list)):
        number_dic[input_list[i]] = [i+1]

    last_number = input_list[-1]
    for i in range(len(input_list)+1,2021):
        if ((last_number in number_dic.keys()) and (len(number_dic[last_number]) == 1)) or (last_number not in number_dic.keys()):
            last_number = 0
        elif (last_number in number_dic.keys()) and (len(number_dic[last_number]) > 1):
            last_number = number_dic[last_number][-1]-number_dic[last_number][-2]
        if last_number not in number_dic.keys():
            number_dic[last_number]= []
        number_dic[last_number]+=[i]
    print(last_number)


def day15_2():
    input_list = [0,8,15,2,12,1,4]
    number_dic = {}
    for i in range(0,len(input_list)):
        number_dic[input_list[i]] = [i+1]

    last_number = input_list[-1]
    for i in range(len(input_list)+1,30000001):
        print(i)
        if last_number in number_dic.keys():
            if len(number_dic[last_number]) == 1:
                last_number = 0
            elif len(number_dic[last_number]) > 1:
                last_number = number_dic[last_number][-1]-number_dic[last_number][-2]
        if last_number not in number_dic.keys():
            last_number = 0
            number_dic[last_number]= []
        number_dic[last_number] += [i]
        if len(number_dic[last_number])>2:
            number_dic[last_number].pop(0)
    print(last_number)


def day15_3():
    list_1 = [0,8,15,2,12,1,4]
    number_dic = collections.defaultdict(list)
    for i in range(0,len(list_1)):
        number_dic[list_1[i]] = [i+1]

    last_number = list_1[-1]
    for i in range(len(list_1) + 1, 30000001):
        if len(number_dic[last_number]) <= 1:
            last_number = 0
        else:
            last_number = number_dic[last_number][-1] - number_dic[last_number][-2]
        number_dic[last_number].append(i)
        if len(number_dic[last_number]) > 2:
            number_dic[last_number].pop(0)
    print(last_number)
