# Nhập số dòng muốn đọc từ cuối
n = int(input("Nhập số dòng cuối cùng muốn đọc: "))

# Mở file để đọc
with open('D:/a.txt', 'r', encoding='utf-8') as file:
    # Đọc tất cả các dòng vào một list
    lines = file.readlines()

# Lấy n dòng cuối cùng
last_n_lines = lines[-n:] if n <= len(lines) else lines

# Hiển thị các dòng
print(f"{n} dòng cuối cùng của file:")
for line in last_n_lines:
    print(line, end='')  # end='' vì dòng đã có ký tự \n
