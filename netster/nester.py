#coding=utf-8
#Head_First_Python第一章-一个函数
'''
此函数作用为打印嵌套列表内的所有数据,
list = the_list
'''
def print_lol(the_list):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item)
        else:
            print (each_item)