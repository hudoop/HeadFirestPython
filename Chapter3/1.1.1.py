#coding=utf-8
#Head_First_Python第一章-文件与异常-先尝试 再恢复 检查文件 try方法
try:    #把try放在代码起始点，只要代码出错 立即执行except内容
    date = open('sketch.txt')
    for each_item in date:
        try:
            if not each_item.find(':') == -1 :  #使用find方法判断each_item获取的每一行数据里是否有 ' : '字符串
                                            #为什么用not?因为我们是反向思维 不等于 -1 也就是说 等于 1 则顺利通过判断
                (role , line_spoken) = each_item.split(':',1) #使split方法 分割 以':'为分割点 分割每行数据并赋值
                                                        # 冒号前赋值 role 冒号后 赋值 line_spoken
                                                        #split的参数是 '目标字符串' '允许最大数量'
                print (role, end='')
                print (' said:', end='')
                print (line_spoken,end='')
        except ValueError:  #如果是valueerror就直接执行pass 为什么会肯定这里只会有value错误呢?因为在代码块
                            #起始点有try: 第二行代码快就是关于io读取的语句 如果错了 肯定是执行与第一个try配套的
                            #except IOError
            pass
    date.close()    #关闭文件
except IOError: #如果是IOerror就直接执行print
    print ('The date file is missing')