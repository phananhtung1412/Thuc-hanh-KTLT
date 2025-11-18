class Bank:
    # Thuộc tính mặc định của Class
    Account_Type = "Savings"
    location = "Guntur"

    def __init__(self, name, Account_Number, balance):
        # Thiết lập thuộc tính của đối tượng
        self.name = name
        self.Account_Number = Account_Number
        self.balance = balance
        self.Account_Type = Bank.Account_Type
        self.location = Bank.location

    def repr(self):
        """Phương thức chào mừng và yêu cầu nhập mã PIN."""
        print("Welcome to the SBI ATM Machine ")
        print("------------------------------")
        
        # Mã PIN cứng được đặt là 123
        account_pin = int(input("Please enter your pin number: "))
        
        if (account_pin == 123):
            self.Account()
        else:
            print("Pin Incorrect. Please try again")
            # Sử dụng return để thoát khỏi hàm nếu sai PIN
            return 

    def Account(self):
        """Phương thức kiểm tra PIN và hiển thị menu chính."""
        # Mã PIN được kiểm tra lại ở đây (mặc dù đã kiểm tra trong repr)
        account_pin = int(input("Please enter your pin number: "))
        
        if (account_pin == 123):
            # Nếu PIN đúng, hiển thị thông tin thẻ và menu
            print("Your Card Number is: XXXX XXXX XXXX 1337")
            print("Would you like to Deposit/Withdraw/Check Balance?")
            print("1) Balance")
            print("2) Withdraw")
            print("3) Deposit")
            print("4) Quit")

            # --- Vòng lặp chính để xử lý lựa chọn của người dùng ---
            while True:
                # option = int(input("Please enter your choice: ")) - Dòng này bị lỗi cú pháp trong ảnh, nên sửa lại
                try:
                    option = int(input("Please enter your choice (1-4): "))
                except ValueError:
                    print("Lựa chọn không hợp lệ. Vui lòng nhập số.")
                    continue

                if (option == 1):
                    self.Balance()
                elif (option == 2):
                    self.Withdraw()
                elif (option == 3):
                    self.Deposit()
                elif (option == 4):
                    self.Exit()
                    break # Thoát khỏi vòng lặp sau khi thoát
                else:
                    print("Lựa chọn không hợp lệ. Vui lòng chọn từ 1 đến 4.")

        else:
            print("Pin Incorrect. Please try again")
            # Thoát khỏi hàm Account nếu PIN sai lần thứ hai
            return

    # --- Phương thức 1: Kiểm tra số dư ---
    def Balance(self):
        """Hiển thị số dư hiện tại."""
        print("\nBalance:", self.balance)
        # Tự động gọi lại Account() để hiển thị menu sau khi hoàn thành giao dịch
        self.Account()

    # --- Phương thức 2: Rút tiền ---
    def Withdraw(self):
        """Xử lý giao dịch rút tiền."""
        try:
            w = int(input("Please Enter Desired amount: "))
        except ValueError:
            print("Số tiền nhập vào không hợp lệ.")
            return

        # Kiểm tra điều kiện: số tiền muốn rút > 0 VÀ số dư >= số tiền muốn rút
        if (w > 0 and self.balance >= w):
            self.balance = self.balance - w # Cập nhật số dư
            print("Your transaction is successfull")
            print("Your Balance:", self.balance)
            print(" ")
        else:
            print("Your transaction is cancelled due to:")
            print("Amount is not sufficient in your account OR Amount is invalid.")

        self.Account()

    # --- Phương thức 3: Gửi tiền ---
    def Deposit(self):
        """Xử lý giao dịch gửi tiền."""
        try:
            d = int(input("Please Enter Desired amount: "))
        except ValueError:
            print("Số tiền nhập vào không hợp lệ.")
            return

        # Kiểm tra số tiền gửi phải dương
        if d > 0:
            self.balance = self.balance + d # Cập nhật số dư
            print("Your transaction is successfull")
            print("Your Balance:", self.balance)
        else:
            print("Số tiền gửi không hợp lệ.")

        self.Account()

    # --- Phương thức 4: Thoát ---
    def Exit(self):
        """Thoát khỏi chương trình."""
        print("\nExit: Thank you for using the ATM. Goodbye!")
        # Không cần gọi self.Account() ở đây để kết thúc chương trình

# --- Khởi tạo và chạy chương trình ---
# Khởi tạo đối tượng Bank: (Tên khách hàng, Số tài khoản, Số dư ban đầu)
t1 = Bank("Mahesh", 1453210145, 5000)

# Bắt đầu chương trình bằng cách gọi phương thức repr
t1.repr()
