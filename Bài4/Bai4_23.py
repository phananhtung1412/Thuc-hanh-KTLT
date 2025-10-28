chuoi = input("Nhập chuỗi: ") 
chu_cai = 0 
chu_so = 0 
for ch in chuoi: 
    if ch.isalpha(): 
        chu_cai += 1 
    elif ch.isdigit(): 
        chu_so += 1 
print("Chữ cái:", chu_cai) 
print("Chữ số:", chu_so) 
