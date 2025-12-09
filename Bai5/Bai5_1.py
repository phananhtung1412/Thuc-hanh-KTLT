# File: main.py
import mymath  # Import module mymath

values = [2, 4, 6, 8, 10]  # Danh sách số để tính

# Tính bình phương từng phần tử
print('Squares:')
for v in values:
    print(mymath.square(v))  # Gọi hàm square từ module

# Tính lập phương từng phần tử
print('Cubes:')
for v in values:
    print(mymath.cube(v))  # Gọi hàm cube từ module

# Tính trung bình cộng
print('Average:', mymath.average(values))  # Gọi hàm average từ module

# Sử dụng alias cho module
import mymath as mt  # Đặt tên viết tắt mt
print('Alias example:')
print(mt.square(2))
print(mt.cube(3))
