lst1=[1,2,3,4,5,6]
print(lst1)
lst1.remove(4)#移出
#从列表中移除一个元素，如果有重复元素只移除第一个元素
print(lst1)
#lst.remove(100)--- ValueError:list.remove(x): x not in list
print("------------------------------")
print("------------------------------")
print("------------------------------")

#pop()根据索引移除元素
lst1.pop(1)
print(lst1)
#lst1.pop(100)--- IndexError: pop index out of range(超出边界--指定索引位置不存在，抛出异常)
lst1.pop()#不指定参数，将会删除列表中的最后一个元素
print('不指定参数结果',lst1)


print('-------切片操作会删除至少一个元素，将会产生一个新的列表对象')
new_list1=lst1[1:3]
print('源列表',lst1)
print('切片后的列表',new_list1)

print('不产生新的列表对象，而是删除列表的原内容')
lst7=[1,2,3,'0',6,7,8,9,0,6,5]#删除指定位置区间的元素
lst7[1:4]=[]
print(lst7)
print('运行后',lst7)

##clear 清除列表中所有元素
lst7.clear()
print(lst7)

'''del语句将列表对象删除'''
del lst7
#print(lst7)  #NameEeeor：name 'lst7' is not defined
