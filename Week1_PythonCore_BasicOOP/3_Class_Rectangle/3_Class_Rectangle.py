### 1. Create class Rectangle
##  1.1. Note:
#   - __init__ -> constructor: 
#   - self -> đối tượng đang được tạo. self.width: Lưu tham số width vào đối tượng self
## 1.2. Code: 
# class Rectangle:
#     def __init__(self, width: float, height: float) -> None:
#         self.width = width
#         self.height = height
# rect = Rectangle(4, 3)

# print(rect.width)
# print(rect.height)


### 2. Add method: area and perimeter
##  2.1. Note:
#   - Thuộc tính : self.width
#   - Method : rect.area()
#   - self: tham số đầu vào của method 
##  2.2. Code:
# class Rectangle:
#     #initial
#     def __init__(self, width: float, height: float) -> None:
#         self.width = width              #attribute
#         self.height = height

#     #method
#     def area(self) -> float:
#         return self.width * self.height

#     def perimeter(self) -> float:
#         return (self.width * self.height)*2

# rect = Rectangle(3.5, 7)

# print (rect.area())
# print (rect.perimeter())


### 3. Add setter validation: chặn số âm

##  3.2. Code:
# class Rectangle:
#     def __init__(self, width: float, height: float) -> None:
#         self.width = width              
#         self.height = height

#     @property
#     def width(self) -> float:
#         return self._width

#     @width.setter
#     def width(self, value: float) -> None:
#         if value <= 0:
#             raise ValueError(f"Width phai > 0 , nhan duoc {value}")
#         self._width = value

#     @property
#     def height(self) -> float:
#         return self._height

#     @height.setter
#     def height(self, value: float) -> None:
#         if value <= 0:
#             raise ValueError(f"height phai > 0 , nhan duoc {value}")
#         self._height = value

#     @property
#     def area(self) -> float:
#         return self._width * self._height

# rect = Rectangle(4, 3)
# print(rect.area)     # 12

# rect.width = 10
# print(rect.area)     # 30

# rect.width = -5    # -> ValueError: width phai > 0, nhan duoc -5
# print(rect.area)