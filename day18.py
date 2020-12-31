import itertools
import re
import collections


def day18_1():
    with open('/Users/xinyue/Downloads/day18_1.txt', 'r') as file:
        input_file = file.read().split('\n')

    new_input = []
    for i in input_file[:-1]:
        current_item = [j for j in i]
        current_item.insert(len(current_item), ')')
        current_item.insert(0,'(')
        while ' ' in current_item:
            current_item.remove(' ')
        new_input.append(current_item)

    overall_result = 0
    for each_line in new_input:
        current_signlist = []
        for i in range(len(each_line)):
            if each_line[i] == '(':
                current_signlist.append(i)
            elif each_line[i] == ')':
                close_left = current_signlist[-1]
                current_signlist.remove(close_left)
                close_right = i
                current_result = 0
                current_sign_sublist = '+'
                for each_subchar in each_line[close_left+1:close_right]:
                    if each_subchar.isdigit():
                        if current_sign_sublist =='+':
                            current_result += int(each_subchar)
                        else:
                            current_result*=int(each_subchar)
                    else:
                        if each_subchar!='':
                            current_sign_sublist = each_subchar
                each_line[close_left] = str(current_result)
                for j in range(close_left+1,close_right+1):
                    each_line[j] = ''
        overall_result +=int(each_line[0])
    print(overall_result)


def day18_2():
    with open('/Users/xinyue/Downloads/day18_1.txt', 'r') as file:
        input_file = file.read().split('\n')

    new_input = []
    for i in input_file[:-1]:
        current_item = [j for j in i]
        current_item.insert(len(current_item), ')')
        current_item.insert(0,'(')
        while ' ' in current_item:
            current_item.remove(' ')
        new_input.append(current_item)

    overall_result = 0
    for each_line in new_input:
        current_signlist = []
        for i in range(len(each_line)):
            if each_line[i] == '(':
                current_signlist.append(i)
            elif each_line[i] == ')':
                close_left = current_signlist[-1]
                current_signlist.remove(close_left)
                close_right = i
                counter = 0
                while '+' in each_line[close_left+1:close_right]:
                    if each_line[close_left+1:close_right][counter].isdigit():
                        last_digit_pos = counter
                    elif each_line[close_left+1:close_right][counter] == '+':
                        each_line[close_left + 1+counter + 1] = str(int(each_line[close_left+1:close_right][last_digit_pos]) + int(each_line[close_left+1:close_right][counter+1]))
                        each_line[close_left + 1+last_digit_pos] = ''
                        each_line[close_left + 1+counter] = ''
                    counter+=1
                print(each_line[close_left+1:close_right])
                current_result = 0
                current_sign_sublist = '+'
                for each_subchar in each_line[close_left + 1:close_right]:
                    if each_subchar.isdigit():
                        if current_sign_sublist == '+':
                            current_result += int(each_subchar)
                        else:
                            current_result *= int(each_subchar)
                    else:
                        if each_subchar != '':
                            current_sign_sublist = each_subchar
                each_line[close_left] = str(current_result)
                for j in range(close_left + 1, close_right + 1):
                    each_line[j] = ''
        while ''in each_line:
            each_line.remove('')
        overall_result += int(each_line[0])
    print(overall_result)
