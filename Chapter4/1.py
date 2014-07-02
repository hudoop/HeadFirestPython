#coding=utf-8
#Head_First_Python第一章-数据保存到文件
import io
man = []
other = []
try :
    date = open('sketch.txt')
    for each_item in date:
        try:
            (role, line_spoken) = each_item.split(':',1)
            line_spoken = line_spoken.split()
            if role == 'Man':
                man.append(line_spoken)
            elif role == 'Other Man':
                other.append(line_spoken)
        except ValueError:
            pass
    date.close()

except IOError:
    print ('The date file is missing')

print (man)
print (other)
