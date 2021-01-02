''' fully credit to anthonywritescode'''
''' day19_x is n unefficient way to do this question'''

import itertools
import collections
import re

def day19_1():
    with open('/Users/xinyue/Downloads/day19_1.txt','r') as file:
        input_file = file.read().split('\n\n')

    rules_dic = {}
    for i in input_file[0].split('\n'):
        text = i.split(': ')
        while '"' in text[1]:
            text[1] = text[1].replace('"','')
        rules_dic[text[0]] = text[1]

    result_list = input_file[1].split('\n')

    def find_result(key):
        current_rule = rules_dic[key]

        if current_rule.islower():
            return current_rule
        else:
            break_rules = current_rule.split(' ')
            return_part = ''.join('|' if item == '|' else find_result(item) for item in break_rules)
            return '('+return_part+')'

    solve_question = re.compile(find_result('0'))
    counter = 0
    for each_result in result_list:
        if solve_question.fullmatch(each_result):
            counter+=1
    print(counter)


def day19_2():
    with open('/Users/xinyue/Downloads/day19_1.txt','r') as file:
        input_file = file.read().split('\n\n')

    rules_dic = {}
    for i in input_file[0].split('\n'):
        text = i.split(': ')
        while '"' in text[1]:
            text[1] = text[1].replace('"','')
        rules_dic[text[0]] = text[1]

    def find_result(key):
        current_rule = rules_dic[key]

        if current_rule.islower():
            return current_rule
        else:
            break_rules = current_rule.split(' ')
            return_part = ''.join('|' if item == '|' else find_result(item) for item in break_rules)
            return '(' + return_part + ')'

    result_list = input_file[1].split('\n')

    result_42 = re.compile(find_result('42'))
    result_31 = re.compile(find_result('31'))
    counter = 0



    for each_result in result_list:
        end_position = 0
        counter_42 = 0
        match = result_42.match(each_result, end_position)
        while match:
            counter_42 +=1
            end_position = match.end()
            match = result_42.match(each_result, end_position)

        counter_31 = 0
        match = result_31.match(each_result, end_position)
        while match:
            counter_31 += 1
            end_position = match.end()
            match = result_31.match(each_result, end_position)

        if end_position == len(each_result) and 0<counter_31<counter_42:
            counter +=1
    print(counter)
    
    
 
 
 
def day19_x():
    with open('/Users/xinyue/Downloads/day19_1.txt','r') as file:
        input_file = file.read().split('\n\n')

    rules_dic = collections.defaultdict(list)
    for i in input_file[0].split('\n'):
        text = i.split(':')
        split_rest = text[1].split('|')
        for j in split_rest:
            text_sub = j.split(' ')
            while ''in text_sub:
                text_sub.remove("")
            if '\"' in text_sub[0]:
                text_sub[0] = text_sub[0].replace('\"', '')
            tuple_list = text_sub
            rules_dic[text[0]].append(tuple_list)



    def combination_eachpart(part1,part2):
        ret = []
        for i in part1:
            for j in part2:
                ret.append(i+j)
        return ret

    start_0 = '0'

    def find_base(start_0):
        current_rule= rules_dic[start_0]

        while True:
            if any([item1.isdigit() for item in current_rule for item1 in item]):
                current_rule_copy=[]
                for i in current_rule:
                    partial_result = []
                    for j in i:
                        if (j!= 'a' )and (j!='b'):
                            new_part = rules_dic[j]
                            if (len(new_part) >= 1) and (len(partial_result) > 0):
                                partial_result = combination_eachpart(partial_result, new_part)
                            elif (len(new_part) > 1) and (len(partial_result) == 0):
                                partial_result = new_part
                            else:
                                partial_result.append(new_part[0])
                        else:
                            for each_current in range(len(partial_result)):
                                partial_result[each_current].extend(j)

                        for each_list in partial_result:
                            current_rule_copy.append(each_list)
                        current_rule = current_rule_copy
            else:
                return current_rule



    result = find_base(start_0)
    counter = 0
    for i in result:
        item = ''.join(i)
        if item in input_file[1].split('\n'):
            counter+=1
    print(counter)
