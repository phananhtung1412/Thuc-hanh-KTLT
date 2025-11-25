import turtle

# Tạo đối tượng bút vẽ
pen = turtle.Turtle()

# Đặt tốc độ vẽ (1: chậm – 10: nhanh – 0: rất nhanh)
pen.speed(3)

# Vẽ hình vuông
for i in range(4):
    pen.forward(100)   # vẽ đường thẳng dài 100 pixel
    pen.right(90)      # quay bút 90 độ sang phải

# Chờ người dùng đóng cửa sổ
turtle.done()
