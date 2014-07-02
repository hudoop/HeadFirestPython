#coding=utf-8
#Head_First_Python第一章-文件格式到底适合不适合?

with open('man_date.txt') as mdf:   #打开man_date文件 并赋值到mdf
    print(mdf.readline())   #打印mdf对象 只读取一行

#这段代码的结果是显示了所有的man_date文本内数据,证明man_date没有多行的巨大文本