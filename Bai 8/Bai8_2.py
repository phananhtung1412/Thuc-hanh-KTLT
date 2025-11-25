import turtle

# Tạo màn hình
screen = turtle.Screen()
screen.bgcolor("white")

# Tạo bút vẽ
pen = turtle.Turtle()
pen.speed(0)          # tốc độ vẽ nhanh
pen.color("red")       # màu nét vẽ
pen.pensize(2)         # độ dày nét

# Vẽ một cánh hoa
for i in range(36):
    pen.circle(100)    # vẽ 1 cung tròn bán kính 100
    pen.left(10)       # xoay nhẹ 10 độ tạo các cánh hoa

# Vẽ tâm hoa
pen.color("yellow")
pen.begin_fill()
pen.circle(30)
pen.end_fill()

# Giữ cửa sổ khi vẽ xong
turtle.done()
