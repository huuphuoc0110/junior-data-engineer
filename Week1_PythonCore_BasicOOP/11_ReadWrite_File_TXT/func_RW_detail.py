def loc_doanh_thu_cao(input_path, output_path, nguong):
    f_in = None
    f_out = None
    try:    
        f_in = open(input_path, "r", encoding="utf-8")
        f_out = open(output_path, "r", encoding="utf-8")
        for line in f_in:
            parts = line.strip().split(",")
            if len(parts) != 3:
                continue                #pipeline không được dừng chỉ vì một dòng dữ liệu bẩn
            ngay, mon, gia = parts
            if int(gia) >= nguong:
                f_out.write(line)
    except FileNotFoundError:
        print(f"Không tìm thấy file {input_path}")
    finally:
        if f_in:
            f_in.close()
        if f_out:
            f_out.close()        

        