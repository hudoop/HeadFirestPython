#coding=utf-8
#Head_First_Python第一章-处理更多的错误类型
try:
    date = open('missing.txt')  #尝试打开一个不存在的文件
    print (date.readline(),end='')  #并打印 这一步并不会执行 因为他出错了

except IOError as err:  #指定err对象显示确切的错误消息
    print ('file error' + str(err))    #错误类型是IOError 所以打印错误提示 + str(err) 使err 为str字符串 并打印

finally:
    if 'date' in locals():  #无论文件是否存在我们都要做好关闭文件的准备,但如果文件不存在时
                            #date这个变量的值是空白的,如果空白的date.close()运行起来会报错
                            #所以我们在之前添加一个使用locals 的方法 用if 来查询 date是否存在
        date.close()