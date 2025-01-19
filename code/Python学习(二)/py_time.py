import time

a = int(time.time())
print(a)
totalMinutes = a//60
print(totalMinutes)
totalDays = totalMinutes//(60*24)
print(totalDays)
totalYears = totalDays//365 # 不考虑闰年
print(totalYears)