MAX_SPEED = 120
print(MAX_SPEED) # 输出120
MAX_SPEED = 140 # 实际是可以改的，只是逻辑上不做修改
print(MAX_SPEED) # 输出140

#使用系列解包赋值实现变量值交换
a,b = 1,2
a,b = b,a # 变量值互换
print(a,b) # 输出2 1