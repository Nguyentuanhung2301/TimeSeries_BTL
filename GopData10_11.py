import csv

# Đường dẫn các file
oct_path = r"C:\Users\nguye\CODE\TimeSeries\BTL\Final_Data\Data\2019-Oct.csv"
nov_path = r"C:\Users\nguye\CODE\TimeSeries\BTL\Final_Data\Data\2019-Nov.csv"
dec_path = r"C:\Users\nguye\CODE\TimeSeries\BTL\Final_Data\Data\2019-Dec.csv"
output_path = r"C:\Users\nguye\CODE\TimeSeries\BTL\Final_Data\Data\2019_Data.csv"

# Bước 1: Lấy user mua hàng trong tháng 11 (dành cho churn của tháng 10)
users_purchased_in_nov = set()
with open(nov_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['event_type'] == 'purchase':
            users_purchased_in_nov.add(row['user_id'])

# Bước 2: Lấy user mua hàng trong tháng 12 (dành cho churn của tháng 11)
users_purchased_in_dec = set()
with open(dec_path, 'r', encoding='utf-8') as f:
    reader = csv.DictReader(f)
    for row in reader:
        if row['event_type'] == 'purchase':
            users_purchased_in_dec.add(row['user_id'])

# Bước 3: Mở file đầu ra và ghi dữ liệu của tháng 10 và 11 kèm nhãn churn
with open(output_path, 'w', newline='', encoding='utf-8') as out_file:
    writer = None

    # ---------- Gộp tháng 10 ----------
    with open(oct_path, 'r', encoding='utf-8') as f_oct:
        reader = csv.reader(f_oct)
        header = next(reader)
        header.append("churn")  # Thêm nhãn churn
        writer = csv.writer(out_file)
        writer.writerow(header)

        for row in reader:
            uid = row[header.index("user_id")]
            churn = "0" if uid in users_purchased_in_nov else "1"
            row.append(churn)
            writer.writerow(row)

    # ---------- Gộp tháng 11 ----------
    with open(nov_path, 'r', encoding='utf-8') as f_nov:
        reader = csv.reader(f_nov)
        next(reader)  # bỏ header

        for row in reader:
            uid = row[header.index("user_id")]
            churn = "0" if uid in users_purchased_in_dec else "1"
            row.append(churn)
            writer.writerow(row)

print("✅ Đã gộp dữ liệu tháng 10 và 11, gán nhãn churn theo tháng kế tiếp (tháng 11 & 12).")
