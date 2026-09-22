class Rect:
    def __init__(self, l, b):
        self.l = l
        self.b = b

    def area(self):
        return self.l * self.b

    def perimeter(self):
        return 2 * (self.l + self.b)


obj_area = Rect(10, 5)

print(obj_area.area())       # 50
print(obj_area.perimeter())  # 30