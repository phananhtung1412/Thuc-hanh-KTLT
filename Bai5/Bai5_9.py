# Hàm tìm kiếm nhị phân
def binary_search(lst, value):
    lower, upper = 0, len(lst)-1          # Giới hạn đầu và cuối của danh sách
    while lower <= upper:                 # Lặp cho tới khi hết phạm vi
        mid = (lower + upper) // 2       # Vị trí giữa
        if lst[mid] == value:            # Nếu giá trị ở mid bằng value
            return True                   # Trả về True
        elif lst[mid] < value:           # Nếu mid nhỏ hơn value
            lower = mid + 1              # Tìm nửa bên phải
        else:                            # Nếu mid lớn hơn value
            upper = mid - 1              # Tìm nửa bên trái
    return False                          # Không tìm thấy

# Nhập danh sách từ bàn phím, các phần tử cách nhau bằng dấu cách
lst = sorted([int(x) for x in input("Nhập các phần tử: ").split()])  # Tự sắp xếp tăng dần

# Nhập phần tử cần tìm
value = int(input("Nhập phần tử cần tìm: "))

# Gọi hàm tìm kiếm và in kết quả
if binary_search(lst, value):
    print(f"{value} được tìm thấy trong danh sách")  # Nếu tìm thấy
else:
    print(f"{value} không có trong danh sách")       # Nếu không tìm thấy
