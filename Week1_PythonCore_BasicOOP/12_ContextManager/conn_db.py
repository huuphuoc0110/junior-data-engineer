import sqlite3


class DatabaseConnection:
    def __init__(self, db_path):
        self.db_path = db_path
        self.conn = None

    def __enter__(self):
        print(f"[DB] Mở kết nối tới {self.db_path}")
        self.conn = sqlite3.connect(self.db_path)
        return self.conn  # trả về connection để dùng sau 'as'

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is None:
            self.conn.commit()   # không lỗi -> lưu thay đổi
            print("[DB] Commit thành công")
        else:
            self.conn.rollback() # có lỗi -> hoàn tác, giữ dữ liệu sạch
            print(f"[DB] Rollback vì lỗi: {exc_val}")
        self.conn.close()
        print("[DB] Đã đóng kết nối")
        return False  # vẫn ném lỗi ra ngoài để pipeline biết mà báo động


# Sử dụng trong một bước của pipeline
with DatabaseConnection(":memory:") as conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE events (id INTEGER, name TEXT)")
    cur.execute("INSERT INTO events VALUES (1, 'page_view')")
    print("[ETL] Đã nạp 1 dòng vào bảng events")
