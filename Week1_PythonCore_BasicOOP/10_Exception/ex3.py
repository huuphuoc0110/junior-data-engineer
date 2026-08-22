#[Thử thách] Mô phỏng một bước ETL: 
# cho danh sách dict bản ghi (một số thiếu key "quantity", một số có "quantity" là chuỗi không parse được). 
# Viết pipeline gom thành valid (đã ép quantity sang int) và errors (dict gốc kèm thông điệp lỗi trong khóa "reason"). 
# Cuối cùng in tỉ lệ dòng lỗi theo phần trăm: error_rate = ∣ e r r o r s ∣ ∣ r e c o r d s ∣ × 100 error_rate= ∣records∣ ∣errors∣ ​ ×100. 
# Nếu tỉ lệ lỗi vượt 20%, raise ValueError("Nguồn dữ liệu quá bẩn, dừng pipeline")

def etl_pipeline(records):
    """
    Process ETL pipeline: validate and transform records
    - Separate valid records (quantity successfully converted to int) 
    - Separate error records (with 'reason' key explaining the error)
    - Calculate error rate and raise ValueError if > 20%
    """
    valid = []
    errors = []
    
    for record in records:
        try:
            # Check if 'quantity' key exists
            if 'quantity' not in record:
                raise KeyError("Missing 'quantity' key")
            
            # Try to convert quantity to int
            quantity = int(record['quantity'])
            
            # If successful, add to valid list with quantity as int
            valid.append({**record, 'quantity': quantity})
        
        except (KeyError, ValueError, TypeError) as e:
            # Add original record with error reason
            error_record = record.copy()
            error_record['reason'] = str(e)
            errors.append(error_record)
    
    # Calculate error rate as percentage
    total_records = len(records)
    error_rate = (len(errors) / total_records * 100) if total_records > 0 else 0
    
    print(f"Error rate: {error_rate:.2f}%")
    
    # Check if error rate exceeds 20%
    if error_rate > 20:
        raise ValueError("Nguồn dữ liệu quá bẩn, dừng pipeline")
    
    return valid, errors


# Test the pipeline
if __name__ == "__main__":
    # Sample data with various issues
    records = [
        {'id': 1, 'name': 'Product A', 'quantity': '10'},     # Valid: string convertible to int
        {'id': 2, 'name': 'Product B', 'quantity': 5},        # Valid: already int
        {'id': 3, 'name': 'Product C'},                       # Error: missing quantity key
        {'id': 4, 'name': 'Product D', 'quantity': 'abc'},    # Error: can't convert to int
        {'id': 5, 'name': 'Product E', 'quantity': '20'},     # Valid
    ]
    
    try:
        valid, errors = etl_pipeline(records)
        print(f"\nValid records ({len(valid)}):")
        for v in valid:
            print(f"  {v}")
        print(f"\nError records ({len(errors)}):")
        for e in errors:
            print(f"  {e}")
    except ValueError as e:
        print(f"Pipeline stopped: {e}")