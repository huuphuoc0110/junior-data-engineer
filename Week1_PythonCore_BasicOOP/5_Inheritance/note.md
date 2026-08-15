### BÀI SỐ 5

# 1. Khi nào dùng inheritance? - Là mối quan hệ is-a(là một loại của)
# So sánh với quan hệ has - a (có một):

    Quan hệ     Ý nghĩa                     Nên dùng
    is-a        "Con là một loại của Cha"   Inheritance
    has-a       "A chứa/sở hữu B"           Composition (Bài tuần 2)

# 2. 'super()' - chìa khóa gọi ngược lên lớp cha

    class Shape:
        def __init__(self, name: str) -> None:
            self.name = name
            print(f"[LOG] Tao {name}")


    class Circle(Shape):
        def __init__(self, radius: float) -> None:
            super().__init__(name="Hinh tron")  # vẫn chạy log của cha
            self.radius = radius                # rồi thêm phần riêng

# 3. Polymorphism - Tính đa hình - "Cùng lời gọi nhưng khác hành vi"

