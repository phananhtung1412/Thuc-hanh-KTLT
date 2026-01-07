# Mở file nguồn và đọc nội dung
with open('D:/a.txt', 'r', encoding='utf-8') as source_file:
    content = source_file.read()

# Mở file đích và ghi nội dung
with open('D:/c.txt', 'w', encoding='utf-8') as dest_file:
    dest_file.write(content)

print("Đã sao chép nội dung từ a.txt sang c.txt")

# Mở file đích và hiển thị nội dung
with open('D:/c.txt', 'r', encoding='utf-8') as dest_file:
    print("\nNội dung file c.txt sau khi sao chép:")
    print(dest_file.read())
