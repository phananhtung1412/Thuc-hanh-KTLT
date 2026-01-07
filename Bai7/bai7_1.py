# Mở file để đọc
input_file = open('D:/a.txt', 'r')

# Đọc toàn bộ nội dung file
content = input_file.read()

# Đảo ngược nội dung
reversed_content = content[::-1]

# In ra màn hình
print("Nội dung gốc:")
print(content)
print("\nNội dung đảo ngược:")
print(reversed_content)

# Đóng file
input_file.close()
