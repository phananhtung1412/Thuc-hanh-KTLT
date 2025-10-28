S = input("Nhập chuỗi: ") 
ketqua = "" 
for ch in S: 
    if not ch.isdigit(): 
        ketqua += ch 
print("Chuỗi sau khi bỏ số:", ketqua) 
