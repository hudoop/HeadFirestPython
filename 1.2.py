#coding=utf-8
#Head_First_Python第一章-关于for、迭代
move = ['The Holy Girl' , "The Life of Brian", "The Meaning of Life"]

for each_flick in move: #循环 使each_flick每次循环move的内容, 循环 变量 至 列表
                        #也就是说循环顺序为 move[0] move[1] move[2] 结束
    print (each_flick)

k = 0   #由于 while循环是无限循环 所以必须创建一个计数标识符
while k < len(move):    #当 k 小余 move列表最大值时
    print (move[k]) #打印列表 循环顺序为 move[0] move[1] move[2] 当到2时 k并不小于 len(move)所以停止
    k = k + 1   #执行完成一次循环后 k应+1 否则k一直为 0
    
    
    
    
    
    
    
    #我改了啊！！！！
