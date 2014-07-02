#coding=utf-8
#Head_First_Python第一章-推导数据-推导列表
'''
clean_mikey = []
for each_t in mikey:
    clean_mikey.append(sanitize(each_t))
这是一个列表转换到另一个列表的代码
他一共有三行,四个步骤.
1.创建一个新的列表clean_mikey =[]
2.迭代运算 for each_t in mikey :
3.通过函数转换(sanitize(each_t))
4.追加新内容至新列表append.(sanitize(each_t))
下面作为同样的功能,我们使用推到列表
clean_mikey = [sanitize(each_t) for each_t in mikey ]
1. 创建一个列表clean_mikey = [*************]
2. 迭代运算 for each_t in mikey
3. 通过函数运算 sanitize(each_t)
4. 追加clean_mikey = [sanitize(each_t) for each_t in mikey ]
下面是简单的例子
'''
def sanitize(item_string):  #创建一个函数,及一个函数参数
        if '-' in item_string:  #如果传递回来的参数内包含'-'
            splitter = '-'  #splitter赋值为 '-'
        elif ':' in item_string:
            splitter = ':'
        else:   #如果item_string里既没有- 又没有: 那么什么都不执行
            return item_string  #什么都不执行
        (mins,secs) = item_string.split(splitter)   #利用split方法调用splitter变量数据分解item_string里的数据
        return (mins+'.'+secs)  #返回一个值

mins = [1, 2, 3]
secs = [m * 60 for m in mins]
print (secs)
#结果是 60 120 180 也就是说 这行代码是 1 * 60 2 * 60 3 *60在运算

meters = [1 , 10 , 3]
feet = [m* 3.281 for m in meters]
print (feet)
#结果是3.281 32.81 9.843 同理 这是米转换英尺

lower = ['I',"don't",'like',"spam"]
upper = [s.upper() for s in lower]
print (upper)
#结果是 I DON'T LIKE SPAM 这是一个把大小写统一转换为大写的代码 每一次循环 都会执行s.upper()函数

dirty = ['2-22','3:12','2.99']
clean = [sanitize(a) for a in dirty]
print (clean)
#此代码块就是在本文件开头注释里所说的内容
clean1 = [float(t) for t in clean]
print (clean1)
#用代码串联的方法把clean的内容转换为float 浮点数据类型
clean2 = [float(sanitize(t)) for t in ['2-22','3:33','4.44']]
print (clean2)
#转换也可以是一个函数连（方法串联） 在for 里 对象也可以为未赋值的数据项内容