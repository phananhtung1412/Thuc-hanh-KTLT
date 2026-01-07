import numpy as np

# Tạo mảng có cấu trúc
dtype = [('name', 'U10'), ('class', int), ('height', float)]
students = np.array([
    ('James', 5, 48.5),
    ('Nail', 6, 52.5),
    ('Paul', 5, 42.1),
    ('Pit', 5, 40.11)
], dtype=dtype)

print("Danh sách ban đầu:")
print(students)

# Sắp xếp theo class, nếu class bằng nhau thì theo height
sorted_students = np.sort(students, order=['class', 'height'])

print("\nDanh sách sau khi sắp xếp:")
print(sorted_students)
