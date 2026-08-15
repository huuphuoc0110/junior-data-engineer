# my_math.py

#1. Example
def add(x: float, y: float) -> float:
    return x+y

def average(numbers: list[float]) -> float:
    #return 0.0 if lists are blank 
    if not numbers:
        return 0.0
    return sum(numbers)/len(numbers)

def percent_change(old: float, new: float) -> float:
    """Tính phần trăm thay đổi từ 'old' sang 'new'
    Ví dụ doanh thu từ 100 -> 120 return 20 (20%)
    """
    if old == 0:
        raise ValueError("Giá trị cũ bằng 0, không tính được phần trăm thay đổi")
    return (new - old)/old * 100

def is_in_range(value: float, low: float, high: float) -> bool:
    return low <= value <= high

#thử thách
def summarize(numbers: list[float]) -> dict:
    if not numbers:
        return [0.0, 0.0, 0.0, 0.0, 0.0]
    return{
        "count": len(numbers),
        "sum": sum(numbers),
        "mean": sum(numbers)/len(numbers),
        "min": min(numbers),
        "max": max(numbers)
    }
    
if __name__ == "__main__":
    arr = [3,2,4,5,1]
    print("Summarize: ", summarize(arr))
    
