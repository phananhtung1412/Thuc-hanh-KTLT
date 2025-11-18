class Nguoi(object):
    def getGender(self):
        return "Unknown"


class Nam(Nguoi):
    def getGender(self):
        return "Nam"


class Nu(Nguoi):
    def getGender(self):
        return "Nữ"


# Sử dụng
aNam = Nam()
aNu = Nu()

print(aNam.getGender())  # Nam
print(aNu.getGender())   # Nữ
