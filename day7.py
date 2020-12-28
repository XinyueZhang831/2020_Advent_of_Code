import itertools
import re

def day7_1():
    with open('/Users/xinyue/Downloads/day7_1.txt', 'r') as file:
        file = file.read()
    file = file.split('\n')
    file.remove('')
    bag_dic = {}
    for each_rule in file:
        sub_bag = []
        main_bag = each_rule.split('contain')[0].replace(' bags ', '')
        for each_subbag in each_rule.split('contain')[1].split(','):
            sub_bag.append(' '.join(each_subbag.split(' ')[:-1]).lstrip())
        bag_dic[main_bag] = sub_bag

    def check_color(contain_gold_shiny):
        contain_gold_shiny_copy = contain_gold_shiny.copy()
        for k,v in bag_dic.items():
            for i in v:
                for each_color in contain_gold_shiny:
                    if each_color in i:
                        contain_gold_shiny_copy.add(k)
        return contain_gold_shiny_copy

    contain_gold_shiny ={'shiny gold'}
    while True:
        old_len = len(contain_gold_shiny)
        contain_gold_shiny = check_color(contain_gold_shiny)
        new_len = len(contain_gold_shiny)
        if old_len ==new_len:
            break

def day7_2():
    with open('/Users/xinyue/Downloads/day7_1.txt', 'r') as file:
        file = file.read()
    file = file.split('\n')
    file.remove('')
    bag_dic = {}
    for each_rule in file:
        sub_bag = {}
        main_bag = each_rule.split('contain')[0].replace(' bags ', '')
        for each_subbag in each_rule.split('contain')[1].split(','):
            each_subbag = each_subbag.lstrip()
            each_subbag = each_subbag.replace(' bags', '')
            each_subbag = each_subbag.replace(' bag', '')
            each_subbag = each_subbag.replace('.', '')
            number_bag = re.findall('[0-9]+', each_subbag)
            if len(number_bag) > 0:
                number_bag = number_bag[0]
            else:
                number_bag = '0'
            color_name = each_subbag.replace(number_bag, '')
            sub_bag[color_name.lstrip()] = int(number_bag)
        bag_dic[main_bag] = sub_bag

    def check_color(color_check):
        if color_check =='no other':
            current_bag_list = {}
        else:
            current_bag_list = bag_dic[color_check].copy()
        base_number = 0
        while len(current_bag_list)>0:
            key, value = current_bag_list.popitem()
            number = check_color(key)
            base_number = value + value*number+base_number
        return base_number




    print(check_color('shiny gold'))
