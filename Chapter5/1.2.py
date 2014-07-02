#coding=utf-8
#Head_First_Python第一章-推导数据-修改字符串的内容
james_new = []
julie_new = []
mikey_new = []
sarah_new = []
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


for each_t in james:    #循环james列表里的每一项数据
    james_new.append(sanitize(each_t))  #每一项数据作为参数笤俑到sanitize函数内并把返回值赋值到james_new列表的最后
for each_t in mikey:
    mikey_new.append(sanitize(each_t))
for each_t in julie:
    julie_new.append(sanitize(each_t))
for each_t in sarah:
    sarah_new.append(sanitize(each_t))

print (sorted(james_new))
print (sorted(mikey_new))
print (sorted(julie_new))
print (sorted(sarah_new))