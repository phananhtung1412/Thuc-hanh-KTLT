# Nhập số dòng cần đọc
n = int(input("Nhập số dòng muốn đọc: "))

# Mở file
with open('D:/a.txt', 'r', encoding='utf-8') as file:
    print(f"{n} dòng đầu tiên của file:")
    
    # Duyệt từng dòng
    for i in range(n):
        line = file.readline()
        if line == '':  # Nếu file hết dòng trước n dòng
            break
        print(line, end='')  # end='' để không thêm dòng mới nữa
