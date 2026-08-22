def tong_so(path):
    try:
        f = open(path, "r", encoding = "utf-8")
        total = 0
        for line in f:
            num = line.strip()
            if not num:
                continue
            try:
                total += int(num)
            except ValueError:
                continue
        return total
    except FileNotFoundError:
        print(f"Không mở được file: {path}")
        return 0
    finally:
        f.close()

print(tong_so("numbers.txt"))