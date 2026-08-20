# temps = [23, -5, 45, 150, 30, 99, -1, 12]

# valid = [t for t in temps if 0 <= t <= 100]
# print(valid)

##data quality
# orders = [
#     {"id": 1, "amount": 250, "status": "paid"},
#     {"id": 2, "amount": 0,   "status": "cancelled"},
#     {"id": 3, "amount": 990, "status": "paid"},
#     {"id": 4, "amount": -10, "status": "error"},
#     {"id": 5, "amount": 120, "status": "paid"},
# ]

# # Chỉ giữ đơn đã thanh toán và số tiền dương -> dữ liệu "sạch" cho tầng sau
# clean = [o for o in orders if o["status"] == "paid" and o["amount"] > 0]


# for o in clean:
#     print(o["id"], o["amount"])


temps = [23, -5, 45, 150]

# if-else Ở BIỂU THỨC: gắn nhãn, KHÔNG loại phần tử nào
labels = ["ok" if 0 <= t <= 100 else "bad" for t in temps]
print(labels)  # ['ok', 'bad', 'ok', 'bad']

# if Ở CUỐI: loại phần tử không đạt
kept = [t for t in temps if 0 <= t <= 100]
print(kept)    # [23, 45]
