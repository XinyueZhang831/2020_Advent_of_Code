import itertools
import re

def day5_1():
    with open('/Users/xinyue/Downloads/day5_1.txt', 'r') as file:
       tickets_list = [i for i in file.readlines()]

    def find_position(start_number,end_number,direction_sign,target_sign):
        new_median = (end_number-start_number-1)/2 +start_number
        if direction_sign == target_sign:
            end_number = new_median
            result = start_number
        else:
            start_number = new_median+1
            result=end_number
        return start_number,end_number,result


    ticket_number_list = []
    for each_tickets in tickets_list:
        start_number= 0
        end_number = 127
        for i in each_tickets[:7]:
            start_number,end_number,result = find_position(start_number,end_number,  i, 'F')

        start_number_c = 0
        end_number_c = 7
        for i in each_tickets[7:]:
            start_number_c,end_number_c,result_c = find_position(start_number_c,end_number_c,  i, 'L')
        ticket_number = result*8+result_c
        ticket_number_list.append(int(ticket_number))
    print(max(ticket_number_list))


def day5_2():
    with open('/Users/xinyue/Downloads/day5_1.txt', 'r') as file:
       tickets_list = [i for i in file.readlines()]

    def find_position(start_number,end_number,direction_sign,target_sign):
        new_median = (end_number-start_number-1)/2 +start_number
        if direction_sign == target_sign:
            end_number = new_median
            result = start_number
        else:
            start_number = new_median+1
            result=end_number
        return start_number,end_number,result


    ticket_number_list = []
    for each_tickets in tickets_list:
        start_number= 0
        end_number = 127
        for i in each_tickets[:7]:
            start_number,end_number,result = find_position(start_number,end_number,  i, 'F')

        start_number_c = 0
        end_number_c = 7
        for i in each_tickets[7:]:
            start_number_c,end_number_c,result_c = find_position(start_number_c,end_number_c,  i, 'L')
        ticket_number = result*8+result_c
        ticket_number_list.append(int(ticket_number))

    max_ticket = max(ticket_number_list)
    min_ticket = min(ticket_number_list)

    emptseat = {i for i in range(min_ticket,max_ticket+1)} - set(ticket_number_list)
    print(emptseat)
