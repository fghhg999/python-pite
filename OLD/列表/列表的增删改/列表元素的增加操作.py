#向列表的末尾添加一个元素
lst1=[10,20,30]
print('添加元素之前',lst1,id(lst1))
lst1.append(100)#常用
print('添加元素之后',lst1,id(lst1))
lst2=['hello','world']
print("------------------------------")

#lst.append(lst1)----将lst1作为一个元素添加到列表的末尾
#向列表的末尾一次性添加多个元素
lst2.append(lst1)
print(lst2)
print("------------------------------")
#向列表的末尾以此向添加多个元素


lst1.extend(lst2)#lst1.extend(lst2)-----将lst2作为一个元素添加到列表的末尾
print(lst1)
print("------------------------------")


#在任意位置上添加一个元素
lst3=['hero','bear']
lst3.insert(1,'or')
print('输出后',lst3)
print("------------------------------")


#切片：在任意位置上添加N多个元素
#lst[start:stop]=要添加元素
lst4=[True,False,'hello']
lst4[1:]=lst3#（切点后面的位置全被替换）
print(lst4)
print("------------------------------")
lst5=['a','b','c','d']
lst5[1:2]=lst3
print(lst5)

