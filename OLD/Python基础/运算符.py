#算术运算符
##标准算术运算符
# 标准算术运算符，加减乘除，整除（\\，一正一负向下取整)
print(1+1-2*8/3)
print(11//2)    #   5   整除运算
print(9//-4)#-3

##取余运算符（%）  一正一负要公式:余数=被除数-除数*商
print(11%2)# 余数为1
print(-9%4)#       3
print(9%-4)#      -3

##幂运算符（**）
print(2**2)#2的2次方
print(2**3)#2的3次方

##赋值运算符，运算顺序从右到左

'''支持链式赋值'''
x=7+5
print(x)#支持参数赋值

a=b=c=d=10086
print(a,id(a))
print(b,id(b))
print(c,id(c))

'''支持参数赋值'''
a=10086
a+=10086 #相当于a=a+10086
print(a)

a=10086
a-=10086#相当于a=a-10086
print(a)

a*=2 #相当于a=a*2
print(a,type(a)) #type=float

a/=2 #相当于a=a*2
print(a,type(a))

a//=2 #相当于a=a*2
print(a,type(a))

a%=2 #相当于a=a*2
print(a,type(a))


'''支持系列解包赋值'''
a,b,c=10,20,30
print(a,b,c)#左右变量的个数和值的个数需要对应，不能多或者少

#优势：两个变量的交换不需要中间变量
a,b=10,20
print('交换之前:',a,b)
#交换
a,b=b,a
print('交换之后:',a,b)

##比较运算符
###比较运算符是对变量或者表达式的结果进行大小、真假等比较
###符号：>,<,>=,<=,!=
###==  比较value（值） 比较对象的标识是  is 
### is , is not     对象的id的比较
a,b=10,20
print("a>b吗？",a>b)
print("a<b吗？",a<b)
print("a>=b吗？",a>=b)
print("a>=b吗？",a>=b)
print("a==b吗？",a>b)#一个 = 称为赋值运算符，==称为比较运算符
print("a!=b吗？",a>b)

a=10
b=10
print(a==b)#true  说明：a与b的value相等
print(a is b )#true 说明：a与b的id标识，相等

lst1=[11,22,33,44]
lst2=[11,22,33,44]
print(lst1==lst2)#value  true
print(lst1 is lst2)#id   false
print(id(lst1))
print(id(lst2))
print(a is not b)#false  a id = b id
print(lst1 is not lst2)#true  id !=

###布尔运算符
#布尔值之间的运算
#符号：and,or,not(对bool类型操作数取反),in,not in（在不在当中）
a,b=1,2
print(a==1 and b==2)#T  T  and    T   ---T 
print(a==1 and b<2)#F   T  and    F   ---F
print(a!=1 and b==2)#F  F  and    T   ---F
print(a!=1 and b!=2)#F  F  and    F   ---F

print(a==1 or b==2)#T  T  or    T   ---T 
print(a==1 or b<2)#T   T  or    F   ---F
print(a!=1 or b==2)#T  F  or    T   ---F
print(a!=1 or b!=2)#F  F  or    F   ---F

f1=True
f2=False
print(not f1)
print(not f2)

s=('helloword')
print('w' in s)#true
print('p'not in  s)#false

###位运算符   
# 将数据转成二进制进行计算       
### 位与&             对应位数都是1，结果位数才是1，否则为0
### 位与|             对应位数都是0，结果位数才是1，否则为1
### 左移位运算符<<    高位溢出舍弃，低位补0
### 右移位运算符>>    低位溢出舍弃，高位补0

#4的二进制为100， 8的二进制为1000
print(4&8)#0   按位与&  同为1时结果为1
print(4|8)#12  按位或|  同为0时结果为0
print(4<<1)  #向左移动1位（移动1个位置）相当于*2
print(4<<2)  #向左移动2位（移动2个位置）相当于*4

print(4>>1)  #向右移动1位（移动1个位置）相当于/2
print(4>>2)  #向右移动2位（移动1个位置）相当于/4

##运算符的优先级
#有括号先括号
#先乘除，再加减；
#先算术运算，然后位运算，再比较运算和布尔运算，最后赋值运算


