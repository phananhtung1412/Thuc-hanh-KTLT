# Nhập danh sách từ bàn phím
n = int(input("Nhập số lượng phần tử: "))
lst = [float(input(f"Nhập phần tử {i+1}: ")) for i in range(n)]

# In danh sách ban đầu
print("Danh sách ban đầu:", lst)

# Sắp xếp danh sách
sorted_lst = sorted(lst)
print("Danh sách sau khi sắp xếp:", sorted_lst)

# Tìm giá trị lớn nhất và nhỏ nhất
max_val = max(lst)
min_val = min(lst)

# In kết quả
print("Phần tử lớn nhất:", max_val)
print("Phần tử nhỏ nhất:", min_val)
