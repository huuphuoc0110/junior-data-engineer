import math

class Shape:
    """Class cha đại diện cho một hình học tổng quát"""

    def __init__(self, name: str)-> None:
        print(f"[LOG] Tao {name}")
        self.name = name

    def area(self) -> float:
        #Hình tổng quát chưa biết công thức tính diện tích
        #Class con BẮT BUỘC phải định nghĩa lại (override)
        raise NotImplementedError("Class con phải cài đặt area()")

    def describe(self)->str:
        #Phần chung: dùng chung cho mọi CLASS CON, không cần viết lại
        return f"{self.name} có diện tích {self.area():.2f}"
    
class Circle(Shape):
    """Hình tròn - là một loại của shape"""

    def __init__(self, radius: float) -> None:
        super().__init__(name= "Hinh tron")     #gọi __init__ của Shape
        self.radius = radius

    def area(self) -> float:                    # override area()
        return math.pi * (self.radius**2)

class Square(Shape):
    """Hình vuông - là một loại của shape"""

    def __init__(self, side: float) -> None:
        super().__init__(name= "Hinh vuong")    #gọi __init__ của Shape
        self.side = side

    def area(self) -> float:                    # override area()
        return self.side**2

# Polymorphism 
def tong_dien_tich(shapes: list[Shape]) -> float:
    return sum(shape.area() for shape in shapes)

if __name__ == "__main__":
    data = [Circle(1), Square(2), Circle(3)]
    print(f"Tong: {tong_dien_tich(data):.2f}")  # Tong: 32.42