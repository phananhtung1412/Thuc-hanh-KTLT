ds = input("Nhập danh sách: ").split() 
x = input("Nhập phần tử cần tìm: ") 
if x in ds: 
    print("Vị trí của", x, "là:", ds.index(x)) 
else: 
    print(x, "không có trong danh sách") 
