#[Trung bình] Viết hàm safe_divide(a, b) chia a cho b. 
# Bắt ZeroDivisionError (trả None + in cảnh báo) và TypeError (trả None + in “Kiểu dữ liệu không hợp lệ”). 
# Dùng finally in "Đã thực hiện phép chia." mỗi lần gọi. Test với (10, 2), (5, 0), (10, "x").

def safe_divide(a: float, b: float) -> float|None:
    try:
        return a / b
    except ZeroDivisionError:
        print("Mẫu số không thể bằng 0")
        return None
    except TypeError:
        print("Kiểu dữ liệu không hợp lệ")
        return None
    finally:
        print("Đã thực hiện phép chia")


print(safe_divide(10,2))

print(safe_divide(5,0))

print(safe_divide(10,"x"))