class ManagedResource:
    def __enter__(self):
        print(">> Đang mở tài nguyên...")
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        print(">> Đang đóng tài nguyên...")
        return False

try:
    with ManagedResource() as res:
        print("Đang làm việc bên trong khối")
        raise ValueError("Dữ liệu hỏng!")
except ValueError as e:
    print(f"     Bắt được lỗi ở ngoài: {e}")       