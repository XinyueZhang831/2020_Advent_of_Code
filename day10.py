import itertools
import collections
import re

def day10_1():
    with open('/Users/xinyue/Downloads/day10_1.txt', 'r') as file:
        input_file = file.read().split('\n')
    input_file.remove('')
    input_file = [int(i) for i in input_file]+[0]
    sorted_file = sorted(input_file)
    sorted_file = sorted_file+[max(sorted_file)+3]


    counter_dic = collections.defaultdict(int)
    for i in range(len(sorted_file)-1):

        if sorted_file[i+1] - sorted_file[i] == 1:
            counter_dic['1'] +=1
        elif sorted_file[i+1] - sorted_file[i] == 3:
            counter_dic['3'] += 1
        elif sorted_file[i+1] - sorted_file[i]>3:
            break

    print(counter_dic['1']*counter_dic['3'])



def day10_2():
    with open('/Users/xinyue/Downloads/day10_1.txt', 'r') as file:
        input_file = file.read().split('\n')
    input_file.remove('')
    input_file = [int(i) for i in input_file]+[0]
    sorted_file = sorted(input_file)
    sorted_file = sorted_file+[max(sorted_file)+3]

    repeat_part = {}
    def counter_times(position):
        if position in repeat_part.keys():
            return repeat_part[position]

        if position == len(sorted_file)-1:
            return 1

        current_subways = 0

        if (position+1<len(sorted_file)):
            if(sorted_file[position+1] -sorted_file[position] <=3):
                current_subways += counter_times(position+1)
        if (position+2<len(sorted_file)):
            if (sorted_file[position+2] -sorted_file[position] <=3):
                current_subways += counter_times(position+2)
        if (position+3<len(sorted_file)):
            if (sorted_file[position+3] -sorted_file[position] <=3):
                current_subways += counter_times(position+3)

        repeat_part[position] = current_subways
        return current_subways


    print(counter_times(0))
