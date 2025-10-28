import math

pos = [0, 0]  # vị trí ban đầu

while True:
    s = input("Nhập lệnh (UP/DOWN/LEFT/RIGHT bước) hoặc Enter để kết thúc: ")
    if not s:  # nếu nhập rỗng thì dừng
        break

    movement = s.split(" ")
    direction = movement[0].upper()  # chuyển về chữ hoa để đồng nhất
    steps = int(movement[1])

    if direction == "UP":
        pos[0] += steps
    elif direction == "DOWN":
        pos[0] -= steps
    elif direction == "LEFT":
        pos[1] -= steps
    elif direction == "RIGHT":
        pos[1] += steps
    else:
        print("Lệnh không hợp lệ!")

# Tính khoảng cách từ gốc (0,0)
distance = int(round(math.sqrt(pos[0]**2 + pos[1]**2)))
print("Khoảng cách là:", distance)
