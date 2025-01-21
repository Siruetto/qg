a = 20
b = 20
c = 30
print("a和b是同一个对象",a is b)
print("a和c是同一个对象",a is c)
print("a和c不是同一个对象",a is not c)

d = "python"
e = "py"
print(e in d)
f = [10,20,30]
print(10 not in f)