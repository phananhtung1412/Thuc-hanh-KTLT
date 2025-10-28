n = int(input("Nhập số dòng: ")) 
def pascal(n): 
    for i in range(n): 
        so = 1 
        for j in range(i + 1): 
            print(so, end=' ') 
            so = so * (i - j) // (j + 1) 
        print() 
pascal(n) 
