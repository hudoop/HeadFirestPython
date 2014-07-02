#coding=utf-8
#Head_First_Python第一章-推导数据-数据排序工作
print ('---------------------Date如下---------------------')
date = [6,3,1,5,2,4]
print (date)
print ('使用sorted函数把date进行排序并把排序结果赋值到一个新的列表里')
date2 = sorted(date)
print ('date = ',date)
print ('date2 = ',date2)
print ('使用sort函数把date进行排序并替换原本在date内的数据')
date.sort()
print (date)
print ('---------------------学习排序完毕---------------------')

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
print ('-----------------------排序前-----------------------')
print ('-----------------------排序后-----------------------')
print (sorted(james))   #使用sorted排序james并替换内容（原本james的内容已不存在）
print (sorted(julie))
print (sorted(mikey))
print (sorted(sarah))