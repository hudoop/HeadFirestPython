#coding=utf-8
#Head_First_Python第一章-推导数据-集合set()删除重复项 并把读取代码块写成函数
def sanitize(item_string):
        if '-' in item_string:
            splitter = '-'
        elif ':' in item_string:
            splitter = ':'
        else:
            return item_string
        (mins,secs) = item_string.split(splitter)
        return (mins+'.'+secs)

def loadfile(name): #创建一个函数 名为loadfile 并传递一个name的参数
    with open(name) as abc: #name参数即为文件名 用with方法打开 并赋值 到abc变量里
        date = abc.readline()   #读取abc里每一行的内容并赋值到date
        return (date.strip().split(','))        #return的意义是返回函数结果 也就是类似于print(是打印) 但是这里是返回一个结果
                                                #那么我们在调用的时候 我们就把以 变量名 等于 函数名(参数) 的语法来调用函数
                                                #所以return对应的是 调用函数的那个 变量名 return = james return = julie 很清楚了吧?


james = loadfile('james.txt')
julie = loadfile('julie.txt')
mikey = loadfile('mikey.txt')
sarah = loadfile('sarah.txt')

print(sorted(set(sanitize(t) for t in james))[0:3]) #这里就应该是执行了4步代码操作
#sorted,set,sanitize,for 四个方法叠加到一行代码中，是不是很神奇.
#翻译过来就是打印 首先调用sanitize方法 并使 t 向 james 里的每一个数据进行循环
#每一次循环的过程中set会进行去重工作
#最终sorted会来进行排序并打印结果为[0:3]就是显示0,1,2排序在最前的三条数据

print(sorted(set(sanitize(t) for t in julie))[0:3])
print(sorted(set(sanitize(t) for t in mikey))[0:3])
print(sorted(set(sanitize(t) for t in sarah))[0:3])

