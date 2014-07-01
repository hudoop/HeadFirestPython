#coding=utf-8
#Head_First_Python第一章-文件与异常-先尝试 再恢复 检查文件 if方法
import os

if os.path.exists('sketch.txt'):    #利用os库的path.exists方法检查是否有'sketch.txt'文件
    date = open('sketch.txt')
    for each_item in date:
        try:    #try 顾名思义 尝试一下代码
            if not each_item.find(':') == -1 :  #使用find方法判断each_item获取的每一行数据里是否有 ' : '字符串
                                            #为什么用not?因为我们是反向思维 不等于 -1 也就是说 等于 1 则顺利通过判断
                (role , line_spoken) = each_item.split(':',1) #使split方法 分割 以':'为分割点 分割每行数据并赋值
                                                        # 冒号前赋值 role 冒号后 赋值 line_spoken
                                                        #split的参数是 '目标字符串' '允许最大数量'
                print (role, end='')
                print (' said:', end='')
                print (line_spoken,end='')
        except: #如果try的代码遇到错误则执行except内代码 pass
            pass
    date.close()    #关闭文件
else:
    print ('file error')