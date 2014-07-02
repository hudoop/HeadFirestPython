#coding=utf-8
#Head_First_Python第一章-推导数据-处理数据把文本数据处理到列表中并显示 使用了with、strip、split
with open('james.txt') as jaf:  #用with方法打开james.txt文本并赋值到jaf
    date = jaf.readline()          #获取jaf里的一行数据赋值到date
james = date.strip().split(',')   #使用strip()函数去除空格并用split(',')函数的传递参数分割数据并赋值到james
                                  #date.strip().split(',')这句代码叫做方法串联
with open('julie.txt') as juf:
    date = juf.readline()
julie = date.strip().split(',')
with open('mikey.txt') as mif:
    date = mif.readline()
mikey = date.strip().split(',')
with open('sarah.txt') as saf:
    date = saf.readline()
sarah = date.strip().split(',')

print (james)
print (julie)
print (mikey)
print (sarah)