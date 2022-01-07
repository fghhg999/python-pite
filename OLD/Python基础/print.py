#print(),输出数字，字符串，含有运算符的字串符
print(123)
print("helloword")
print(1+5*5)

#将数据输出文件中,注意：所指定的盘符必须存在，使用file=（文件）
bp=open('D:text.txt','a+')#a+—追加，如果文件不存在就创建，存在就在文件内容的后面继续追加
print('print-text',file=bp)
bp.close()
#不进行换行输出（内容在一行当中）
print('hello','world','python')