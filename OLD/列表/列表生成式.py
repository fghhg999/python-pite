#列表生成式---生成列表的公式     
#语法格式  [i*i              for     i        in range(1 ,10)]
#       表示列表元素的表达式       自定义变量         可迭代对象

#注意事项  “表示列表元素的表达式”中通常包含自定义变量

lst1=[i*i for i in range(1,10) ]

print('''列表中的元素的值为2，4，6，8，10''')
lst2=[i*2 for i in range(1,6)]
print(lst2)