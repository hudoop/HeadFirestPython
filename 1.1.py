#coding=utf-8
#Head_First_Python第一章-关于列表的创建

move = ['The Holy Girl' , "The Life of Brian", "The Meaning of Life"]   #创建一个列表字符串位置从0开始
print (move)
print (len(move))   #查询并打印列表最大数据
#-----------------------------关于创建
move.append('Cool list')    #添加Cool list至move列表的最后一项,append是至添加内容至列表的末尾 只能添加单一数据
print (move)
move.pop()  #删除move列表最末尾的数据
print (move)
move.extend(['Cool list', 'Perter list'])   #添加多个数据至列表的末尾
print (move)
#----------------------------关于删除
move.remove('Cool list')    #删除列表里的数据
print (move)
#-----------------------------关于修改
move.insert(0,'Cool list')  #从指定位置添加数据 从move[0]添加 cool list数据
print (move)