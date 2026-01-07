# Hàm tìm kiếm tuyến tính
def Sequential_Search(dlist, item):
    for i, value in enumerate(dlist):  # Duyệt danh sách kèm index
        if value == item:               # Nếu tìm thấy
            return True, i              # Trả về True và index
    return False, -1                    # Không tìm thấy

# Nhập số lượng phần tử
n = int(input("Nhập số lượng phần tử của danh sách: "))

# Nhập danh sách n phần tử
dlist = [int(input(f"Nhập phần tử {i+1}: ")) for i in range(n)]

# Nhập phần tử cần tìm
item = int(input("Nhập phần tử cần tìm: "))

# Gọi hàm tìm kiếm
found, index = Sequential_Search(dlist, item)

# In kết quả
if found:
    print(f"Phần tử {item} được tìm thấy tại vị trí {index}")
else:
    print(f"Phần tử {item} không được tìm thấy")

