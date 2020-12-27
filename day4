import itertools
import re

def day4_1():
    with open('/Users/xinyue/Downloads/day4_1.txt', 'r') as file:
        file = file.read()
        counter = 0
        for each_passport in file.split('\n\n'):
            if (each_passport.count(':') == 8) | ((each_passport.count(':') == 7) and ('cid' not in each_passport)):
                counter += 1
        print(counter)


def day4_2():
    with open('/Users/xinyue/Downloads/day4_1.txt', 'r') as file:
        file = file.read()
        passport_list = []
        for each_passport in file.split('\n\n'):
            passport_dic = {}
            if (each_passport.count(':') == 8) | ((each_passport.count(':') == 7) and ('cid' not in each_passport)):
                each_passport = each_passport.replace(' ','/')
                each_passport = each_passport.replace('\n','/')
                parts = each_passport.split('/')
                try:
                    parts.remove('')
                except:
                    pass
                for each_part in parts:
                    passport_dic[each_part.split(':')[0]] =  each_part.split(':')[1]
            if len(passport_dic)>0:
                passport_list.append(passport_dic)
        counter = 0
        for each_dic in passport_list:
            if (int(each_dic['byr'])>=1920) & (int(each_dic['byr'])<=2020):
                if (int(each_dic['iyr'])>=2010) & (int(each_dic['iyr'])<=2020):
                    if (int(each_dic['eyr'])>=2020) & (int(each_dic['eyr'])<=2030):
                        if (('cm' in each_dic['hgt']) and ((int(each_dic['hgt'][:-2])>= 150) and(int(each_dic['hgt'][:-2])<= 193))) |\
                                (('in' in each_dic['hgt']) and ((int(each_dic['hgt'][:-2])>= 59) and(int(each_dic['hgt'][:-2])<= 76))):
                            if (each_dic['hcl'][0] == '#')and(len(each_dic['hcl'][1:])==6):
                                text = re.findall('[a-fA-F0-9]+',  each_dic['hcl'][1:])
                                if (len(text) == 1)and(len(text[0])==6):
                                    if each_dic['ecl'] in ['amb','blu','brn','gry','grn','hzl','oth']:
                                        if (len(each_dic['pid']) == 9) and (each_dic['pid'].isdecimal()):
                                            counter+=1
        print(counter)
