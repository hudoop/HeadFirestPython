import millyn_nester    #调用之前写的函数
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

try:
     with open('man_date.txt','w') as man_file:
         millyn_nester.print_lol (man,edit=man_file)    #调用函数并写入参数 edit在函数里代表的是插入位置
                                                        #那么 man,edit=man_file意思就是 把man的内容插入到man_date.txt内
     with open('other_date.txt','w') as other_file:
         millyn_nester.print_lol (other,edit=other_file)
except IOError as err:
    print ('file error'+ str(err))