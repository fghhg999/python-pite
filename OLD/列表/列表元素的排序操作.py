#常见的两种方式：_调用sort（）方法，列于中的所有元素默认按照从小到大的顺序进行排序，可以指定reverse=True，进行降序排序
#_调用内置函数sorted（），可以指定reverse=true，进行降序排序，产生新列表，源列表不发生改变
lst1=[81,62,13,44,55,63]
print('排序前的列表',lst1,id(lst1))
#开始排序，调用列表对象的sort方法，升序排序
lst1.sort()
print('排序后的列表',lst1,id(lst1))

#通过指定关键字参数，将列表中的元素进行降序排序
lst1.sort(reverse=True)  #reverse=Ture 表示降序排序，reverse=False就是升序排序
print(lst1)
lst1.sort(reverse=False)
print(lst1)

print('-----------使用内置函数sorted（）对列表进行排序，将产生一个新的列表对象--------------')
lst2=[4,6,8,344,89,234,6,879,90,2]
print('原列表',lst2)
#开始排序
new_list=sorted(lst2)
print(lst2)
print(new_list)
#指定关键字参数，实现列表元素的降序排序
desc_list=sorted(lst2,reverse=True)
print(desc_list)