#coding=utf-8
#Head_First_Python第一章-with处理文件

try:
    with open('miss.txt','w') as date:  #在这里我们看到了 我们使用了with方法以读写方式打开miss.txt文件并赋值date
        print('this is with bif',file=date) #打印this is with bif 至date变量里 也就是 miss.txt

except IOError as err:
    print ('file error'+ str(err))

#由此我们看到代码内没有我们熟悉的date.close() 我们没有关闭文件 这应该是不允许的
#为什么不写?因为我们使用了with方法, with方法利用一种上下文管理协议 使用with方法时python编译器会自动帮你考虑date.close()



man = []
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
'''
把两行with合并成一行
with open('man_date.txt','w') as man_file , open('other_date.txt','w') as other_file:
print (man,file=man_file)
print (other,file+other_file)
以下代码是根据书中题目写的作业
'''
try:
     with open('man_date.txt','w') as man_file:
         print (man,file=man_file)
     with open('other_date.txt','w') as other_file:
         print (other,file=other_file)
except IOError as err:
    print ('file error'+ str(err))