#coding=utf-8
#Head_First_Python第一章-检查列表中的列表 if使用说明

name = ['Michael' , ' Terry'] #创建一个list
print (isinstance(name,list)) #使用isinstance BIF判断name是否为一个list 并打印出来
#True 结果为真 那么name即为一个list
num_name = len(name)    #使用len获取name的最大值并赋值到num_name
print (isinstance(num_name,list)) #判断num_name是否为一个列表并打印出来
#False 结果为假 num_name 不是一个list

movies = ["The hold Graill", 1975 ,"Terry Jones & Terry Gilliam", 91,\
         ["Graham Chapman",["Micheal Palin", "John Cleese","Terry Gilliam",\
         "Eric Idie", "Terry Jones"]]]
''' 这一段是我写出来的 我仅仅只是判断movies是否为列表 然后打印出详细数据 否则 打印error
if isinstance(movies,list):
    for each_item in movies:
        print (each_item)
else:
    print ('error')
print ('------------------------')
'''
for each_item in movies:    #开始执行循环
    if isinstance(each_item,list):  #判断each_item的值是否为list属性
        for nested_item in each_item:   #如果是list属性 继续开始判断
            if isinstance(nested_item,list): #判断nested_item是否为一个list属性
                for deeper_item in nested_item: #如果是list属性 就打印出来
                    print (deeper_item) #打印嵌套列表数据
            else:   #nested_item不是list属性
                print (nested_item)
    else:#each_item不是list属性
        print (each_item)   #如果不是列表即直接打印

