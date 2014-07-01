#coding=utf-8
#Head_First_Python第一章-为函数增加第二个参数
#为了更好的打印list所以我们增加了tab制表功能,使嵌套的list以tab来进行排序打印
def print_lol(the_list,level=0):  #我们增加一个名为level的参数,为什么要=0?因为使level成为一个可选或者说有默认值的参数
                                    #保证在有人更新使用此函数时并没有添加第二个参数而出错
    for each_item in the_list:
        if isinstance(each_item,list):
            print_lol(each_item,level+1)    #!!!记住 这里一定也要增加参数,因为这里是递归调用
                                            #为什么要+1 如果循环是正常的,那么就会出现list[x][x]这样的数据 那么证明
                                            #这是一个嵌套list,我们把每一层的嵌套list进行tab排序,如果不在参数+1的话
                                            #无论是嵌套了几层,都是固定值.因为参数没有变化.
        else:
            for tab_stop in range(level):
                print ('\t', end='')
            print (each_item)
            
movies = ["The hold Graill", 1975 ,"Terry Jones & Terry Gilliam", 91,\
         ["Graham Chapman",["Micheal Palin", "John Cleese","Terry Gilliam",\
         "Eric Idie", "Terry Jones"]]]

print_lol(movies,0)