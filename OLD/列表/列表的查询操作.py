## 列表的查询操作
### '''获取列表中指定元素的索引'''

#### 获取单个元素   索引
lst5=['hello','world',98,'hello']
print(lst5 .index('hello',1))#如果列表中有相同元素值返回列表中相同元素的第一个元素
'''如果查询的元素在列表中不存在，则会抛出 ValueError'''
'''还可以在指定的start和stop之间进行查找'''
'''获取列表中的单个元素'''
'''正向索引从0到N-1  举例lst[0]'''
'''逆向索引-N到-1'''
'''指定索引不存，抛出IndexError'''

#### 获取列表中的多个元素
'''语法表格    列表名[start,stop,step]'''
lst6=[1,2,3,4,5,6,7,8,9,10]
print(lst6[1:5:2])
'''步长为复数'''
print('源列表：',lst6)
print(lst6[::-1])

### 判断指定元素是否存在
'''元素  in  列表名   ///    元素  not in  列表名'''
print('p'in'python')
lst7=[1,2,3,'python','ok','l']
print()
### 列表元素的遍历
'''for  迭代变量  in  列表名：'''
lst8=[1,2,3,4,5,6,7,8,9]
for item in lst8:
    print(item)
