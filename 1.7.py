#coding=utf-8
#Head_First_Python第一章-为函数增加第三个参数
#我们发现有的人并不喜欢用TAB来进行制表那么我们在参数中添加了第三个关键值indent
def print_lol(the_list,indent=False,level=0):  #增加一个名为indent的参数,默认为False(假)
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,indent,level+1)    #!!!同1.6一样,我们在递归调用中添加新添加的参数值
        else:
            if indent:  #我们判断indent 是真(True)或假(False) 这全看调用函数时传递的参数
                        #print_lol(movies,0)0代表假,如果是这样则不执行
                        #print_lol(movies,1~n)代表真超过0的值都代表真,代表真的情况下会继续执行下面代码块
                for tab_stop in range(level):
                    print ('\t', end='')
            print (each_item)
            
movies = ["The hold Graill", 1975 ,"Terry Jones & Terry Gilliam", 91,\
         ["Graham Chapman",["Micheal Palin", "John Cleese","Terry Gilliam",\
         "Eric Idie", "Terry Jones"]]]

print_lol(movies,1)