import numpy as np

# Dữ liệu đầu vào
student_id = np.array([1023, 5202, 6230, 1671, 1682, 5241, 4532])
student_height = np.array([40., 42., 45., 41., 38., 40., 42.0])

# Sắp xếp theo chiều cao, nếu bằng nhau thì theo student_id
# lexsort nhận thứ tự ưu tiên từ phải sang trái
indices = np.lexsort((student_id, student_height))

print("Chỉ số sắp xếp:")
print(indices)

print("\nDữ liệu sau khi sắp xếp:")
for i in indices:
    print(student_id[i], student_height[i])
