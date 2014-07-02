#coding=utf-8
#Head_First_Python第一章-读写数据,并保存
import io,sys
man = []    #创建列表 用于保存 Man的对话及 Other的对话内容
other = []

try :
    date = open('sketch.txt')   #date打开sketch.txt文本数据
    for each_item in date:  #进行date每一行的循环判断
        try:
            (role,line_spoken) = each_item.split(':',1)   #使用split方式 分割 :号前后的对话
            line_spoken = line_spoken.strip()   #去除空格
            if role == 'Man':   # 冒号前的对话赋值到role对象里 如果 role 等于Man,即为Man的对话
                man.append(line_spoken) #插入冒号后的对话内容至man[]这个列表
            elif role == 'Other Man':   #向上同理如role 等于other man 即为 other man的对话
                other.append(line_spoken)   #插入冒号后的对话内容至other[]这个列表
        except ValueError:
            pass

    date.close()
except IOError:
    print ('the datefile is missing!')

try:
    man_file = open('man_date.txt','w') #以w(读写)方式打开man_date.txt并赋值至man_file
    other_file = open('other_date.txt','w')#同理

    print (man,file=man_file)   #打印出man[]列表里的内容 并保存至man_file数据里 此时man_file就等于man_date.txt,w
    print (other,file=other_file) #同理

    man_file.close()
    other_file.close()

except IOError:
    print ('the date file is missing!')

