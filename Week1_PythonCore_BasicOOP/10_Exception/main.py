def parse_row(row: dict) -> dict | None:
    try:
        clean = {
            "user_id": int(row["user_id"]),
            "amount": float(row["amount"])
        }
    except(KeyError, ValueError, TypeError) as e:
        print(f"[QUARANTINE]{row} -> {type(e).__name__}: {e}")
        return None
    else:
        return clean

raw_rows = [
    {"user_id": "1", "amount": "100.5"},
    {"user_id": "2", "amount": "N/A"},     # amount hỏng
    {"user_id": "x", "amount": "42"},      # user_id hỏng
    {"amount": "7.0"},                      # thiếu user_id
    {"user_id": "5", "amount": "88.0"},
]

good, bad = [], []
for row in raw_rows:
    result = parse_row(row)
    if result is None:
        bad.append(row)
    else:
        good.append(row)

print(f"Clean rows: {len(good)}, Error rows: {len(bad)}")