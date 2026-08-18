# [Dễ] 
# Viết decorator dem_lan_goi in ra số lần một hàm đã được gọi 
# (gợi ý: dùng một thuộc tính gắn trên wrapper hoặc biến nonlocal). 
# Áp dụng lên một hàm xu_ly_batch() và gọi 3 lần.

import functools

def dem_lan_goi(func):
    count = 0
    @functools.wraps(func)
    def wrapper():
        nonlocal count
        count += 1
        print(f"[COUNT] {func.__name__} da duoc goi {count} lan")
    return wrapper

@dem_lan_goi
def xu_ly_batch():
    return 0

xu_ly_batch()
xu_ly_batch()
xu_ly_batch()