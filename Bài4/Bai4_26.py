tong_tien = 0 
while True: 
    du_lieu = input("Nhập giao dịch (D/W số) hoặc nhấn Enter để dừng: ") 
    if not du_lieu: 
        break 
    lenh = du_lieu.split() 
    if lenh[0] == 'D': 
        tong_tien += int(lenh[1]) 
    elif lenh[0] == 'W': 
        tong_tien -= int(lenh[1]) 
print("Số tiền hiện có là:", tong_tien)
