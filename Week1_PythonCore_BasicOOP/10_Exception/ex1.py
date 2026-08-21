#Viết hàm to_int(text) nhận một chuỗi. Nếu chuyển được sang int thì trả về số đó, 
# nếu ValueError thì trả về 0 và in "Không phải số: <text>". Test với "42", "abc", "".

def to_int(text: str) -> int:
    try:
        value = int(text)
    except ValueError:
        print(f"Không phải số: <{text}>")
        return 0
    else:
        return value

print(to_int("42"))

print(to_int("abc"))

print(to_int(""))
    