#coding=utf-8
#Head_First_Python第一章-推导数据-列表推导 实际操作
def sanitize(item_string):  #创建一个函数,及一个函数参数
        if '-' in item_string:  #如果传递回来的参数内包含'-'
            splitter = '-'  #splitter赋值为 '-'
        elif ':' in item_string:
            splitter = ':'
        else:   #如果item_string里既没有- 又没有: 那么什么都不执行
            return item_string  #什么都不执行
        (mins,secs) = item_string.split(splitter)   #利用split方法调用splitter变量数据分解item_string里的数据
        return (mins+'.'+secs)  #返回一个值

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

print(sorted(sanitize(t) for t in james))   #推导列表的实际操作用法，其代码意思就是 打印
                                            # sorted方法调用sanitize函数 传递(t)这个参数 循环 t 至 james变量
print(sorted(sanitize(t) for t in julie))
print(sorted(sanitize(t) for t in mikey))
print(sorted(sanitize(t) for t in sarah))