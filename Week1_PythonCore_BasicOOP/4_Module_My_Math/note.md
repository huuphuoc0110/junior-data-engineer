#Lesson 4 
#1. MODULE -> là một file .py chứa code dùng chung -> import để mượn về xài, thay vì copy paste khắp nơi

#2. Một dự án pipeline điển hình có cấu trúc kiểu:
my_pipeline/
├── extract.py       # đọc dữ liệu từ nguồn
├── transform.py     # biến đổi, làm sạch
├── load.py          # ghi vào kho dữ liệu
└── my_math.py       # các hàm tính toán dùng chung  <-- module của chúng ta

#3. Các khái niệm cơ bản
Khái niệm           Ý nghĩa                             Ví dụ
Module              Một file .py                        my_math.py, transform.py
Package             Một thư mục chứa nhiều module       thư mục my_pipeline/
Standard Libary     Module có sẵn của python            math, statistics, json, csv
Third-party         cài qua pip                         pandas, pyspark, dlt


#4. Ba kiểu 'import':

#Kiểu 1: Import cả module -> gọi qua tiền tố
import my_math
my_math.add(100, 200)

#Kiểu 2: import 1 hàm cục thể -> gọi trực tiếp
from my_math import add, average, percent_change
average([1, 2, 3])

#Kiểu 3: đặt bí danh (alias) -> gọn cho tên dài
import my_math as mm
mm.average([1, 2, 3])

Kiểu                Cú pháp                             Nên dùng khi
Import module       import my_math                      Muốn rõ ràng hàm đến từ đâu (khuyến nghị)
Import tên cụ thể   from my_math import average         Chỉ cần vài hàm, gọi nhiều lần
Alias               import my_math as mm                Tên module dài, hoặc theo quy ước (import pandas as pd)



#5. Biến '__name__' và khối 'if __name__ == "__main__"'
#Nếu bạn chạy trực tiếp file đó (python my_math.py) -> __name__ == "__main__".
#Nếu file bị import bởi file khác -> __name__ == "my_math" (tên module).

#python my_math.py -> in ra kết quả test.
#import my_math trong transform.py -> khối test im lặng, chỉ nạp các hàm.

#6. module chỉ định nghĩa hàm/hằng số; công việc nặng đặt trong hàm, gọi khi cần.