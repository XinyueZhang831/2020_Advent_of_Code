import itertools
import re

def day9_1():
    with open('/Users/xinyue/Downloads/day9_1.txt', 'r') as file:
        number_list =[int(i) for i in file.read().split('\n') if i!= '']

    for i in range(25, len(number_list)):
        if number_list[i] not in [i[0]+i[1] for i in list(itertools.combinations(number_list[i-25: i+1],2))]:
            return number_list[i]


def day9_2():
    with open('/Users/xinyue/Downloads/day9_1.txt', 'r') as file:
        number_list =[int(i) for i in file.read().split('\n') if i!= '']

    wrong_number = day9_1()
    for i in range(len(number_list)):
        if sum(number_list[:i])>wrong_number:
            current_number_position = i
            break

    for i in range(len(number_list)-current_number_position):
        start_point = 0
        while True:
            current_sum = sum(number_list[start_point: current_number_position+i])

            if current_sum< wrong_number:
                break
            elif (current_sum == wrong_number) &(len(number_list[start_point: current_number_position+i])>1):
                weakness_number = max(number_list[start_point: current_number_position+i])+min(number_list[start_point: current_number_position+i])
                print(weakness_number)
                break
            else:
                start_point+=1
