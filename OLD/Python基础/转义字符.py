#转义字符，表达：反斜杠\+i想要实现的转义功能首字母
#当字符串中包含反斜杠、单引号、和双引号等有特殊用途的字符时，必须使用反斜杠对这些字符进行转义（转换一个含义）
#反斜杠：\\  单引号:'\'  双引号："\"
#换行：\n(ext)   水平制表符：\t(ap)    退格：\b    回车，回到文本开头：\r
print('hello\nworld')#\  +转义功能首字母   n——》newline的首字母，表示换行
print('hello\tworld')#\t 制表位占4个字符位
print('hello\rworld')#\r world将hello进行列覆盖，回的
print('hello\bworld')#\b 回退一格

print('http:\\\\www.baidu.com')
print('神说：\'要有光\'')

#原字符，不希望str中的转义字符起作用，就使用原字符，即在str之前加上r，或者R.注意事项：最后一个字符不能是反斜杠\
print(r'hello\nworld')

#