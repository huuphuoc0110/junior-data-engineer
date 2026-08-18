import time
import functools

def do_thoi_gian(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.perf_counter()
        result = func(*args, **kwargs)      #chuyển tiếp tham số
        elapsed = time.perf_counter() - start
        print(f"[TIMER] {func.__name__} chay het {elapsed:.4f}s")
    return wrapper

@do_thoi_gian
def doc_csv(bath, rows=1000):
    """Doc file csv vao pipeline"""
    time.sleep(0.3)
    return f"Da doc {rows} dong tu {bath}"

result = doc_csv("customer.csv", rows=2000)

print(result) 