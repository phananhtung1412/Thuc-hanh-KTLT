class Circle(object):
    def __init__(self, r):
        self.radius = r

    def area(self):
        return self.radius ** 2 * 3.14


# Ví dụ sử dụng
aCircle = Circle(2)
print(aCircle.area())   # 12.56
