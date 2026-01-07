# Nhập văn bản muốn nối vào file
text_to_append = input("Nhập văn bản muốn nối vào file: ")

# Mở file ở chế độ append (nối)
with open('D:/a.txt', 'a', encoding='utf-8') as file:
    file.write(text_to_append + '\n')  # Thêm xuống dòng sau văn bản mới

# Mở lại file để đọc toàn bộ nội dung
with open('D:/a.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Hiển thị nội dung file
print("\nNội dung file hiện tại:")
print(content)
