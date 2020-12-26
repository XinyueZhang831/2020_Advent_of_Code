import itertools
import re

def day3_1():
    with open('/Users/xinyue/Downloads/day3_1.txt', 'r') as file:
        tree_notempty= {}
        for y in enumerate(file.readlines()):
            current_row = []
            line_length = len(y[1].strip())
            for each_sign in range(len(y[1])):
                if y[1][each_sign] == '#':
                    current_row.append(each_sign)
            tree_notempty[y[0]] = current_row


    def counter_trees(tree_notempty, line_length):
        counter = 0
        for current_r in range(len(tree_notempty)):
            if ((current_r)*3)%line_length in tree_notempty[current_r]:
                counter+=1
        print(counter)

    counter_trees(tree_notempty, line_length)


def day3_2():
    with open('/Users/xinyue/Downloads/day3_1.txt', 'r') as file:
        tree_notempty= {}
        for y in enumerate(file.readlines()):
            current_row = []
            line_length = len(y[1].strip())
            for each_sign in range(len(y[1])):
                if y[1][each_sign] == '#':
                    current_row.append(each_sign)
            tree_notempty[y[0]] = current_row

    def counter_trees(tree_notempty, line_length,move_right,move_down):
        counter = 0
        for current_r in range(len(tree_notempty)):
            if current_r*move_down> len(tree_notempty):
                break
            if ((current_r)*move_right)%line_length in tree_notempty[current_r*move_down]:
                counter+=1
        return counter

    move_set = [(1,1), (3,1),(5,1),(7,1),(1,2)]
    current_result = 1
    for each_set in move_set:
        counter = counter_trees(tree_notempty, line_length, each_set[0],each_set[1])
        current_result *=counter
    print(current_result)
