# Mở file
with open('D:/a.txt', 'r', encoding='utf-8') as file:
    content = file.read()

# Tách thành các từ
words = content.split()

# Tìm độ dài từ dài nhất
max_length = max(len(word) for word in words)

# Lấy tất cả từ có độ dài bằng độ dài tối đa
longest_words = [word for word in words if len(word) == max_length]

print("Những từ dài nhất trong file:", longest_words)
print("Độ dài từ dài nhất:", max_length)


