import itertools
import collections
import re

def day20_1():
    with open('/Users/xinyue/Downloads/day20_1.txt', 'r') as file:
        input_file = file.read().split('\n\n')
    while '' in input_file:
        input_file.remove('')

    graph_dic = {}
    order_list = collections.defaultdict(list)
    for each_input in input_file:
        each_input_lines = each_input.split('\n')
        number = re.findall('[0-9]+', each_input_lines[0])[0]
        first_line = each_input_lines[1]
        last_line = each_input_lines[-1]
        left_line = []
        right_line = []
        for each_line in each_input_lines:
            charlist = list(each_line)
            left_sign = charlist[0]
            right_sign = charlist[-1]
            left_line.append(left_sign)
            right_line.append(right_sign)
        left_line = ''.join(left_line)[1:]
        right_line = ''.join(right_line)[1:]
        line_list = [first_line,last_line,left_line,right_line]
        graph_dic[number] = line_list
        for each_line_side in line_list:
            order_list[each_line_side].append(number)
            order_list[each_line_side[::-1]].append(number)

    attached_map = collections.defaultdict(int)
    single_side_map = collections.defaultdict(int)
    for k,v in order_list.items():
        if len(v) == 2:
            for each_number in v:
                attached_map[each_number]+=1
        if len(v) == 1:
            single_side_map[v[0]]+=1

    result = 1
    for k,v in attached_map.items():
        if v ==4:
            result *=int(k)
    print(result)


