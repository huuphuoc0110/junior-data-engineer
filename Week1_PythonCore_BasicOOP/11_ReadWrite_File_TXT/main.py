# ##BA CÁCH ĐỌC FILE PHỔ BIẾN

# #1. read() - đọc toàn bộ vào một chuỗi
# f = open("sales.txt", "r", encoding = "utf-8")
# content = f.read()
# f.close()
# print(content)


# #2. readlines() - đọc thành list các dòng
# f = open("sales.txt", "r", encoding = "utf-8")
# lines = f.readlines()
# f.close()
# for line in lines:
#     print(line)


# #3. Lặp trực tiếp trên file - cách chuẩn DE
# f = open("sales.txt", "r", encoding="utf-8")
# total = 0
# for line in f:                 # đọc TỪNG dòng, không nạp hết vào RAM
#     ngay, mon, gia = line.strip().split(",")
#     total += int(gia)
# f.close()
# print("Tổng doanh thu:", total)  # Tổng doanh thu: 120000


##   GHI FILE - ĐƯA KẾT QUẢ PIPELINE RA NGỒI

# #1. write() - ghi 1 chuỗi
# f = open("report.txt", "w", encoding="utf-8")
# f.write("Báo cáo doanh thu\n")    
# f.write("Tổng: 120000\n")
# f.close()


# #2. writelines() - ghi một list chuỗi
# rows = ["tra_sua,90000\n", "ca_phe,30000\n"]
# f = open("summary.txt", "w", encoding="utf-8")
# f.writelines(rows)   # LƯU Ý: cũng KHÔNG tự thêm '\n'
# f.close()


# Mỗi lần pipeline chạy, ghi thêm 1 dòng log, KHÔNG xoá log cũ
f = open("pipeline.log", "a", encoding="utf-8")
f.write("2026-07-18 03:00 - Job load_sales THÀNH CÔNG\n")
f.close()