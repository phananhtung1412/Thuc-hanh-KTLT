from tkinter import *

root = Tk()
root.title("Thông Tin Cá Nhân")
root.geometry("350x250")

# Tiêu đề
Label(root, text="THÔNG TIN CÁ NHÂN", font=("Arial", 14), fg="blue").pack(pady=10)

# Nội dung thông tin
Label(root, text="Họ và tên     : Nguyễn Văn A", font=("Arial", 11)).pack(anchor="w", padx=20)
Label(root, text="Ngày sinh    : 01/01/2000", font=("Arial", 11)).pack(anchor="w", padx=20)
Label(root, text="MSSV            : 123456789", font=("Arial", 11)).pack(anchor="w", padx=20)
Label(root, text="Ngành học   : Công nghệ thông tin", font=("Arial", 11)).pack(anchor="w", padx=20)

root.mainloop()
