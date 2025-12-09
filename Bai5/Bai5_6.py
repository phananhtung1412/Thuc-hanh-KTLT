# Nhập danh sách từ bàn phím
n = int(input("Nhập số lượng phần tử: "))
lst = [float(input(f"Nhập phần tử {i+1}: ")) for i in range(n)]

# Tìm giá trị lớn nhất, nhỏ nhất
max_val = max(lst)
min_val = min(lst)

# Tìm vị trí (index) của chúng
max_idx = lst.index(max_val)  # Vị trí đầu tiên xuất hiện giá trị lớn nhất
min_idx = lst.index(min_val)  # Vị trí đầu tiên xuất hiện giá trị nhỏ nhất

# In kết quả
print("Phần tử lớn nhất:", max_val, "tại vị trí:", max_idx)
print("Phần tử nhỏ nhất:", min_val, "tại vị trí:", min_idx)
