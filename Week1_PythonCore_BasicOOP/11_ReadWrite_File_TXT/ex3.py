def read_order_status_filter(input_path, output_path, status):
    f_in = None
    f_out = None
    try:
        f_in = open(input_path, "r", encoding = "utf-8")
        f_out = open(output_path, "w", encoding = "utf-8")

        total = 0
        valid = 0

        next(f_in)      #bỏ qua header
        for line in f_in:
            parts = line.strip().split(",")
            if len(parts) != 3:
                continue
            order_id, amount, order_status = parts
            total += 1

            if order_status == status:
                f_out.write(f"{order_id}, {amount}, {order_status}\n")
                valid += 1

        with open("etl.log", "a", encoding ="utf-8") as log:
            log.write(f"Đã xử lý {total} đơn, giữ lại {valid} hợp lệ\n")
    except FileNotFoundError:
        print(f"Không đọc được file: {input_path}")    
    finally:
        if f_in:
            f_in.close()
        if f_out:
            f_out.close()

input_path = r"D:\project\junior-data-engineer\Week1_PythonCore_BasicOOP\11_ReadWrite_File_TXT\raw_order.csv"

print(read_order_status_filter(input_path, "clean_order.csv", "paid"))