#coding=utf-8
#Head_First_Python第一章-文件与异常-文件处理
import os
os.getcwd()
date = open('sketch.txt')   #打开一个命名文件 赋值到date对象
print(date.readline(),end='')   #使用 readline方法 获取date对象里的一行数据 并打印

date.seek(0)    #使date回到起始点,因为上面的指令已经修改了他的起始点(已经读取了一行)

for each_item in date:
    if not each_item.find(':') == -1 :  #使用find方法判断each_item获取的每一行数据里是否有 ' : '字符串
                                        #为什么用not?因为我们是反向思维 不等于 -1 也就是说 等于 1 则顺利通过判断
        (role , line_spoken) = each_item.split(':',1) #使split方法 分割 以':'为分割点 分割每行数据并赋值
                                                    # 冒号前赋值 role 冒号后 赋值 line_spoken
                                                    #split的参数是 '目标字符串' '允许最大数量'
        print (role, end='')
        print (' said:', end='')
        print (line_spoken,end='')

date.close()    #关闭文件