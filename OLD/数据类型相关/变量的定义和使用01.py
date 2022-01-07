name=10086
print(name)

#变量：
# 标识，表示对象所储存的内存地址，使用内置函数id（obj）获取
# +类型，表示对象的数据类型，使用内置函数type（obj）获取
# +值，表示对象所储存的集体数据，使用print（obj）将值进行打印输出

print(name)
print ('标识',id(name))
print('类型',type(name))
print('值',name)

#常用的数据类型：整数-int   浮点-float  布尔-bool（true，false）    字符串-str

#int可以表示正、负数和0
#可以表示二、八、十、十六进制
print('二进制',0b111)
print('八进制',0o1006)
print('十进制',10086)
print('十六进制',0x1ed)#十六进制：0123456789    abcdef


#float  浮点数整数部分和小数部分组成，浮点数存储不精确性，使用浮点数进行计算时，可能出现小数位数不确定的情况
print(1.1+2.2)#3.3000000000000003
#解决方案:导入Decimal模块
from decimal import Decimal
print(Decimal('1.1')+Decimal('2.2'))#3.3

#bool(boolean),用来表示真假的值，true-真，false-假，
# 布尔值可以转化为整数：true———>1   false———>0
print(True+1)#2
print(False+1)#1

#str,字符串=不可变的字符序列。可以用单、双、三引号来定义
#单、双引号定义的字符串必须在一行
#三引号定义的字符串可以分布在连续的多行
print('''人生苦短
我用Python''')

#多次赋值后，变量名会指向新的空间
name='Tom猫'
name='Jery鼠'
print(name)

