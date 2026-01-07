# Danh sách ví dụ
my_list = ["Python", "Java", "C++", "JavaScript"]

# Mở file để ghi (overwrite)
with open('D:/b.txt', 'w', encoding='utf-8') as file:
    for item in my_list:
        file.write(item + '\n')  # Ghi mỗi phần tử xuống dòng

print("Đã ghi danh sách vào file b.txt")

# Mở file lại để đọc và hiển thị nội dung
with open('D:/b.txt', 'r', encoding='utf-8') as file:
    content = file.read()

print("\nNội dung file b.txt hiện tại:")
print(content)
