import numpy as np

# Tạo mảng từ 12 đến 37
arr = np.arange(12, 38)
print("Mảng được tạo:")
print(arr)

# Đảo ngược mảng
reversed_arr = arr[::-1]  # slicing với step = -1
print("Mảng đảo ngược:")
print(reversed_arr)
