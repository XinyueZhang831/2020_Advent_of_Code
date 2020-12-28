import itertools
import re


def day8_1():
    with open('/Users/xinyue/Downloads/day8_1.txt', 'r') as file:
       operation_list = [(i.replace('\n','').split(' ')[0],int(i.replace('\n','').split(' ')[1])) for i in file.readlines()]

    accumulate_result = 0

    passed_opt = []
    opt_position = 0
    while opt_position not in passed_opt:
        opt = operation_list[opt_position][0]
        passed_opt.append(opt_position)
        if opt == 'acc':
            accumulate_result += operation_list[opt_position][1]
            opt_position += 1
        elif opt == 'nop':
            opt_position += 1
        elif opt =='jmp':
            opt_position += operation_list[opt_position][1]


def day8_2():
    with open('/Users/xinyue/Downloads/day8_1.txt', 'r') as file:
       operation_list = [(i.replace('\n','').split(' ')[0],int(i.replace('\n','').split(' ')[1])) for i in file.readlines()]

    nop_jmp_list = [i for i in range(len(operation_list)) if (operation_list[i][0] == 'nop') or(operation_list[i][0] == 'jmp')]

    for i in nop_jmp_list:

        accumulate_result = 0
        opt_position = 0
        passed_opt = []
        operation_list_copy = operation_list.copy()

        if operation_list[i][0] == 'nop':
            operation_list_copy[i] = ('jmp', operation_list[i][1])
        elif operation_list[i][0] == 'jmp':
            operation_list_copy[i] = ('nop', operation_list[i][1])
        while opt_position not in passed_opt:
            if opt_position == len(operation_list_copy):
                print(accumulate_result)
                break
            opt = operation_list_copy[opt_position][0]
            passed_opt.append(opt_position)
            if opt == 'acc':
                accumulate_result += operation_list_copy[opt_position][1]
                opt_position += 1
            elif opt == 'nop':
                opt_position += 1
            elif opt == 'jmp':
                opt_position += operation_list_copy[opt_position][1]
