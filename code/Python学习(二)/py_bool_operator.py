a = True
b = 3
c = a + b
print(c)
print('空字符串的布尔类型的值：',bool(""))
print('空列表的布尔类型的值：',bool([]))
print('None的布尔类型的值：',bool(None))
print('0的布尔类型的值：',bool(0))
print('字符串True和False转成布尔都是True：',bool("False"))

# 测试逻辑运算符
d,e,f=10,20,30
print((d<e) and (e<f))
print((d>e) or (e>f))
print(not (e<f))

# 测试比较运算符
x = 10>30 and 50<=100
y = 100>200 and 50<(3/0) # 发生短路问题，即便3/0有错误，系统也不会计算50<(3/0)
print(x)
print(y)
z = 4
if(3<z<10): # 相当于z>3,z<10
    print("z在3和10之间")

# 测试位运算符
g = 0b11001
h = 0b01000

print(bin(g|h))
print(bin(g&h))
print(bin(g^h))

print(3<<2)
print(20>>1)