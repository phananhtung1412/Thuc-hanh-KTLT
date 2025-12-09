import numpy as np

# Định nghĩa kiểu dữ liệu cho mảng: tên, lớp, chiều cao
dtype = [('name', 'U15'), ('class', int), ('height', float)]

# Dữ liệu sinh viên
students_data = [
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.10),
    ('Pit', 5, 40.11)
]

# Tạo structured array
students = np.array(students_data, dtype=dtype)

# In mảng ban đầu
print("Danh sách sinh viên ban đầu:")
for s in students:
    print(f"Tên: {s['name']}, Lớp: {s['class']}, Chiều cao: {s['height']}")

# Sắp xếp theo chiều cao
sorted_students = np.sort(students, order='height')

# In mảng đã sắp xếp
print("\nDanh sách sinh viên sắp xếp theo chiều cao:")
for s in sorted_students:
    print(f"Tên: {s['name']}, Lớp: {s['class']}, Chiều cao: {s['height']}")
