# Mở file để đọc
input_file = open('D:/a.txt', 'r', encoding='utf-8')

# Đọc toàn bộ nội dung
content = input_file.read()

# In ra nội dung
print("Nội dung file:")
print(content)

# Đóng file
input_file.close()
