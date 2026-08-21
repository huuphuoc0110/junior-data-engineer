#[Thử thách] Mô phỏng một bước ETL: 
# cho danh sách dict bản ghi (một số thiếu key "quantity", một số có "quantity" là chuỗi không parse được). 
# Viết pipeline gom thành valid (đã ép quantity sang int) và errors (dict gốc kèm thông điệp lỗi trong khóa "reason"). 
# Cuối cùng in tỉ lệ dòng lỗi theo phần trăm: error_rate = ∣ e r r o r s ∣ ∣ r e c o r d s ∣ × 100 error_rate= ∣records∣ ∣errors∣ ​ ×100. 
# Nếu tỉ lệ lỗi vượt 20%, raise ValueError("Nguồn dữ liệu quá bẩn, dừng pipeline")