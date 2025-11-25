from tkinter import *
from tkinter import messagebox

# -------------------------------------
# Các hàm xử lý menu (Bước 3)
# -------------------------------------
def NewFile():
    messagebox.showinfo("Thông báo", "Bạn chọn: New File")

def OpenFile():
    messagebox.showinfo("Thông báo", "Bạn chọn: Open File")

def Exit():
    messagebox.showinfo("Thông báo", "Bạn chọn: Exit chương trình")
    root.quit()

def InsText():
    messagebox.showinfo("Thông báo", "Bạn chọn: Insert Text")

def InsPic():
    messagebox.showinfo("Thông báo", "Bạn chọn: Insert Picture")

def About():
    messagebox.showinfo("Thông tin", "Demo Menu Tkinter\nHệ thống hỗ trợ học tập")

# -------------------------------------
# Bước 1: Tạo Window Form + Menu
# -------------------------------------
root = Tk()
root.title("Demo Menu Tkinter")
root.geometry("400x300")

menu = Menu(root)
root.config(menu=menu)

# -------------------------------------
# Bước 2: Tạo các menu như hình
# File menu
# -------------------------------------
filemenu = Menu(menu, tearoff=0)
menu.add_cascade(label="File", menu=filemenu)

filemenu.add_command(label="New", command=NewFile)
filemenu.add_command(label="Open", command=OpenFile)
filemenu.add_separator()
filemenu.add_command(label="Exit", command=Exit)

# -------------------------------------
# Edit Menu
# -------------------------------------
editmenu = Menu(menu, tearoff=0)
menu.add_cascade(label="Edit", menu=editmenu)

editmenu.add_com_
