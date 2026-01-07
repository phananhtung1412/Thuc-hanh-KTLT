# main.py
from mysort10 import bubbleSort

# Nhập danh sách từ bàn phím
n = int(input("Nhập số phần tử của danh sách: "))
nlist = []

for i in range(n):
    num = int(input(f"Nhập phần tử thứ {i+1}: "))
    nlist.append(num)

print("Danh sách ban đầu:", nlist)

# Sắp xếp bằng bubbleSort
sorted_list = bubbleSort(nlist)
print("Danh sách sau khi sắp xếp:", sorted_list)
