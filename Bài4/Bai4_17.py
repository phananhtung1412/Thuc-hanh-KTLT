n = int(input("Nhập số nguyên n: ")) 
for i in range(1, n): 
    for j in range(2, i): 
        if i % j == 0 and j > i // j: 
            print(i) 
            break 
