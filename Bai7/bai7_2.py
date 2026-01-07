# Mở file để đọc
input_file = open('D:/a.txt', 'r', encoding='utf-8')

# Đọc toàn bộ nội dung
content = input_file.read()

# Đếm số ký tự
num_chars = len(content)

# Đếm số từ (cắt theo khoảng trắng)
num_words = len(content.split())

# Đếm số dòng
num_lines = len(content.splitlines())

# In kết quả
print("Số ký tự trong file:", num_chars)
print("Số từ trong file:", num_words)
print("Số dòng trong file:", num_lines)

# Đóng file
input_file.close()
