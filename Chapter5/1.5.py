#coding=utf-8
#Head_First_Python第一章-推导数据-去掉列表里的重复值
def sanitize(item_string):
        if '-' in item_string:
            splitter = '-'
        elif ':' in item_string:
            splitter = ':'
        else:
            return item_string
        (mins,secs) = item_string.split(splitter)
        return (mins+'.'+secs)

def delun(tt,ttt):  #为了减少代码的输入我们创建一个去重及取最优值的函数,并传递2个参数tt为原始数据ttt为修改后的数据
    for each_t in tt:    # 使each_t 循环 tt 的每一个数据
        if each_t not in ttt:   # 如果 each_t的数据在ttt里不存在
            ttt.append(each_t)  #ttt会增加each_t的数据
    print (ttt[0:3]) #打印修改后的数据 并显示前三

with open('james.txt') as jaf:
    date = jaf.readline()
james = date.strip().split(',')

with open('julie.txt') as juf:
    date = juf.readline()
julie = date.strip().split(',')
with open('mikey.txt') as mif:
    date = mif.readline()
mikey = date.strip().split(',')
with open('sarah.txt') as saf:
    date = saf.readline()
sarah = date.strip().split(',')

james = (sorted(sanitize(t) for t in james))
julie = (sorted(sanitize(t) for t in julie))
mikey = (sorted(sanitize(t) for t in mikey))
sarah = (sorted(sanitize(t) for t in sarah))
un_james = []
un_julie = []
un_mikey = []
un_sarah = []

delun(james,un_james)
delun(julie,un_julie)
delun(mikey,un_mikey)
delun(sarah,un_sarah)
