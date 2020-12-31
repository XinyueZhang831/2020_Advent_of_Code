import itertools
import re
import collections

def day16_1():
    with open('/Users/xinyue/Downloads/day16_1.txt', 'r') as file:
        input_file = file.read().split('\n\n')

    rules = input_file[0].split('\n')
    your_tickets = input_file[1].split('\n')
    nearby_tickets = input_file[2].split('\n')[1:-1]

    rules_dic = {}
    for i in rules:
        text = i.split(' ')
        rule_detail = ' '.join(text[:-3])[:-1]
        rule_1min = text[-3].split('-')[0]
        rule_1max = text[-3].split('-')[1]
        rule_2min = text[-1].split('-')[0]
        rule_2max = text[-1].split('-')[1]
        rules_dic[rule_detail] = {'min1':int(rule_1min),'max1':int(rule_1max),'min2':int(rule_2min), 'max2':int(rule_2max)}
    your_tickets_list = [int(i) for i in your_tickets[1].split(',')]


    total = 0
    for each_ticket in nearby_tickets:
        each_ticket_list = [int(i) for i in each_ticket.split(',')]
        for each_number in each_ticket_list:
            times = 0
            for k,v in rules_dic.items():
                if not ((v['min1'] <= each_number <= v['max1']) or (v['min2'] <= each_number <= v['max2'])):
                    times+=1
            if times == 20:
                total+=each_number

    print(total)


def day16_2():
    with open('/Users/xinyue/Downloads/day16_1.txt', 'r') as file:
        input_file = file.read().split('\n\n')

    rules = input_file[0].split('\n')
    your_tickets = input_file[1].split('\n')
    nearby_tickets = [[int(j) for j in i] for i in [k.split(',') for k in input_file[2].split('\n')[1:-1]]]


    rules_dic = {}
    for i in rules:
        text = i.split(' ')
        rule_detail = ' '.join(text[:-3])[:-1]
        rule_1min = text[-3].split('-')[0]
        rule_1max = text[-3].split('-')[1]
        rule_2min = text[-1].split('-')[0]
        rule_2max = text[-1].split('-')[1]
        rules_dic[rule_detail] = {'min1':int(rule_1min),'max1':int(rule_1max),'min2':int(rule_2min), 'max2':int(rule_2max)}
    your_tickets_list = [int(i) for i in your_tickets[1].split(',')]

    nearby_tickets_copy = nearby_tickets.copy()
    for each_ticket in nearby_tickets:
        for each_number in each_ticket:
            times = 0
            for k,v in rules_dic.items():
                if not ((v['min1'] <= each_number <= v['max1']) or (v['min2'] <= each_number <= v['max2'])):
                    times+=1
            if times == 20:
                nearby_tickets_copy.remove(each_ticket)
                break
        nearby_tickets = nearby_tickets_copy

    not_satisfy_the_rule = collections.defaultdict(set)
    transform_nearby = [[item[i] for item in nearby_tickets] for i in range(20)]

    for each_position in range(len(transform_nearby)):
        for each_number in transform_nearby[each_position]:
            for k, v in rules_dic.items():
                if not ((v['min1'] <= each_number <= v['max1']) or (v['min2'] <= each_number <= v['max2'])):
                    not_satisfy_the_rule[each_position].add(k)

    satisfy_the_rule = collections.defaultdict(set)
    for k,v in not_satisfy_the_rule.items():
        satisfy_the_rule[k] = set(list(rules_dic.keys()))-v

    result_dic = collections.defaultdict(list)
    while any([len(v1)>1 for k1,v1 in satisfy_the_rule.items()]):
        for k,v in satisfy_the_rule.items():
            if len(v) == 1:
                result_dic[list(v)[0]].append(k)
                discard_value = list(v)[0]
                break
        for k,v in satisfy_the_rule.items():
            if discard_value in v:
                satisfy_the_rule[k].remove(discard_value)

    print(your_tickets_list[result_dic['departure location'][0]]*\
          your_tickets_list[result_dic['departure station'][0]]*your_tickets_list[result_dic['departure platform'][0]]*\
          your_tickets_list[result_dic['departure track'][0]]*your_tickets_list[result_dic['departure date'][0]]*\
          your_tickets_list[result_dic['departure time'][0]])
