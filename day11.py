import itertools
import collections
import re
import copy

def day11_1():
    with open('/Users/xinyue/Downloads/day11_1.txt', 'r') as file:
        input_file = file.read().split('\n')
    while '' in input_file:
        input_file.remove('')


    while True:
        whole_space = []
        for each_line in range(len(input_file)):
            current_line = ''
            for each_seat in range(len(input_file[each_line])):
                #print(each_line,each_seat)
                upseat, upseat_l, upseat_r, sameline_l, sameline_r, downseat_l, downseat, downseat_r = '', '', '', '', '', '', '', ''
                if each_line > 0:
                    upseat = input_file[each_line - 1][each_seat]
                if each_line < len(input_file) - 1:
                    downseat = input_file[each_line + 1][each_seat]
                if each_seat > 0:
                    sameline_l = input_file[each_line][each_seat - 1]
                if each_seat < len(input_file[each_line]) - 1:
                    sameline_r = input_file[each_line][each_seat + 1]
                if (each_line > 0) and (each_seat > 0):
                    upseat_l = input_file[each_line - 1][each_seat - 1]
                if (each_line > 0) and (each_seat < len(input_file[each_line]) - 1):
                    upseat_r = input_file[each_line - 1][each_seat + 1]
                if (each_line < len(input_file) - 1) and each_seat>0:
                    downseat_l = input_file[each_line + 1][each_seat - 1]
                if (each_line < len(input_file) - 1) and (each_seat < (len(input_file[each_line]) - 1)):
                    downseat_r = input_file[each_line + 1][each_seat + 1]

                adj_seats = [upseat, upseat_l, upseat_r, sameline_l, sameline_r, downseat_l, downseat, downseat_r]
                if (input_file[each_line][each_seat] == 'L') and all([i != '#' for i in adj_seats]):
                    current_line += '#'
                elif (input_file[each_line][each_seat] == '#') and adj_seats.count('#') >= 4:
                    current_line += 'L'
                else:
                    current_line += input_file[each_line][each_seat]
            whole_space.append(current_line)
        if whole_space == input_file:
            break
        else:
            input_file = whole_space

    counter = 0
    for i in whole_space:
        counter+=i.count('#')
    print(counter)


def day11_2():
    with open('/Users/xinyue/Downloads/day11_1.txt', 'r') as file:
        input_file = file.read().split('\n')
    while '' in input_file:
        input_file.remove('')

    seat_dic={'L':set(), '.':set(), '#':set()}
    for i in enumerate(input_file):
        for j in range(len(i[1])):
            if i[1][j] == 'L':
                seat_dic['L'].add((i[0],j))
            elif i[1][j] =='.':
                seat_dic['.'].add((i[0], j))


    def leftup_point(current_point):
        i = current_point[0]-1
        j = current_point[1]-1
        while (i !=0) and (j!=0) and ((i,j) in seat_dic['.']):
            i -=1
            j -=1
        return (i,j)

    def up_point(current_point):
        i = current_point[0]-1
        j = current_point[1]
        while (i !=0) and ((i,j) in seat_dic['.']):
            i -=1
        return (i,j)

    def rightup_point(current_point):
        i = current_point[0]-1
        j = current_point[1]+1
        while (i !=0) and (j!= len(input_file[0])-1) and ((i,j) in seat_dic['.']):
            i -=1
            j +=1
        return (i,j)

    def leftsame_point(current_point):
        i = current_point[0]
        j = current_point[1]-1
        while (j!=0) and ((i,j) in seat_dic['.']):
            j-=1
        return (i,j)

    def rightsame_point(current_point):
        i = current_point[0]
        j = current_point[1]+1
        while j!=len(input_file[0])-1 and ((i,j) in seat_dic['.']):
            j+=1
        return (i,j)

    def leftdown_point(current_point):
        i = current_point[0]+1
        j = current_point[1]-1
        while (i !=len(input_file)-1) and (j!=0) and ((i,j) in seat_dic['.']):
            i +=1
            j -=1
        return (i,j)

    def down_point(current_point):
        i = current_point[0]+1
        j = current_point[1]
        while (i !=len(input_file)-1) and (((i,j) in seat_dic['.'])):
            i +=1
        return (i,j)

    def rightdown_point(current_point):
        i = current_point[0]+1
        j = current_point[1]+1
        while (i !=len(input_file)-1) and (j!=len(input_file[0])-1)and (((i,j) in seat_dic['.'])):
            i +=1
            j+=1
        return (i,j)


    def find_eight_direction(current_point,key):
        if key !='.':
            leftup_points = leftup_point(current_point)
            up_points = up_point(current_point)
            rightup_points = rightup_point(current_point)
            leftsame_points = leftsame_point(current_point)
            rightsame_points = rightsame_point(current_point)
            leftdown_points = leftdown_point(current_point)
            down_points = down_point(current_point)
            rightdown_points = rightdown_point(current_point)
            occupied_list = {leftup_points, up_points,rightup_points,leftsame_points, rightsame_points,leftdown_points,
                             down_points, rightdown_points}
            if key == '#':
                if len(occupied_list & seat_dic_copy['#'])>=5:
                    seat_dic['#'].remove(current_point)
                    seat_dic['L'].add(current_point)
            elif key == 'L':
                if len(occupied_list & seat_dic_copy['#']) == 0:
                    seat_dic['#'].add(current_point)
                    seat_dic['L'].remove(current_point)

    seat_dic_copy = {}
    while (seat_dic_copy != seat_dic):
        seat_dic_copy = copy.deepcopy(seat_dic)
        for k,v in seat_dic_copy.items():
            for each_v in v:
                find_eight_direction(each_v, k)

    print(len(seat_dic['#']))
