name='闰猹'
occupation='树人药剂师'
age=666

#print(type(name),type(age))#将无法运行;数据类型不同 解决：类型转换
print('我是'+occupation+'，我叫'+name+'，今年已经'+str(age)+'岁了。')
#将int类型通过str（）函数转成str类型

a=10
b=5.18
c=False
print(type(a),type(b),type(c))
print(str(a)+str(b)+str(c))#字符串不能进行运算，要转换为int()
#105.18False
'''int()无法转换文字类和小数类str、
float文字类无法转换为整数，整数类转换为浮点数，末尾为0'''
