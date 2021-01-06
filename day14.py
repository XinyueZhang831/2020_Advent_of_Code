import itertools
import collections
import re


def day14_1():
    with open('/Users/xinyue/Downloads/day14_1.txt', 'r') as file:
        input_file = file.read().split('\n')

    current_list=[]
    for i in input_file:
        if 'mask' in i:
            text = i.split(' = ')
            current_list.append(text[1])
        if 'mem' in i:
            text = re.findall("\[([0-9_]+)\]", i)[0]
            text1 = i.split(' = ')[1]
            current_list.append((text,text1))

    memory_dic = {}
    current_mask = ''
    for i in current_list:
        if isinstance(i,str):
            current_mask = i
        else:
            position = i[0]
            number = str(bin(int(i[1]))[2:].zfill(len(current_mask)))
            for j in range(len(number)):
                number = list(number)
                if current_mask[j] == '0':
                    number[j] = '0'
                elif current_mask[j] == '1':
                    number[j] = '1'
                number = ''.join(number)
            memory_dic[position] = number

    total = 0
    for k,v in memory_dic.items():
        current_number = int(v, 2)
        total+=current_number
    print(total)


def day14_2():
    with open('/Users/xinyue/Downloads/day14_1.txt', 'r') as file:
        input_file = file.read().split('\n')

    current_list=[]
    for i in input_file:
        if 'mask' in i:
            text = i.split(' = ')
            current_list.append(text[1])
        if 'mem' in i:
            text = re.findall("\[([0-9_]+)\]", i)[0]
            text1 = i.split(' = ')[1]
            current_list.append((text,text1))


    def find_result(current_bin):

        if 'X' not in current_bin:
            return current_bin

        result_bin = ''
        current_X = current_bin.index('X')

        current_bin_0 = list(current_bin)
        current_bin_1 = list(current_bin)
        current_bin_0[current_X] = '0'
        current_bin_1[current_X] = '1'
        current_bin_0 = ''.join(current_bin_0)
        current_bin_1 = ''.join(current_bin_1)

        result_bin +=find_result(current_bin_0)+','
        result_bin += find_result(current_bin_1)
        return result_bin

    memory_dic = {}
    current_mask = ''
    for i in current_list:
        if isinstance(i, str):
            current_mask = i
        else:
            value = int(i[1])

            number = str(bin(int(i[0]))[2:].zfill(len(current_mask)))
            number = list(number)
            for j in range(len(number)):
                if current_mask[j] == '0':
                    pass
                elif current_mask[j] == '1':
                    number[j] = '1'
                else:
                    number[j] = 'X'
            number = ''.join(number)
            memory_location = find_result(number).split(',')
            for each_location in memory_location:
                each_location = int(each_location,2)
                memory_dic[each_location] = value

    total = 0
    for k,v in memory_dic.items():
        total+=v
    print(total)