def day20_2():
    with open('/Users/xinyue/Downloads/day20_1.txt', 'r') as file:
        input_file = file.read().split('\n\n')
    while '' in input_file:
        input_file.remove('')
    
    # modify input => a nested list of each piece
    # graph_dic is a dictionary which store four sides of each piece
    graph_dic = {}
    # order_list is the dictionary which {'side':[pieceA, pieceB]}
    order_list = collections.defaultdict(list)
    # whole_piece is a dictionay which contains all lines for each piece
    whole_piece = {}
    for each_input in input_file:
        each_input_lines = each_input.split('\n')
        number = re.findall('[0-9]+', each_input_lines[0])[0]
        whole_piece[number] = each_input_lines[1:]
        first_line = each_input_lines[1]
        last_line = each_input_lines[-1]
        left_line = []
        right_line = []
        for each_line in each_input_lines:
            charlist = list(each_line)
            left_sign = charlist[0]
            right_sign = charlist[-1]
            left_line.append(left_sign)
            right_line.append(right_sign)
        left_line = ''.join(left_line)[1:]
        right_line = ''.join(right_line)[1:]
        line_list = [first_line,last_line,left_line,right_line]
        graph_dic[number] = line_list
        for each_line_side in line_list:
            order_list[each_line_side].append(number)
            order_list[each_line_side[::-1]].append(number)

    # find the corner piece
    corner_map = []
    for k,v in attached_map.items():
        if v ==4:
            corner_map.append(k)


    def rotate_puzzle(number):
        if type(number) == str:
            result_pl = []
            for pl_length in reversed(range(len(whole_piece[number][0]))):
                new_line = []
                for i in whole_piece[number]:
                    new_line.append(i[pl_length])
                result_pl.append(''.join(new_line))
            whole_piece[number] = result_pl
        else:
            result_pl = []
            for pl_length in reversed(range(len(number[0]))):
                new_line = []
                for i in number:
                    new_line.append(i[pl_length])
                result_pl.append(''.join(new_line))
        return result_pl

    def flip_puzzle_up(number):
        if type(number) == str:
            flip_result = whole_piece[number][::-1]
        else:
            flip_result = number[::-1]
        return flip_result

    def flip_puzzle_left(number):
        result_pl= []
        if type(number) == str:
            for each_line in whole_piece[number]:
                result_pl.append(each_line[::-1])
        else:
            for each_line in number:
                result_pl.append(each_line[::-1])
        return result_pl
    
    # to modift the next piece so that the left side of the next piece is the same as the right side of the previous piece
    def modify_next_piece(next_piece, previous_right_side):
        current_left_side = ''
        while current_left_side != previous_right_side:
            rotate_puzzle(next_piece)
            current_left_side = ''.join([i[0] for i in whole_piece[next_piece]])
            if current_left_side == previous_right_side:
                break
            new_piece = flip_puzzle_left(next_piece)
            current_left_side= ''.join([i[0] for i in new_piece])
            if current_left_side == previous_right_side:
                whole_piece[next_piece] = new_piece
                break
            new_piece = flip_puzzle_up(next_piece)
            current_left_side = ''.join([i[0] for i in new_piece])
            if current_left_side == previous_right_side:
                whole_piece[next_piece] = new_piece
                break

    # to modift the next piece so that the up side of the next piece is the same as the down side of the piece above it
    def modify_next_piece_up(next_piece, previous_down_side):
        current_up_side = ''
        while current_up_side != previous_down_side:
            rotate_puzzle(next_piece)
            current_up_side = whole_piece[next_piece][0]
            if current_up_side == previous_down_side:
                break
            new_piece = flip_puzzle_left(next_piece)
            current_up_side = new_piece[0]
            if current_up_side == previous_down_side:
                whole_piece[next_piece] = new_piece
                break
            new_piece = flip_puzzle_up(next_piece)
            current_up_side = new_piece[0]
            if current_up_side == previous_down_side:
                whole_piece[next_piece] = new_piece
                break

    # according to the order_list which contains which side is shared with two piece, find the next piece.
    def find_next_piece(current_piece):
        current_right_side = ''.join([i[-1] for i in whole_piece[current_piece]])
        next_piece_list = order_list[current_right_side].copy()
        next_piece_list.remove(current_piece)
        modify_next_piece(next_piece_list[0], current_right_side)
        return next_piece_list[0]
    
    # graph_finish is a nested list which contains all the puzzle number in order
    graph_finish = []
    # current lines is a list which contains the puzzle number which should be in the same line
    current_lines = []
    counter = 0
    start_with = corner_map[0]
    current_right_side = ''.join([i[-1] for i in whole_piece[start_with]])
    current_down_side = whole_piece[start_with][-1]
    while (len(order_list[current_right_side])!= 2) or (len(order_list[current_down_side])!= 2):
        rotate_puzzle(start_with)
        current_right_side = ''.join([i[-1] for i in whole_piece[start_with]])
        current_down_side = whole_piece[start_with][-1]

    # list every piece properly in graph_finish and current_lines
    while counter< len(whole_piece):
        counter +=1
        current_lines.append(start_with)
        piece_number = find_next_piece(start_with)
        next_right_side = ''.join([i[-1] for i in whole_piece[piece_number]])
        if len(order_list[next_right_side]) == 1:
            current_lines.append(piece_number)
            bottem_line_previous = whole_piece[current_lines[0]][-1]
            start_with_list = order_list[bottem_line_previous].copy()
            start_with_list.remove(current_lines[0])
            graph_finish.append(current_lines)
            current_lines = []
            if len(start_with_list)==0:
                break
            modify_next_piece_up(start_with_list[0], bottem_line_previous)
            start_with =start_with_list[0]
        else:
            start_with = piece_number

    combine_lines = []
    for each_line in graph_finish:

        for i in range(1,len(whole_piece[each_line[0]])-1): # find the total number of lines in each piece
            current_line = ''
            for j in each_line:
                current_line+=whole_piece[j][i][1:-1]
            combine_lines.append(current_line)

    moster_line1 = [18]
    moster_line2 = [0,5,6,11,12,17,18,19]
    moster_line3 = [1,4,7,10,13,16]

    # check the monster by each line and each character to see if there is a monster and how many monster in the picture. if 0 monster, flip up-down and check gain
    # if still counter = 0, flip left-right. 0 again, rotate to left.
    def find_monster(combine_lines):
        counter = 0
        for i in range(len(combine_lines)):
            for j in range(len(combine_lines[0])):
                if (i+2 < len(combine_lines))&(moster_line1[0] + j<len(combine_lines[0])):
                    if (combine_lines[i][moster_line1[0] + j] == '#') :
                        second_line = []
                        sign_line = []
                        for k in moster_line2:
                            if k+j<len(combine_lines[0]):
                                if combine_lines[i + 1][k + j] != '#':
                                    second_line.append(False)
                                else:
                                    sign_line.append(combine_lines[i + 1][k + j])
                                    second_line.append(True)
                            else:
                                second_line.append(False)
                        for l in moster_line3:
                            if l+j<len(combine_lines[0]):
                                if combine_lines[i + 2][l + j] != '#':
                                    second_line.append(False)
                                else:
                                    sign_line.append(combine_lines[i + 1][l + j])
                                    second_line.append(True)
                            else:
                                second_line.append(False)
                        if all(second_line) == True:
                            counter+=1
        return counter


    counter = 0
    times = 0
    while counter==0:
        times+=1
        combine_lines = rotate_puzzle(combine_lines)
        print(combine_lines)
        counter = find_monster(combine_lines)
        if counter == 0:
            current_graph = flip_puzzle_left(combine_lines)
            counter = find_monster(current_graph)
        if counter == 0:
            current_graph = flip_puzzle_up(combine_lines)
            counter = find_monster(current_graph)
        if times == 10:
            break

    counter_sign = 0
    for each_line in combine_lines:
        counter_sign+=each_line.count('#')
    print(counter_sign-15*counter)
