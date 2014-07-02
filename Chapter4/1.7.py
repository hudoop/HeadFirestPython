#coding=utf-8
#Head_First_Python第一章-pickle的运用dump保存load读取
import pickle,millyn_nester
man = []
other = []
new_man = []
try :
    date = open('sketch.txt')
    for each_item in date:
        try:
            (role,line_spoken) = each_item.split(':',1)
            line_spoken = line_spoken.strip()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass

    date.close()
except IOError:
    print ('this date is missing')
try:
    with open('man_date.txt','wb') as man_file , open('other_date.txt','wb') as other_file:#使用pickle函数
        man = pickle.dump(man,man_file)     #pickle.dump函数保存文件
        other = pickle.dump(other,other_file)

except pickle.PickleError as perr:
    print('pickle err:'+ str(perr))

try:
    with open('man_date.txt','rb') as man_file: #使用pickle.loadh函数读取之前pickle.dump方法保存的二进制文件
        new_man = pickle.load(man_file) #并赋值到new_man这个列表

except IOError as err:
    print ('this date is missing :'+str(err))

except pickle.PickleError as perr:
    print ('pickle error :',+str(perr))