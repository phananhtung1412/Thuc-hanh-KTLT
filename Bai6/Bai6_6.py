class IOString:
    """
    Class quản lý chuỗi, cho phép nhận chuỗi từ người dùng 
    và in chuỗi đó dưới dạng chữ in hoa.
    """
    def __init__(self):
        # Khởi tạo thuộc tính str1 để lưu chuỗi 
        self.str1 = "" 

    def get_String(self):
        """
        Phương thức nhận chuỗi từ người dùng qua hàm input().
        """
        print("--- Phương thức get_String đang chạy ---")
        self.str1 = input("Mời nhập một chuỗi: ")

    def print_String(self):
        """
        Phương thức in chuỗi đã lưu dưới dạng chữ in hoa.
        """
        print("\n--- Phương thức print_String đang chạy ---")
        print("Chuỗi in hoa:")
        # Sử dụng phương thức .upper() để chuyển chuỗi thành chữ in hoa
        print(self.str1.upper())

# --- Chương trình chính để kiểm tra (Test Run) ---
print("Bắt đầu thực thi chương trình...")

# 1. Khởi tạo đối tượng IOString
str_handler = IOString()

# 2. Gọi phương thức get_String
# Chương trình sẽ tạm dừng tại đây và chờ bạn nhập dữ liệu
str_handler.get_String() 

# 3. Gọi phương thức print_String
str_handler.print_String()

print("\nKết thúc chương trình.")

# Ví dụ Đầu vào/Đầu ra nếu bạn nhập "hello world":
# Mời nhập một chuỗi: hello world
# Chuỗi in hoa:
# HELLO WORLD
