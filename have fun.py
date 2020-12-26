import itertools


def day1_1():
    with open('/Users/xinyue/Downloads/input.txt','r') as file:
        number_list = [int(i)for i in file.readlines()]
    if len(number_list)>1:
        for numbers in itertools.combinations(number_list, 2):
            if sum(numbers) == 2020:
                print(numbers)
                print(numbers[0]*numbers[1])


def day1_2():
    with open('/Users/xinyue/Downloads/input.txt','r') as file:
        number_list = [int(i)for i in file.readlines()]

    if len(number_list)>1:
        for numbers in itertools.combinations(number_list, 3):
            if sum(numbers) == 2020:
                print(numbers)
                print(numbers[0]*numbers[1]*numbers[2])


def day17_1():
    def read_in():
        input_list_active=set()
        with open('/Users/xinyue/Downloads/day17.txt','r') as file:
            for y in enumerate(file.readlines()):
                for x in range(len(y[1])):
                    if y[1][x]=='#':
                        input_list_active.add((x+1,y[0]+1,0))
        return input_list_active

    def count_active(input_list_active):
        backup_activelist = input_list_active.copy()
        new_inactive= {}
        for each_cube in input_list_active:
            counter_active = 0
            x,y,z = each_cube[0],each_cube[1],each_cube[2]
            for add_x in [-1,0,1]:
                for add_y in [-1,0,1]:
                    for add_z in [-1,0,1]:
                        if (x+add_x,y+add_y,z+add_z) != (x,y,z):
                            if (x+add_x,y+add_y,z+add_z) in input_list_active:
                                counter_active +=1
                            else:
                                if (x+add_x,y+add_y,z+add_z) in new_inactive.keys():
                                    new_inactive[(x+add_x,y+add_y,z+add_z)] += 1
                                else:
                                    new_inactive[(x + add_x, y + add_y, z + add_z)] =1
            # because only points arround active cound be actived latter, so count how many times it shows nearby an active point.
            if (counter_active == 2) |(counter_active == 3):
                pass
            else:
                backup_activelist.remove((x,y,z))
        for k,v in new_inactive.items():
            if v==3:
                backup_activelist.add(k)
        return backup_activelist, len(backup_activelist)

    input_list = read_in()
    for times in range(6):
        input_list, len_active = count_active(input_list)
    print(len_active)



def day17_2():
    def read_in():
        input_list_active=set()
        with open('/Users/xinyue/Downloads/day17_2.txt','r') as file:
            for y in enumerate(file.readlines()):
                for x in range(len(y[1])):
                    if y[1][x]=='#':
                        input_list_active.add((x+1,y[0]+1,0,0))
        return input_list_active

    def count_active(input_list_active):
        backup_activelist = input_list_active.copy()
        new_inactive= {}
        for each_cube in input_list_active:
            counter_active = 0
            x,y,z,w = each_cube[0],each_cube[1],each_cube[2],each_cube[3]
            for add_x in [-1,0,1]:
                for add_y in [-1,0,1]:
                    for add_z in [-1,0,1]:
                        for add_w in [-1, 0, 1]:
                            if (x+add_x,y+add_y,z+add_z,w+add_w) != (x,y,z,w):
                                if (x+add_x,y+add_y,z+add_z,w+add_w) in input_list_active:
                                    counter_active +=1
                                else:
                                    if (x+add_x,y+add_y,z+add_z,w+add_w) in new_inactive.keys():
                                        new_inactive[(x+add_x,y+add_y,z+add_z,w+add_w)] += 1
                                    else:
                                        new_inactive[(x + add_x, y + add_y, z + add_z,w+add_w)] =1
            # because only points arround active cound be actived latter, so count how many times it shows nearby an active point.
            if (counter_active == 2) |(counter_active == 3):
                pass
            else:
                backup_activelist.remove((x,y,z,w))
        for k,v in new_inactive.items():
            if v==3:
                backup_activelist.add(k)
        return backup_activelist, len(backup_activelist)

    input_list = read_in()
    for times in range(6):
        input_list, len_active = count_active(input_list)
    print(len_active)

day17_2()



