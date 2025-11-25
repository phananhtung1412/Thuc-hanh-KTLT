import tkinter as tk

# ----------------------------------------
# (a) Xây dựng hàm xử lý khi chọn radio
# ----------------------------------------
def handle_selection():
    result_label.config(text=f"Bạn chọn: {choice.get()}")

# ----------------------------------------
# Tạo cửa sổ chính
# ----------------------------------------
window = tk.Tk()
window.title("Radio Button Indicator")
window.geometry("350x250")

# Biến lưu lựa chọn
choice = tk.StringVar()
choice.set("Lựa chọn 1")

# ----------------------------------------
# (b) Tạo radio button dạng indicator tùy chỉnh
# Gợi ý: dùng indicatoron = 0
# ----------------------------------------
rb1 = tk.Radiobutton(window,
                     text="Lựa chọn 1",
                     variable=choice,
                     value="Lựa chọn 1",
                     indicatoron=0,   # đổi radio button thành dạng button (indicator)
                     width=15,
                     pady=8,
                     bg="lightblue",
                     fg="black",
                     command=handle_selection)

rb2 = tk.Radiobutton(window,
                     text="Lựa chọn 2",
                     variable=choice,
                     value="Lựa chọn 2",
                     indicatoron=0,
                     width=15,
                     pady=8,
                     bg="lightgreen",
                     fg="black",
                     command=handle_selection)

rb3 = tk.Radiobutton(window,
                     text="Lựa chọn 3",
                     variable=choice,
                     value="Lựa chọn 3",
                     indicatoron=0,
                     width=15,
                     pady=8,
                     bg="pink",
                     fg="black",
                     command=handle_selection)

# Hiển thị các indicator button
rb1.pack(pady=5)
rb2.pack(pady=5)
rb3.pack(pady=5)

# Nhãn hiển thị kết quả
result_label = tk.Label(window, text="Bạn chọn: Lựa chọn 1", font=("Arial", 12))
result_label.pack(pady=15)

# Chạy chương trình
window.mainloop()
