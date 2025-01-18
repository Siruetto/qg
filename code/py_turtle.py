import turtle # 导入模块

turtle.showturtle() # 显示箭头
turtle.write("你好 世界！")
turtle.forward(300) # 前进300个像素
turtle.color("red") # 改变画笔的颜色
turtle.left(90) # 箭头左转90度
turtle.forward(300)
turtle.goto(0,0) # 回到坐标系的点(0,0)
turtle.penup() # 抬起笔，不画出路径
turtle.goto(0,50)
turtle.pendown() # 放下笔，画出路径
turtle.circle(100) # 画一个半径为100的圆

turtle.done() # 程序结束，可以保持窗口一直存在