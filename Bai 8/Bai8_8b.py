from tkinter import *
from tkinter import messagebox

root = Tk()
root.title("Radio Button Example")
root.geometry("300x200")

Label(root, text="Chọn một số:", font=("Arial", 12)).pack(pady=10)

# Biến lưu lựa chọn radio
choice = IntVar()
choice.set(1)   # giá trị mặc định

# Tạo radio buttons
Radiobutton(root, text="1", variable=choice, value=1).pack()
Radiobutton(root, text="2", variable=choice, value=2).pack()
Radiobutton(root, text="3", variable=choice, value=3).pack()

# Hàm xử lý Click Me
def show_choice():
    messagebox.showinfo("Lựa chọn", f"Bạn đã chọn: {choice.get()}")

Button(root, text="Click Me", command=show_choice).pack(pady=10)

root.mainloop()
