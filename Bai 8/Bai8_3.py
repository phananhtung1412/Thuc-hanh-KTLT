import turtle

# Tạo màn hình
screen = turtle.Screen()
screen.bgcolor("white")

# Tạo bút vẽ
pen = turtle.Turtle()
pen.speed(0)          # tốc độ nhanh nhất
pen.pensize(2)

colors = ["red", "green", "blue"]   # 3 màu lặp lại

# Vẽ 18 vòng tròn xoay quanh tâm
for i in range(18):
    pen.color(colors[i % 3])   # thay đổi màu liên tục
    pen.circle(100)            # vẽ 1 vòng tròn bán kính 100
    pen.left(20)               # xoay 20 độ tạo hình hoa

turtle.done()
