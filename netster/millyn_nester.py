#coding=utf-8
#Head_First_Python第一章-一个函数
'''
此函数作用为打印嵌套列表内的所有数据,
list = the_list
level = 嵌套列表的制表符参数 填写0即可 每一层list增加1
indent = 是否使用TAB制表符 默认为 否 传递参数时 0代表否 1或以上代表真
'''
def print_lol(the_list,indent=False,level=0):
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1)
        else:
            if indent:
                for tab_stop in range(level):
                    print ('\t', end='')
            print (each_item)

movies = ["The hold Graill", 1975 ,"Terry Jones & Terry Gilliam", 91,\
         ["Graham Chapman",["Micheal Palin", "John Cleese","Terry Gilliam",\
         "Eric Idie", "Terry Jones"]]]

print_lol(movies,0)