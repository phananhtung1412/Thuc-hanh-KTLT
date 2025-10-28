data = input("Nhập các số nhị phân, cách nhau bởi dấu phẩy: ").split(',') 
for b in data: 
    if int(b, 2) % 5 == 0: 
        print(b) 
