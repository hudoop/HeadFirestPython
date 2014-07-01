#coding=utf-8
#Head_First_Python第一章-关于列表中的列表，其他语言俗称多维数组

movies = ["The hold Graill", 1975 ,"Terry Jones & Terry Gilliam", 91,\
         ["Graham Chapman",["Micheal Palin", "John Cleese","Terry Gilliam",\
         "Eric Idie", "Terry Jones"]]]
#形成一个列表中的列表
#move[0]=The hold graill move[1]=1975 move[2] = terry jones move[3] 91
#move[4]="Graham Chapman",["Micheal Palin", "John Cleese","Terry Gilliam","Eric Idie", "Terry Jones"]
#由此可见move[4]是一个多维数组当print move[4]的时候会打印出move[4]嵌套列表
#当列表参数精准到多维数组的数据时 就会精准打印出 当前数据
print (movies[4][1][3])
# Eric Idie
print (movies[4])
# ['Graham Chapman', ['Micheal Palin', 'John Cleese', 'Terry Gilliam', 'Eric Idie', 'Terry Jones']]
print ('-----------------------------------------')
for each_item in movies:    #循环 使each_item每次循环movies的内容, 循环 变量 至 列表
                            #也就是说循环顺序为 move[0] move[1] move[2] move[3] move [4]结束
    print (each_item)