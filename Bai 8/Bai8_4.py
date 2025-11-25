import tkinter as tk
from tkinter import messagebox

# -----------------------------------------
# (c) Hàm xử lý sự kiện khi bấm nút
# -----------------------------------------
def on_button_click():
    messagebox.showinfo("Thông báo", "Bạn đã nhấn nút!")

# -----------------------------------------
# (a) Tạo cửa sổ đồ họa Window Form
# -----------------------------------------
window = tk.Tk()
window.title("Demo Tkinter - Button")
window.geometry("350x200")

# -----------------------------------------
# (b + d) Tạo Button và đổi màu nền + màu chữ
# -----------------------------------------
btn = tk.Button(
    window,
    text="Bấm vào đây",
    command=on_button_click,
    bg="lightblue",      # màu nền
    fg="red",            # màu chữ
    font=("Arial", 14)   # phông chữ đẹp hơn
)
btn.pack(pady=40)

# -----------------------------------------
# Chạy cửa sổ
# -----------------------------------------
window.mainloop()
