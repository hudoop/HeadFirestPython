#coding=utf-8
#Head_First_Python第一章-为了不写重复代码 我们创建一个函数

movies = ["The hold Graill", 1975 ,"Terry Jones & Terry Gilliam", 91,\
         ["Graham Chapman",["Micheal Palin", "John Cleese","Terry Gilliam",\
         "Eric Idie", "Terry Jones"]]]

def print_lol(the_list):    #定义一个函数名为print_lol 并指定参数名为 the_list
    for each_item in the_list:  # 使each_item 与 the_list进行循环
        if isinstance(each_item,list):  #判断each_item(即为参数传递进来的the_list是否为list
            print_lol(each_item)    #利用函数打印
        else:
            print (each_item) #普通打印

print_lol(movies)